# Intrusion Detection System for Industrial Control Networks (SCADA/ICS)

---

## Executive Summary

This project proposes the design and implementation of a **Network-Based Intrusion Detection System (NIDS) specifically designed for Industrial Control System (ICS) and SCADA (Supervisory Control and Data Acquisition) networks.** The system passively captures and deep-inspects industrial protocol traffic (Modbus, DNP3, IEC 61850, OPC-UA), enforces a rule-based behavioral baseline, and uses an anomaly-detection ML module as a second layer to flag unusual command sequences that rule signatures cannot anticipate.

**Motivation:** Industrial control systems manage power grids, water treatment plants, oil pipelines, and manufacturing facilities. Cyberattacks on ICS have caused real-world physical damage (Stuxnet destroyed Iranian centrifuges; the 2021 Oldsmar water treatment attack could have poisoned drinking water). These networks run legacy protocols with zero authentication or encryption, making them critically vulnerable. Yet traditional IT intrusion detection systems (like Snort or Suricata) are useless here because they do not understand Modbus or DNP3 packets. This project builds an ICS-native IDS from scratch.

**Objectives:**
- Implement a packet capture and deep inspection engine for industrial protocols (Modbus TCP, DNP3, IEC 60870-5-104).
- Build a rule-based detection engine enforcing protocol-level signatures (e.g., "write to coil address X during production hours is forbidden").
- Implement a behavioral baseline engine that learns normal command sequences during a training period.
- Add an anomaly-detection ML module that scores real-time traffic against the behavioral baseline.
- Provide a security operations dashboard visualizing active alerts, protocol traffic breakdown, and device communication graphs.

**Expected Impact:** A specialized cybersecurity platform protecting critical infrastructure — one of the most underfunded and vulnerable sectors in the world — with a unique combination of protocol-aware rule enforcement and ML anomaly detection.

**Target Users:** Power utilities, water treatment operators, oil & gas companies, manufacturing plants, and national cybersecurity agencies.

---

## Problem Statement

ICS/SCADA networks are uniquely vulnerable:

1. **Legacy Protocols Without Security:** Modbus (1979) and DNP3 (1990s) were designed for closed, air-gapped networks. They have no authentication, no encryption, and no integrity checking. Any device on the network can send any command.
2. **Operational Continuity Constraint:** Unlike IT systems, ICS cannot simply be patched or rebooted. A patch to a power plant controller could cause an outage. Security must be passive and non-intrusive.
3. **Protocol Diversity:** A single industrial facility may run Modbus, DNP3, IEC 61850, OPC-UA, and PROFINET simultaneously — each requiring specialized parsing.
4. **Slow, Low-Bandwidth Traffic:** ICS traffic is not high-throughput web traffic. It is slow, deterministic, and highly patterned — making anomaly detection both more achievable and more consequential when deviations occur.
5. **IT/OT Convergence:** As industrial networks connect to corporate IT networks and cloud systems for monitoring, they become exposed to internet-facing attacks.

---

## Existing Solutions

### Commercial Solutions
- **Claroty / Dragos / Nozomi Networks:** The leading ICS security vendors. Extremely expensive (enterprise licensing), closed source, and not accessible to students or smaller utilities.
- **Forescout:** General network visibility platform with ICS modules.

### Open-Source Solutions
- **Snort / Suricata:** Excellent general-purpose NIDS but no native ICS protocol parsers.
- **Bro/Zeek:** Network analysis framework with some community ICS protocol analyzers (basic Modbus support).
- **GRASSMARLIN (NSA):** Open-source ICS network mapping tool (topology only, no active detection).

### Limitations of Existing Solutions
- No open-source solution provides a complete pipeline: ICS protocol parsing → rule-based detection → ML anomaly scoring → security dashboard — in one integrated platform.
- GRASSMARLIN only maps topology; it does not detect attacks.
- Zeek's Modbus analyzer is basic; it does not support behavioral baselining or ML-based anomaly scoring.

---

## Proposed Solution

Build **AeroICS Guard**, an ICS-native NIDS:

