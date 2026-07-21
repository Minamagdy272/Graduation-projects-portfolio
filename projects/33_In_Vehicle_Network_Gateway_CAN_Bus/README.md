# In-Vehicle Network Gateway with CAN-Bus Security Layer

---

## Executive Summary

This project proposes the design and implementation of an **In-Vehicle Network (IVN) Security Gateway with a CAN-Bus Intrusion Detection Layer**. Modern vehicles contain 70–150 Electronic Control Units (ECUs) communicating over the CAN (Controller Area Network) bus — a protocol with zero authentication or encryption. This gateway sits between internal vehicle networks, enforces communication policies between domains (powertrain, chassis, infotainment), and uses an anomaly-detection module to identify malicious CAN frame injections that indicate an active cyberattack.

**Motivation:** Vehicle cybersecurity is a critical and rapidly growing field. Since 2015, researchers have demonstrated remote takeover of Jeep Cherokee, Tesla, BMW, and other vehicles by exploiting the unprotected CAN bus. Modern regulations (UNECE WP.29 / ISO 21434) now mandate cybersecurity management for all new vehicle models globally. Yet CAN bus security education is extremely rare — there are almost no academic projects in this domain. Building this gateway provides unique expertise in automotive protocols, embedded security, and real-time anomaly detection on constrained hardware.

**Objectives:**
- Implement a CAN frame parser for standard and extended CAN frames, plus CAN-FD.
- Build a configurable firewall (message filtering table) that enforces communication policies between vehicle domains.
- Implement rule-based detection signatures for known attack patterns (replay attacks, frame spoofing, ID flooding).
- Build an anomaly-detection ML module that learns normal CAN traffic patterns and flags statistical deviations.
- Log all security events to an immutable audit trail and expose a secure diagnostic interface.

**Expected Impact:** An automotive-grade security gateway demonstrating expertise in safety-critical embedded systems, real-time signal processing, and applied anomaly detection — one of the most specialized and valuable skills in the automotive industry.

**Target Users:** Automotive OEMs (car manufacturers), Tier-1 automotive suppliers (Bosch, Continental, Aptiv), and national vehicle type-approval agencies.

---

## Problem Statement

The CAN bus was designed in 1983 for reliability, not security:

1. **No Authentication:** Any ECU on the CAN bus can send any message. A compromised infotainment system (connected to the internet via Bluetooth/Wi-Fi) can inject brake or steering commands to powertrain ECUs.
2. **No Encryption:** All CAN messages are transmitted in plaintext. Physical access to the OBD-II port gives full read/write access to all ECU communications.
3. **No Authorization:** The CAN bus has no concept of "only the ABS module should send wheel speed messages."
4. **Real-Time Constraint:** CAN operates at up to 5 Mbps. Security processing must happen within the message's time-critical window (often < 1ms) without disrupting real-time communication.
5. **Regulatory Pressure:** ISO 21434 and UNECE WP.29 R155/R156 now mandate vehicle cybersecurity management, creating an immediate commercial need for products like this gateway.

---

## Existing Solutions

### Commercial Solutions
- **Argus Cyber Security / Upstream Security:** Leading vehicle IDS vendors. Proprietary, enterprise.
- **Vector Informatik / ETAS:** Automotive tool vendors with security modules.
- **Bosch / Continental:** Implementing security gateways in production vehicles.

### Open-Source Solutions
- **SocketCAN (Linux):** Linux CAN subsystem for accessing CAN hardware. (Driver layer only, no security.)
- **OpenXC (Ford):** Vehicle data API. (Read-only, no security enforcement.)

### Limitations
- No open-source project implements a complete IVN security gateway with both rule-based filtering and ML anomaly detection.
- The regulatory and safety requirements make this a uniquely challenging domain rarely explored in academia.

---

## Proposed Solution

Build **AeroGateway IVN**, an in-vehicle security gateway:

1. **Hardware Platform:** A Raspberry Pi 4 with a MCP2515 CAN controller or a dedicated automotive development board (e.g., PiRacer with CAN HAT). Connects to a CAN bus network composed of multiple ECU simulators.
2. **ECU Simulation Network:** Python-based ECU simulators (using `python-can`) generating realistic CAN traffic: engine RPM messages, ABS wheel speed reports, airbag system status, and infotainment heartbeats.
3. **CAN Frame Parser:** A C/C++ parser that decodes raw CAN frames (arbitration ID, DLC, data bytes) and maps them to signal definitions using a DBC (Database CAN) file.
4. **Domain Firewall Engine:** A configurable message filtering table enforcing routing policies between network domains. Example: "Messages from the Infotainment domain with Engine Control IDs (0x100–0x1FF) shall be DROPPED." Rules are stored as a JSON policy file and hot-reloadable.
5. **Anomaly Detection Module:** An ML model trained on normal CAN traffic patterns (inter-frame timing distribution, message frequency per ID, payload value ranges). Flags deviations such as unexpected message bursts (ID flooding attack), unusual payload values, or timing irregularities.
6. **Security Event Logger:** All detected incidents are written to an immutable append-only log (with cryptographic hash chaining) on the gateway. A secure UDS diagnostic service exposes logs to authorized tools.

---

## System Architecture

### Hardware / Embedded
- **Platform:** Raspberry Pi 4 (Linux) with CAN HAT (MCP2515) or Vector VN1630A interface.
- **CAN Interfaces:** Two or more CAN buses (simulating domain separation: powertrain, body, infotainment).

