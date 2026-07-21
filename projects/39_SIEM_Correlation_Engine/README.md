# SIEM Correlation Engine

---

## Executive Summary

This project proposes the design and implementation of a **Security Information and Event Management (SIEM) Correlation Engine** — a high-performance, distributed log ingestion, normalization, cross-source event correlation, and security alerting platform. The system ingests logs from diverse enterprise sources (firewalls, Active Directory, web servers, endpoint agents), parses them into a standardized schema (OSSEM / ECS), applies stateful rule-based correlation across event streams, and uses an alert-prioritization scoring module to rank threats and reduce analyst alert fatigue.

**Motivation:** Modern Security Operations Centers (SOCs) are overwhelmed by millions of isolated log events daily. A single failed login is noise; a failed login followed by a privilege escalation, a firewall rule modification, and an outbound connection to an unknown IP within 5 minutes is a critical breach. Traditional SIEM solutions (Splunk, QRadar) cost hundreds of thousands of dollars and often flood security teams with false positives. Building a SIEM correlation engine teaches high-throughput stream processing, security domain modeling, stateful event correlation, and noise-reduction heuristics.

**Objectives:**
- Build a multi-tenant log ingestion and normalization pipeline supporting Syslog, Beats, and HTTP webhooks.
- Implement an event normalization engine mapping raw unstructured logs to Elastic Common Schema (ECS) format.
- Develop a Stateful Event Correlation Engine capable of evaluating complex multi-event temporal patterns (e.g., A followed by B within T seconds).
- Implement an Alert Prioritization Scoring Module that ranks correlated alerts based on asset criticalities, historical false-positive rates, and threat context.
- Provide a SOC Analyst Web Dashboard for alert investigation, timeline visualization, and rule management.

**Expected Impact:** A enterprise-grade cybersecurity platform demonstrating mastery of big data stream processing, rule engine design, security event correlation, and incident response workflows.

**Target Users:** Security Operations Center (SOC) teams, Managed Security Service Providers (MSSPs), enterprise IT security administrators, and compliance auditors.

---

## Problem Statement

1. **Massive Log Volume & Velocity:** Enterprise networks generate 5,000 to 50,000 events per second (EPS). Ingesting and processing this stream without dropping logs requires scalable data engineering.
2. **Siloed & Heterogeneous Formats:** Windows Event Logs, Syslog, Nginx access logs, and AWS CloudTrail all use completely different formats. Correlating across them requires schema normalization.
3. **Complex Attack Chain Detection:** Advanced Persistent Threats (APTs) execute multi-stage attacks across different systems over time. Simple single-event alerts fail to detect multi-stage attack chains.
4. **Severe Alert Fatigue:** SOC analysts face hundreds of false positives daily, leading to missed critical alerts and burnout.

---

## Existing Solutions

### Commercial Solutions
- **Splunk Enterprise Security:** Industry leader. Extremely expensive (per-GB indexing cost), complex SPL query language.
- **IBM QRadar / ArcSight:** Legacy enterprise SIEM systems. Heavy, slow rule engines.
- **Microsoft Sentinel:** Cloud-native SIEM. Powerful, but binds organizations to Azure infrastructure.

### Open-Source Solutions
- **Wazuh:** Open-source SIEM / XDR platform. Excellent agent-based detection, but complex configuration and limited custom correlation engine customization.
- **Apache Metron:** Apache big data security platform (now retired/archived by Apache Foundation).
- **Elastic Security (ELK):** Powerful search, but complex stateful multi-stream correlation rules require heavy enterprise licenses.

### Limitations of Existing Solutions
- Commercial SIEMs are prohibitively expensive for mid-market enterprises.
- Open-source platforms either lack intuitive multi-stream stateful temporal correlation capabilities or rely on complex static queries that consume immense database CPU.

---

## Proposed Solution

Build **AeroSIEM**, a distributed SIEM Correlation Engine:

1. **Ingestion & Normalization Pipeline:** High-performance Go-based ingestion workers receiving Syslog (UDP/TCP/TLS) and JSON webhooks. Maps raw incoming log lines to Elastic Common Schema (ECS) JSON format.
2. **Stream Message Bus:** Apache Kafka partition cluster for buffering raw and normalized log streams.
3. **Stateful Correlation Engine:** Built using Apache Flink or a custom Go CEP (Complex Event Processing) engine that evaluates temporal windowed rules (e.g., "3 failed SSH logins from IP $x$ followed by successful login from IP $x$ to admin account within 120 seconds").
4. **Alert Prioritization & Scoring Module:** An ML/Heuristic module (Gradient Boosting / Random Forest) that calculates a dynamic Risk Score ($0-100$) for generated alerts based on target asset criticality score, historical analyst feedback, and event frequency.
5. **Fast Search & Analytical Storage:** ClickHouse columnar database for sub-second log search and historical aggregation.
6. **SOC Analyst Dashboard:** React web application featuring a live alert queue, interactive event timeline, attack chain visualization (DAG of correlated events), and a visual rule builder.

---

## System Architecture

### Backend & Data Pipeline
- **Ingestion & Normalization:** Go (ultra-fast regex/grok parsing, low memory footprint).
- **Correlation Processing:** Apache Flink (Complex Event Processing API) or custom Go sliding-window correlation engine.
- **Management API:** Python FastAPI (Rule management, user administration, alert management).