1. **Packet Capture Engine:** A Go/C daemon using `libpcap`/`gopacket` to passively capture network traffic on a monitoring port (network TAP or SPAN port) without injecting any packets into the OT network.
2. **ICS Protocol Parser:** Implements parsers for:
   - **Modbus TCP:** Function codes (read/write coils, registers), slave addresses.
   - **DNP3:** Operation requests, data link layer parsing.
   - **IEC 60870-5-104:** ASDU (Application Service Data Unit) parsing.
3. **Rule-Based Detection Engine:** An efficient signature matcher (like a state machine) that evaluates parsed packets against a library of ICS-specific rules. Examples:
   - "Alert if a WRITE command is sent to PLC #3 coil address 100 outside maintenance window."
   - "Alert if any device sends a STOP CPU command to the PLC."
4. **Behavioral Baseline Engine:** During a learning period (e.g., 7 days), the system records the normal communication patterns: which source talks to which destination, which function codes are used, at what intervals. This becomes the baseline.
5. **Anomaly Detection Module:** An ML model (Isolation Forest or Autoencoder) that scores each packet's feature vector against the learned baseline. High anomaly scores trigger alerts.
6. **Security Dashboard:** A React UI showing live traffic graphs, device communication topology (force-directed graph), active alerts with severity, and protocol breakdown.

---

## System Architecture

### Backend
- **Packet Capture + Parsing:** Go with `gopacket` library (wraps libpcap). Parses raw bytes into structured Modbus/DNP3 events.
- **Detection Engine:** Go for rule evaluation (performance-critical, pattern matching).
- **Baseline & ML Scoring:** Python microservice consuming parsed events, maintaining the baseline, and running inference.
- **Alert Manager:** Go service that deduplicates, enriches, and routes alerts to the dashboard.

### Frontend
- **Dashboard:** React with TypeScript.
- **Network Topology:** D3.js force-directed graph showing which PLCs/RTUs communicate with which HMIs and servers.
- **Protocol Analysis:** Real-time counters showing function code distribution.

### Security
- **Passive-Only Design:** The system NEVER injects packets. It operates in read-only mode on a mirrored network port. This is non-negotiable for safety-critical environments.
- **Secure Storage:** Alerts and captured metadata stored with encryption at rest.
- **Access Control:** Role-based dashboard access (analyst, admin).

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Anomaly Detection | Score unusual command sequences against learned behavioral baseline | Isolation Forest on packet feature vectors (src, dst, function code, interval) | ~20% |

**Total AI effort: ~20%.** Remove it → rule engine still detects known attack signatures. The ML layer catches novel attacks that rules cannot anticipate.

### Databases
- **PostgreSQL:** Alert records, rule library, device inventory.
- **InfluxDB:** Time-series storage of per-device traffic metrics (function code counts per minute).
- **Redis:** Real-time sliding window state for anomaly detection.

### Networking
- **SPAN/TAP Port:** The IDS connects passively to a network switch monitoring port.
- **REST API:** Alert retrieval, rule management from the dashboard.
- **WebSocket:** Live alert streaming to the dashboard.

### DevOps
- **Docker:** All backend services containerized.
- **ICS Simulator:** ScadaBR or a custom Python Modbus server to generate realistic test traffic.
- **GitHub Actions:** CI/CD for automated testing.

### Monitoring
- **Prometheus:** Parser throughput, rule engine latency, alert rates.
- **Grafana:** Operational dashboards for the security team.

---

## AI Components

| Component | Technique | Training Data | Justification |
|-----------|-----------|---------------|---------------|
| Network Behavioral Anomaly Scoring | Isolation Forest trained on 7-day baseline of normal ICS traffic | Packet feature vectors: (src IP, dst IP, function code, register address, inter-packet interval) | Isolation Forests are fast for inference, require no labeled attack data (unsupervised), and produce interpretable anomaly scores. This is essential because labeled ICS attack datasets are extremely rare. |

---

## Research Opportunities