### Backend (Gateway Software)
- **Language:** C/C++ for the performance-critical CAN frame processing loop and firewall engine (real-time constraints).
- **Language:** Python for the anomaly detection training and inference pipeline (offline training + C inference via ONNX Runtime).
- **Language:** Go for the management API and secure logging service.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| CAN Traffic Anomaly Detection | Flag statistically unusual CAN frames (ID flooding, replay, out-of-range payload values, timing anomalies) | Isolation Forest on message frequency + inter-frame timing features | ~20% |

**Total AI effort: ~20%.** Remove it → the gateway still enforces domain firewall rules and detects rule-based attacks. The ML layer catches novel, signature-free attacks.

### Databases
- **SQLite (on-device):** Local append-only security event log with hash chaining for tamper evidence.
- **PostgreSQL (optional cloud backend):** Aggregates security events from multiple gateways for fleet-wide threat intelligence.

### Networking
- **CAN Bus:** Physical communication with ECU simulators.
- **Ethernet / SOME/IP:** Diagnostic interface and remote log upload.
- **UDS (Unified Diagnostic Services):** ISO 14229 — standard automotive diagnostic protocol exposed on the secure diagnostic port.

### Security
- **Secure Boot:** Gateway software signed and verified on startup.
- **Tamper-Evident Logging:** Hash chaining on event log ensures log entries cannot be deleted or modified.
- **Domain Isolation:** Physical separation of CAN networks; cross-domain traffic must pass through the gateway.

---

## Research Opportunities

1. **CAN Attack Dataset Generation:** Create a labeled CAN attack dataset by injecting known attacks (fuzzing, replay, targeted ID spoofing) into the simulated network. This dataset itself is a research contribution.
2. **Real-Time ML Inference on Constrained Hardware:** Benchmark the latency of Isolation Forest inference on a Raspberry Pi 4 vs. the CAN bus message arrival rate to determine feasibility under real-time constraints.
3. **DBC Parsing and Signal Normalization:** Research the coverage and accuracy of automated DBC-based signal normalization for anomaly feature extraction.
4. **Gateway Overhead Impact:** Measure the latency overhead introduced by the security gateway on CAN bus message propagation under maximum load.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Languages** | C/C++ | CAN frame processing, firewall engine |
| | Python | ML training, python-can for ECU simulation |
| | Go | Management API, secure logging |
| **Hardware** | Raspberry Pi 4 | Gateway hardware platform |
| | MCP2515 / Vector interface | CAN hardware interface |
| **CAN Tools** | SocketCAN / python-can | CAN bus access |
| | DBC files | CAN signal database format |
| **AI** | Scikit-learn (Isolation Forest) | Anomaly detection training |
| | ONNX Runtime | On-device inference |
| **Standards** | ISO 11898 (CAN), ISO 14229 (UDS) | Automotive protocol standards |
| **DevOps** | Docker (for dev), cross-compilation | Build toolchain |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Technologies |
|--------|------|-----------------|--------------|
| **Member 1** | Embedded & CAN Systems | Implement the CAN frame capture loop, DBC parser, and domain firewall engine in C/C++. Configure SocketCAN. | C/C++, SocketCAN, DBC |
| **Member 2** | ECU Simulation Engineer | Build realistic Python ECU simulators generating authentic CAN traffic for all vehicle domains. | Python, python-can |
| **Member 3** | Anomaly Detection Engineer | Design features from CAN traffic, train Isolation Forest model offline, convert to ONNX for on-device inference. | Python, Scikit-learn, ONNX |
| **Member 4** | Security & Logging | Implement the hash-chained security event logger, UDS diagnostic service, and secure boot verification. | C/Go, Cryptography |
| **Member 5** | Dashboard & Attack Simulation | Build the remote monitoring dashboard; implement attack injection scripts (replay, ID flooding) for testing. | React, Python, Go |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| Raspberry Pi 4 (4GB) + CAN HAT | 5,000 | ~100 |
| CAN transceivers, wiring, breadboard | 1,500 | ~30 |
| Additional CAN hardware for ECU simulation | 2,000 | ~40 |
| **Total** | **~8,500 EGP** | **~170 USD** |

---

## Difficulty
**Score: 8/10** — Working with automotive protocols at the bit level, meeting real-time constraints on embedded Linux, and building a tamper-evident logging system requires deep embedded systems expertise.

## Innovation
**Score: 9/10** — An open-source, hardware-demonstrated IVN security gateway with ML anomaly detection is essentially nonexistent in the academic project space. This would be immediately relevant to the automotive cybersecurity industry.

## Sponsor Potential
**Score: 9/10** — Tier-1 automotive suppliers (Bosch, Continental, Valeo), OEMs, national transport authorities, and vehicle cybersecurity startups.

## Career Value
**Automotive Cybersecurity Engineer:** ⭐⭐⭐⭐⭐
**Embedded Systems Engineer:** ⭐⭐⭐⭐⭐
**Security Engineer:** ⭐⭐⭐⭐

---

## References

1. Miller, C., & Valasek, C. (2015). "Remote Exploitation of an Unaltered Passenger Vehicle." *DEF CON 23.*
2. ISO/SAE 21434:2021 — Road vehicles: Cybersecurity engineering.
3. UNECE WP.29 R155 — Cyber Security Regulation.
4. Avatefipour, O., & Rawassizadeh, R. (2019). "State-of-the-Art Survey on In-Vehicle Network Communication (CAN-Bus) Security." *arXiv.*
5. SocketCAN documentation: https://www.kernel.org/doc/html/latest/networking/can.html