### Frontend
- **SOC Dashboard:** React with TypeScript.
- **Visualization:** Cytoscape.js / D3.js for attack chain graph visualization; Recharts for EPS rates.

### Security
- **RBAC & Multi-Tenancy:** Role-based access control (SOC Tier 1 Analyst, Tier 2 Investigator, Admin).
- **TLS 1.3 Encryption:** For all Syslog-over-TLS, HTTP API, and inter-service communications.
- **Immutable Log Storage:** Cryptographic hash verification for archived log partitions to ensure forensic tamper evidence.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Dynamic Alert Prioritization | Score and rank correlated security alerts to suppress false positives and highlight true threats | XGBoost Classifier / Random Forest trained on analyst alert feedback features | ~15% |

**Total AI effort: ~15%.** If the ML prioritization module is removed, alerts are scored using static additive risk weights (e.g., Asset Value $\times$ Rule Severity). The correlation engine and SIEM remain 100% functional.

### Databases
- **ClickHouse:** Columnar database for high-throughput log storage and analytical search queries.
- **PostgreSQL:** Alert records, correlation rules, asset inventory metadata, user accounts.
- **Redis:** Active state tracking for sliding window event counters and session lookups.

### Networking
- **Syslog (RFC 5424 / RFC 3164):** Standard network log forwarding.
- **Kafka / gRPC:** High-speed internal message passing.
- **WebSockets:** Live alert streaming to the SOC dashboard.

### DevOps
- **Docker Compose & Helm:** Package complete stack for standalone or Kubernetes deployment.
- **Attack Simulation Scripts:** Automated Python scripts executing simulated attack patterns (brute force, port scan, lateral movement) to test correlation rules.

---

## Research Opportunities

1. **Correlation Engine Scaling Limits:** Benchmark stateful CEP engine throughput (EPS) vs. memory consumption under increasing sliding window sizes (5 min vs 1 hour).
2. **False Positive Suppression via ML:** Quantify the reduction in analyst alert review queue size achieved by XGBoost prioritization vs. static rule weighting.
3. **Log Normalization Overhead:** Compare Go regex parsing vs. SIMD-accelerated JSON/log parsing for high-velocity ECS mapping.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Languages** | Go | Log ingestion, ECS normalization, Syslog receiver |
| | Python | Management API, ML scoring microservice |
| | TypeScript | SOC Analyst frontend |
| **Stream Processing** | Apache Kafka | Event stream buffering |
| | Apache Flink / Custom Go CEP | Stateful correlation engine |
| **Databases** | ClickHouse | Columnar log search storage |
| | PostgreSQL | System metadata, rules, alerts |
| | Redis | Real-time sliding window cache |
| **AI / ML** | XGBoost, Scikit-learn | Alert risk scoring & prioritization |
| **Frontend** | React, Cytoscape.js, D3.js | Attack graph visualization & SOC UI |
| **DevOps** | Docker, Helm, GitHub Actions | Packaging, deployment, CI/CD |

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Elastic Common Schema (ECS) & Log Parsing | Essential | Elastic ECS specification documentation |
| Complex Event Processing (CEP) Concepts | Essential | Apache Flink CEP documentation / Distributed Systems literature |
| Columnar Databases (ClickHouse) | Essential | ClickHouse official documentation & benchmarks |
| Cyber Kill Chain & MITRE ATT&CK Framework | Essential | MITRE ATT&CK website & documentation |
| Go High-Concurrency Networking | Important | Go Concurrency Patterns (goroutines, channels) |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Key Technologies |
|--------|------|-----------------|------------------|
| **Member 1** | Ingestion & Parser Lead | Build Syslog/HTTP receivers in Go, implement regex/grok ECS log normalizer. | Go, Syslog, Regular Expressions |
| **Member 2** | Correlation Engine Eng. | Implement stateful temporal correlation rules (CEP engine) in Flink/Go for multi-stage attacks. | Apache Flink / Go, Kafka |
| **Member 3** | Search & Storage Eng. | Design ClickHouse schema, optimize log indexing, build high-speed search API endpoints. | ClickHouse, SQL, Go/Python |
| **Member 4** | AI & Prioritization Eng. | Develop alert scoring & false-positive reduction ML model; map rules to MITRE ATT&CK. | Python, XGBoost, Scikit-learn |
| **Member 5** | Frontend / SOC UI Developer | Develop React SOC dashboard, attack chain visualization graph, and alert management UI. | React, Cytoscape.js, WebSockets |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| Cloud Compute (High RAM for ClickHouse & Kafka cluster) | 12,000 | ~240 |
| Domain & TLS Certificates | 500 | ~10 |
| **Total** | **~12,500 EGP** | **~250 USD** |

---

## Difficulty
**Score: 8/10**
Requires processing high-velocity log streams without memory leaks, designing complex temporal correlation logic, optimizing ClickHouse queries, and building a responsive attack-graph UI.

---

## Innovation
**Score: 8/10**
Combines high-performance columnar log storage (ClickHouse), open-source CEP correlation, and ML-driven alert prioritization mapped directly to MITRE ATT&CK technique IDs.

---

## Career Value
**Security Operations (SOC) / SIEM Engineer:** ⭐⭐⭐⭐⭐
**Data Pipeline / Infrastructure Engineer:** ⭐⭐⭐⭐⭐
**Cybersecurity Software Developer:** ⭐⭐⭐⭐