1. **ICS Protocol Fingerprinting:** Research the feasibility of passively identifying device types (vendor, model, firmware) solely from their Modbus/DNP3 communication patterns.
2. **Anomaly Detection on Slow, Bursty ICS Traffic:** Investigate whether standard anomaly detection methods (designed for high-rate IT traffic) require adaptation for the low-frequency, highly periodic nature of ICS communication.
3. **Attack Dataset Generation:** Create a novel labeled ICS attack dataset using simulation (replay attacks, command injection, unauthorized writes) — itself a research contribution.
4. **False Positive Rate in Operational Environments:** Evaluate whether behavioral baselining without ML produces an acceptable false positive rate in a real-world-simulated ICS environment.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Languages** | Go | Packet capture, protocol parsing, rule engine |
| | Python | ML anomaly detection service, baseline training |
| | TypeScript | Dashboard frontend |
| **Packet Capture** | gopacket (libpcap) | Raw network packet capture |
| **AI** | Scikit-learn (Isolation Forest) | Anomaly scoring |
| **Databases** | PostgreSQL | Alerts, rules, device inventory |
| | InfluxDB | Per-device traffic time-series |
| | Redis | Sliding window anomaly state |
| **Frontend** | React, D3.js | Dashboard and topology graph |
| **Simulation** | pyModbus / ScadaBR | Generate realistic ICS test traffic |
| **DevOps** | Docker, GitHub Actions | Deployment and CI/CD |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Technologies |
|--------|------|-----------------|--------------|
| **Member 1** | Protocol Parser Engineer | Implement the Modbus TCP and DNP3 binary parsers from RFCs. Extract function codes, addresses, and values from raw packet bytes. | Go, gopacket, Binary Parsing |
| **Member 2** | Rule Engine Engineer | Build the rule evaluation engine, design the rule DSL (domain-specific language), maintain the rule library for common ICS attacks (replay, unauthorized write). | Go, Pattern Matching |
| **Member 3** | Anomaly Detection Engineer | Build the behavioral baselining pipeline, train and deploy Isolation Forest, implement the sliding window feature extractor. | Python, Scikit-learn, Redis |
| **Member 4** | Alert Management & Backend | Build the alert deduplication, enrichment, and routing system; design PostgreSQL schema; build the REST API. | Go, Python, PostgreSQL |
| **Member 5** | Dashboard & ICS Simulation | Build the React dashboard and D3.js topology graph; set up ScadaBR or pyModbus to simulate realistic ICS traffic for testing. | React, D3.js, Python (pyModbus) |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| Cloud VMs for ICS simulation network | 5,000 | ~100 |
| Network TAP hardware (optional for demo) | 2,500 | ~50 |
| **Total** | **~7,500 EGP** | **~150 USD** |

---

## Difficulty
**Score: 8/10** — Writing binary protocol parsers from RFCs without libraries is extremely tedious and error-prone. The passive-only constraint and the absence of labeled attack data make the ML design more sophisticated than typical supervised learning projects.

## Innovation
**Score: 9/10** — An open-source, multi-protocol ICS NIDS with integrated ML anomaly detection is a genuine research contribution. No comparable open-source tool exists.

## Sponsor Potential
**Score: 9/10** — National cybersecurity agencies (Egypt CERT), electricity utilities, oil & gas companies, and ICS security firms.

## Startup Potential
**Score: 8/10** — ICS security is one of the fastest-growing cybersecurity verticals. A lightweight, affordable ICS-native IDS targeting developing-world utilities is a clear market gap.

---

## Career Value

| Career Path | Relevance |
|-------------|-----------|
| ICS / OT Security Engineer | ⭐⭐⭐⭐⭐ |
| Network Security Analyst | ⭐⭐⭐⭐⭐ |
| Cybersecurity Engineer | ⭐⭐⭐⭐ |
| Embedded / Systems Engineer | ⭐⭐⭐ |

---

## References

1. Stouffer, K., et al. (2015). *Guide to Industrial Control Systems (ICS) Security.* NIST SP 800-82 Rev. 2.
2. CISA ICS Advisories: https://www.cisa.gov/ics-advisories
3. Modbus Application Protocol Specification V1.1b3.
4. DNP3 Technical Reference: https://www.dnp.org/
5. Chandola, V., Banerjee, A., & Kumar, V. (2009). "Anomaly Detection: A Survey." *ACM Computing Surveys.*
