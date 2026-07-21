import os

PROJECTS_DIR = r"c:\GP\projects"

def write_readme(folder, text):
    filepath = os.path.join(PROJECTS_DIR, folder, "README.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"Updated: {folder}/README.md ({len(text.splitlines())} lines)")

projects_data = {
    "03_Zero_Trust_Network_Access_Platform": {
        "title": "Zero-Trust Network Access Platform",
        "domain": "Cybersecurity / Networking",
        "stack_main": "Go, WireGuard, Open Policy Agent (OPA), mTLS, FastAPI, React, PostgreSQL, Redis, ClickHouse",
        "primary_lang": "Go",
        "ai_tech": "Isolation Forest on access logs",
        "sponsor_egypt": "Vodafone Egypt, CIB Bank",
        "budget_egp": "28,000",
        "budget_usd": "560"
    },
    "04_Realtime_Collaborative_Code_Editor": {
        "title": "Real-time Collaborative Code Editor",
        "domain": "Developer Tools / Web Systems",
        "stack_main": "TypeScript, Node.js, WebSockets, Yjs (CRDTs), Monaco Editor, Docker, Go, React, Redis",
        "primary_lang": "TypeScript / Go",
        "ai_tech": "Lightweight N-gram / Transformer autocomplete hint",
        "sponsor_egypt": "Instabug, Valeo Egypt",
        "budget_egp": "18,000",
        "budget_usd": "360"
    },
    "05_Industrial_IoT_Predictive_Maintenance": {
        "title": "Industrial IoT Predictive Maintenance Platform",
        "domain": "IoT / Edge Computing",
        "stack_main": "C++, ESP32, MQTT, Python, Apache Kafka, InfluxDB, PostgreSQL, React, TensorFlow Lite",
        "primary_lang": "C++ / Python",
        "ai_tech": "Autoencoder & FFT vibration anomaly detection",
        "sponsor_egypt": "Elsewedy Electric, Ezz Steel",
        "budget_egp": "22,000",
        "budget_usd": "440"
    },
    "06_End_to_End_MLOps_Platform": {
        "title": "End-to-End MLOps Platform",
        "domain": "DevOps / AI Infrastructure",
        "stack_main": "Python, Go, Kubernetes, MLflow, Apache Airflow, Feast, FastAPI, MinIO, Evidently AI, React",
        "primary_lang": "Python / Go",
        "ai_tech": "Evidently AI statistical data drift monitoring",
        "sponsor_egypt": "Inception AI, Dell Technologies Egypt",
        "budget_egp": "25,000",
        "budget_usd": "500"
    },
    "08_Privacy_Preserving_Healthcare_Data_Exchange": {
        "title": "Privacy-Preserving Healthcare Data Exchange",
        "domain": "Healthcare Technology / Privacy",
        "stack_main": "Python, PySyft (Federated Learning), HAPI FHIR, PostgreSQL, Docker, FastAPI, React, mTLS",
        "primary_lang": "Python",
        "ai_tech": "Federated Learning with Differential Privacy",
        "sponsor_egypt": "Magdi Yacoub Heart Foundation, 57357 Hospital",
        "budget_egp": "20,000",
        "budget_usd": "400"
    },
    "09_Edge_Native_Video_Analytics_Pipeline": {
        "title": "Edge-Native Video Analytics Pipeline",
        "domain": "IoT / Computer Vision",
        "stack_main": "C++, Python, NVIDIA TensorRT, RTSP, GStreamer, MQTT, FastAPI, React, PostgreSQL",
        "primary_lang": "C++ / Python",
        "ai_tech": "YOLOv8 + DeepSORT object tracking optimized with TensorRT",
        "sponsor_egypt": "New Administrative Capital, Honeywell Egypt",
        "budget_egp": "32,000",
        "budget_usd": "640"
    },
    "10_Digital_Twin_Smart_Building_Management": {
        "title": "Digital Twin for Smart Building Management",
        "domain": "Smart Infrastructure / WebGL",
        "stack_main": "TypeScript, React, Three.js, Python, MQTT, TimescaleDB, PostgreSQL, Redis, Docker",
        "primary_lang": "TypeScript / Python",
        "ai_tech": "LSTM energy demand forecasting model",
        "sponsor_egypt": "Talaat Moustafa Group, Palm Hills",
        "budget_egp": "24,000",
        "budget_usd": "480"
    },
    "11_Peer_to_Peer_Energy_Trading_Platform": {
        "title": "Peer-to-Peer Energy Trading Platform",
        "domain": "Energy & Sustainability / FinTech",
        "stack_main": "Go, Solidity / Hyperledger Fabric, Web3.js, Python, InfluxDB, PostgreSQL, React, MQTT",
        "primary_lang": "Go / Python",
        "ai_tech": "Prophet renewable solar generation forecasting",
        "sponsor_egypt": "KarmSolar, Infinity Power",
        "budget_egp": "26,000",
        "budget_usd": "520"
    },
    "12_Realtime_Data_Lakehouse_Platform": {
        "title": "Real-time Data Lakehouse Platform",
        "domain": "Data Engineering / Big Data",
        "stack_main": "Java, Scala, Python, Apache Iceberg, Apache Flink, Apache Kafka, Trino, MinIO, Spark, React",
        "primary_lang": "Java / Python",
        "ai_tech": "Great Expectations & ML data quality anomaly scoring",
        "sponsor_egypt": "Vodafone Egypt Data Team, Fawry",
        "budget_egp": "30,000",
        "budget_usd": "600"
    },
    "13_Intelligent_API_Gateway": {
        "title": "Intelligent API Gateway",
        "domain": "Developer Tools / Networking",
        "stack_main": "Go, NGINX / Envoy, Lua, Redis, PostgreSQL, Python, Isolation Forest WAF, React, Prometheus",
        "primary_lang": "Go",
        "ai_tech": "Isolation Forest AI Web Application Firewall (WAF) abuse classifier",
        "sponsor_egypt": "Paymob, Instabug",
        "budget_egp": "22,000",
        "budget_usd": "440"
    },
    "14_Software_Defined_WAN_Controller": {
        "title": "Software-Defined WAN (SD-WAN) Controller",
        "domain": "Networking / Systems",
        "stack_main": "Python, Go, OpenFlow (Ryu), Mininet, WireGuard, IPsec, Prometheus, React",
        "primary_lang": "Python / Go",
        "ai_tech": "Q-Learning path loss dynamic route optimization",
        "sponsor_egypt": "Telecom Egypt (WE), Orange Egypt",
        "budget_egp": "25,000",
        "budget_usd": "500"
    },
    "15_Smart_City_Traffic_Optimization": {
        "title": "Smart City Traffic Flow Optimization System",
        "domain": "Smart Infrastructure / AI",
        "stack_main": "Python, SUMO Simulator, PyTorch / Ray RLlib, OpenCV, FastAPI, React, Leaflet",
        "primary_lang": "Python",
        "ai_tech": "Multi-Agent Deep Q-Learning (MARL) for traffic signal control",
        "sponsor_egypt": "New Administrative Capital, Siemens Egypt",
        "budget_egp": "28,000",
        "budget_usd": "560"
    },
    "17_Automated_Penetration_Testing_Framework": {
        "title": "Automated Penetration Testing Framework",
        "domain": "Cybersecurity / Red Teaming",
        "stack_main": "Python, Go, Neo4j Graph DB, Metasploit RPC API, Nmap, Docker, Celery, React, Redis",
        "primary_lang": "Python / Go",
        "ai_tech": "Reinforcement Learning (Q-learning) attack path planner",
        "sponsor_egypt": "CIB InfoSec, EG-CERT",
        "budget_egp": "24,000",
        "budget_usd": "480"
    },
    "19_Self_Healing_Infrastructure_Platform": {
        "title": "Self-Healing Infrastructure Platform",
        "domain": "DevOps / Site Reliability Engineering (SRE)",
        "stack_main": "Go, Kubernetes Operator SDK, Prometheus, AlertManager, Python, Redis, PostgreSQL, React",
        "primary_lang": "Go",
        "ai_tech": "Isolation Forest metric anomaly detector triggering automated K8s CRDs",
        "sponsor_egypt": "Vodafone Cloud Operations, ITIDA",
        "budget_egp": "26,000",
        "budget_usd": "520"
    },
    "20_Remote_Patient_Monitoring_Platform": {
        "title": "Remote Patient Monitoring Platform",
        "domain": "Healthcare Technology / IoT",
        "stack_main": "React Native, TypeScript, BLE, Python, MQTT, InfluxDB, PostgreSQL, Docker",
        "primary_lang": "TypeScript / Python",
        "ai_tech": "Time-series vital sign deterioration risk scoring model",
        "sponsor_egypt": "Vezeeta, El-Ezbawy Pharmacies",
        "budget_egp": "25,000",
        "budget_usd": "500"
    },
    "23_Distributed_Log_Analytics_Anomaly_Detection": {
        "title": "Distributed Log Analytics and Anomaly Detection",
        "domain": "Observability / Big Data",
        "stack_main": "Rust, Go, Apache Kafka, ClickHouse, Drain Parser, PyTorch (DeepLog LSTM), React",
        "primary_lang": "Rust / Go / Python",
        "ai_tech": "Drain NLP log template parser + DeepLog LSTM sequence anomaly detector",
        "sponsor_egypt": "Paymob Infrastructure, Raya Data Center",
        "budget_egp": "28,000",
        "budget_usd": "560"
    },
    "24_Smart_Agriculture_Monitoring_System": {
        "title": "Smart Agriculture Monitoring & Automation System",
        "domain": "AgriTech / IoT",
        "stack_main": "C++, ESP32, LoRaWAN (ChirpStack), Python, InfluxDB, PostgreSQL, PyTorch, React PWA",
        "primary_lang": "C++ / Python",
        "ai_tech": "PlantVillage CNN leaf disease classifier + Penman-Monteith irrigation ML",
        "sponsor_egypt": "DAL Group, SEKEM Organic Farms",
        "budget_egp": "22,000",
        "budget_usd": "440"
    },
    "25_Multi_Cloud_Cost_Intelligence_Platform": {
        "title": "Multi-Cloud Cost Intelligence Platform",
        "domain": "FinTech / Cloud Infrastructure",
        "stack_main": "Python, Apache Airflow, ClickHouse, MinIO, Meta Prophet, FastAPI, React, AG Grid, PostgreSQL",
        "primary_lang": "Python",
        "ai_tech": "Meta Prophet time-series cost forecasting & Isolation Forest cost spike detector",
        "sponsor_egypt": "Cloud Concept Egypt, AWS Community Egypt",
        "budget_egp": "25,000",
        "budget_usd": "500"
    }
}

def generate_markdown(folder, data):
    title = data["title"]
    domain = data["domain"]
    stack_main = data["stack_main"]
    primary_lang = data["primary_lang"]
    ai_tech = data["ai_tech"]
    sponsor_egypt = data["sponsor_egypt"]
    budget_egp = data["budget_egp"]
    budget_usd = data["budget_usd"]
    
    return f"""# {title}

---

## Executive Summary

This project proposes the design and implementation of a **{title}** — a production-grade system engineered for high performance, reliability, and enterprise scalability. The system addresses critical operational challenges in {domain} by building a robust architecture that integrates modern software engineering practices with a bounded AI subsystem.

**Motivation:** Modern enterprise systems demand high-throughput data handling, low-latency processing, and automated decision-making. Traditional approaches struggle with scale, static rules, or vendor lock-in. This project tackles the core engineering challenge of building a modular, resilient platform capable of operating continuously under demanding production workloads.

**Objectives:**
- Build a distributed system architecture processing thousands of operations per second with predictable low latency
- Implement robust fault tolerance, automated recovery, and strict security posture
- Design a high-performance data storage and streaming pipeline tailored to domain requirements
- Integrate a bounded AI module ({ai_tech}) to enhance operational decision-making without creating single-point-of-failure model dependencies
- Create an intuitive, real-time web dashboard for system monitoring, administration, and operational workflows

**Expected Impact:** A production-grade architecture demonstrating mastery of distributed systems, backend engineering, cloud infrastructure, and applied machine learning.

**Target Users:** Enterprise IT operations, security teams, engineering lead practitioners, and domain-specific operations personnel.

---

## Problem Statement

1. **System Scalability & Performance:** High-throughput processing demands optimized concurrency, non-blocking I/O, and efficient data serialization to prevent bottlenecks.

2. **Data Consistency & Reliability:** Managing state across distributed components requires strict transactional boundaries, idempotent execution, and robust recovery mechanisms.

3. **Operational Visibility:** Complex distributed architectures often lack real-time observability, making root-cause analysis and performance tuning difficult.

4. **Security & Access Control:** Securing inter-service communication, enforcing fine-grained access policies, and maintaining immutable audit logs are essential for enterprise compliance.

5. **Static vs. Adaptive Logic:** Hardcoded business rules fail to adapt to evolving environmental conditions, requiring machine-learning-assisted scoring to augment traditional rule engines.

---

## Existing Solutions

### Commercial Solutions
- **Enterprise SaaS Vendors:** Closed-source commercial products with high licensing costs and rigid integration paths.
- **Cloud Provider Managed Services:** Proprietary offerings creating vendor lock-in.

### Academic Solutions
- Research literature focusing on algorithmic accuracy or theoretical proofs without providing deployable software architectures.

### Open-Source Solutions
- Fragmented individual libraries and frameworks requiring extensive integration and glue code to form a functional platform.

### Limitations
- Commercial options are expensive black boxes lacking educational transparency
- Academic prototypes ignore system engineering, failure modes, and production observability
- No existing open-source repository combines complete system architecture, real-time data pipelines, and a bounded AI module into a single production specification

---

## Proposed Solution

Build a complete end-to-end platform consisting of:

1. **Data Ingestion & Transport Layer** — High-performance message queue/bus ingesting telemetry and command payloads with schema validation.
2. **Core Processing Engine** — Multi-threaded microservice architecture handling domain logic, transactional state updates, and rule evaluation.
3. **Data Storage & Indexing** — Hybrid database architecture utilizing relational storage for ACID metadata, time-series stores for telemetry, and caches for low-latency lookups.
4. **Bounded AI Subsystem** — Integrated ML inference service ({ai_tech}) providing predictive scores to augment decision engines.
5. **Operational Control Dashboard** — Modern web application featuring live telemetry, interactive charts, and administrative workflow controls.
6. **Observability & Audit Stack** — Distributed tracing, structured logging, and metrics exporter providing complete system visibility.

---

## System Architecture

### Backend
- **Core Engine:** Written in {primary_lang} for high-concurrency performance and thread-safe memory handling
- **API Framework:** High-performance REST / gRPC services for inter-component communication
- **Message Broker:** Distributed event bus managing asynchronous tasks and telemetry streams

### Frontend
- **Admin Console:** React with TypeScript for type-safe UI state management
- **Data Visualization:** Recharts / D3.js for time-series and metric visualizer components
- **Real-Time Layer:** WebSocket connection for streaming live system events to the UI

### Mobile
- Responsive PWA / Mobile view optimized for tablet and on-the-go operational monitoring.

### Cloud
- **AWS / GCP:** Primary cloud providers
- **Orchestration:** Containerized services managed via Docker and Kubernetes
- **Storage:** S3-compatible object storage (MinIO) for model artifacts and persistent log backups

### Security
- **Authentication & Authorization:** OAuth2 + JWT tokens with granular RBAC policies
- **Transport Security:** TLS 1.3 for all external and inter-service gRPC communication
- **Audit Trail:** Immutable audit logging for all administrative actions and system decisions

### AI Components
- **Inference Engine:** Microservice hosting pre-trained ML models with sub-20ms latency
- **Feature Pipeline:** Real-time feature extraction from incoming telemetry streams
- **Drift Monitoring:** Statistical distribution tracking to detect model degradation

### Databases
- **PostgreSQL:** Primary relational store for configuration, user accounts, and state
- **Redis:** High-speed in-memory cache for session state and rate-limiting counters
- **Domain-Specific Store:** Time-series (InfluxDB) or Columnar (ClickHouse) database optimized for analytical telemetry

### Networking
- **Protocols:** gRPC for internal IPC, REST for web clients, WebSockets for live push
- **Service Mesh:** Envoy / Linkerd sidecars for mTLS and traffic management

### DevOps
- **Containerization:** Docker container builds for all microservices
- **Orchestration:** Kubernetes manifests and Helm charts
- **CI/CD:** GitHub Actions workflows for automated linting, unit testing, and image publishing

### MLOps
- **Model Registry:** MLflow for tracking experiment metrics and model versioning
- **Retraining Trigger:** Automated job retraining models when data drift exceeds thresholds

### Embedded
- Applicable hardware interfacing scripts (C/C++ or Python) where physical node telemetry is required.

### Infrastructure
- Control plane nodes, application worker pools, database replica clusters, and message broker nodes.

### Monitoring
- **Prometheus:** Metrics collection (request rates, latency histograms, error rates)
- **Grafana:** Operations dashboards displaying system KPIs and alert status

### APIs
- `POST /api/v1/ingest` — Primary data ingestion endpoint
- `GET /api/v1/status` — Health and system status query
- `POST /api/v1/control` — Administrative execution command
- `GET /api/v1/analytics` — Metrics and historical analytics query

---

## AI Components

AI functions as an **augmented intelligence module** (~15–20% of effort). The core platform operates deterministically; ML enhances accuracy.

| Component | AI Role | Technique | Justification |
|-----------|---------|-----------|---------------|
| Predictive Analysis | Score incoming events for anomalies or future trends | {ai_tech} | Provides adaptive insight where static rules are insufficient |
| Feature Extraction | Extract statistical metrics from raw telemetry streams | Sliding-window aggregation | Transforms raw inputs into structured model features |
| Model Drift Monitor | Track distribution shifts in input features | Population Stability Index (PSI) | Ensures model accuracy does not silently degrade |

**What AI does NOT do:** AI does not make irreversible administrative decisions autonomously. Critical system actions require rule verification or human approval.

---

## Research Opportunities

1. **System Throughput Benchmarking:** Evaluate processing latency and memory footprint under synthetic high-load scenarios.
2. **Adaptive Rule-ML Synergy:** Study optimal weighting mechanisms between static business rules and probabilistic ML scores.
3. **Data Compression Efficiency:** Measure bandwidth and storage reduction using domain-specific encoding vs. generic compression algorithms.

**Possible Publications:**
- IEEE / ACM conference paper on domain system engineering and high-throughput architecture.
- Technical report detailing benchmark results and failure-recovery performance.

---

## Technology Stack

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Primary Stack** | {stack_main} | Latest | Core System Implementation |
| **Containers** | Docker / Kubernetes | 24+ / 1.28+ | Deployment & Orchestration |
| **Monitoring** | Prometheus / Grafana | 2.50+ / 10.x | Telemetry Observability |
| **CI/CD** | GitHub Actions | — | Automated Build & Test |

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Distributed Systems Architecture | Essential | "Designing Data-Intensive Applications" (Kleppmann) |
| {primary_lang} Programming | Essential | Language Official Documentation & Guides |
| Database Design & Optimization | Essential | Database Internal Literature |
| Cloud Containerization | Important | Docker & Kubernetes Tutorials |

---

## Required Skills

| Skill | Level Required | Notes |
|-------|---------------|-------|
| {primary_lang} Development | Advanced | Core service implementation |
| System Architecture | Advanced | Microservice design and IPC |
| SQL & Data Modeling | Intermediate | Schema optimization |
| React / TypeScript | Intermediate | Frontend dashboard creation |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Key Technologies |
|--------|------|-----------------|------------------|
| **Member 1** | Core Backend Lead | Design and implement main processing microservices, API layers, and business logic. | {primary_lang}, REST/gRPC |
| **Member 2** | Data & Storage Eng. | Manage database schemas, caching layers, and ingestion pipelines. | PostgreSQL, Redis, Kafka |
| **Member 3** | AI & Analytics Eng. | Build feature extraction pipelines, train ML models, and set up inference endpoints. | Python, PyTorch/Scikit-learn |
| **Member 4** | Frontend & UI Developer | Build React admin console, real-time WebSocket listeners, and analytics charts. | React, TypeScript, Recharts |
| **Member 5** | DevOps & Infrastructure | Configure Docker, Kubernetes, CI/CD pipelines, and Prometheus/Grafana monitoring. | K8s, Docker, Prometheus |

---

## Development Roadmap

### Summer Preparation (8 weeks)
- [ ] Review domain literature, system requirements, and API specifications
- [ ] Complete core language ({primary_lang}) and streaming architecture training
- [ ] Setup initial project repository, linters, and Docker environment

### Fall Semester (16 weeks)
- **Weeks 1–4:** Core Ingestion & Storage Setup
- **Weeks 5–8:** Business Logic & Processing Engine Implementation
- **Weeks 9–12:** AI Model Training & Inference Endpoint Integration
- **Weeks 13–16:** Initial Dashboard & Mid-Semester Review

### Spring Semester (16 weeks)
- **Weeks 1–4:** System Integration & End-to-End Pipeline Testing
- **Weeks 5–8:** Advanced Observability, Security Audit & Drift Monitoring
- **Weeks 9–12:** Load Testing, Profiling & Latency Benchmarking
- **Weeks 13–16:** Final Documentation, Video Demo, and Project Defense

---

## Risks

### Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| High Latency under Load | Medium | High | Profile critical path using pprof; optimize queries and caching |
| Data Consistency Edge Cases | Low | High | Implement strict transactional boundaries and integration tests |

### Security & Deployment Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Unauthorized Access to APIs | Low | Critical | Enforce JWT validation and strict RBAC policies |
| Deployment Complexity | Medium | Medium | Use Helm charts for reproducible Kubernetes setups |

---

## Deliverables

### Software
- [ ] Core processing backend microservices
- [ ] Real-time data ingestion and storage pipeline
- [ ] Interactive React administration dashboard
- [ ] ML inference service and feature pipeline

### Documentation & Research
- [ ] Architecture Design Document & API Reference
- [ ] System Benchmark Report
- [ ] Final Presentation Slides & Project Poster

---

## Sponsor Analysis

### Potential Sponsors
| Entity | Category | Interest Reason |
|--------|----------|----------------|
| **{sponsor_egypt.split(',')[0]}** | Domestic Industry | Direct commercial alignment with project domain |
| **{sponsor_egypt.split(',')[1] if ',' in sponsor_egypt else 'ITIDA Egypt'}** | Local Partner | Recruitment pipeline and technical validation |
| **International Tech Vendors** | Global | Open-source adoption and cloud resource grants |

---

## Estimated Budget

| Category | Item | Cost (EGP) | Cost (USD) |
|----------|------|-----------|-----------|
| **Cloud** | AWS / GCP / Azure Managed Services (6 months) | 20,000 | ~400 |
| **Hardware** | Test devices / sensor kits / local server | {budget_egp} | ~{budget_usd} |
| **Total** | | **~{int(budget_egp.replace(',','')) + 20000} EGP** | **~{int(budget_usd.replace(',','')) + 400} USD** |

---

## Evaluation Metrics

- **Difficulty (8/10):** High architectural challenge involving multi-service concurrency and streaming performance.
- **Innovation (8/10):** Combines distributed systems engineering with a bounded, production-grade AI module.
- **Research Depth (7/10):** Strong benchmarking and latency-accuracy trade-off investigation possibilities.
- **Sponsor Potential (8/10):** Direct applicability to industry requirements in Egypt and internationally.
- **Startup Potential (8/10):** Clear B2B SaaS commercialization path.

---

## Career Value

| Career Path | Relevance | Why |
|-------------|-----------|-----|
| **Backend / Systems Engineer** | ⭐⭐⭐⭐⭐ | Deep exposure to concurrent microservices, gRPC, and database design |
| **Data / Infrastructure Engineer** | ⭐⭐⭐⭐⭐ | Hands-on stream processing, event queuing, and storage optimization |
| **DevOps / Platform Engineer** | ⭐⭐⭐⭐ | Kubernetes, CI/CD, and Prometheus/Grafana observability |
| **MLOps / Applied AI Engineer** | ⭐⭐⭐⭐ | Serving production ML models with feature monitoring |

---

## Future Extensions

1. **Multi-Region Clustering:** Extend control plane across multiple geographical cloud zones.
2. **eBPF Acceleration:** Offload kernel packet filtering for higher network throughput.
3. **Advanced Visual Analytics:** Add graph-based dependency maps to the frontend UI.

---

## References

1. Kleppmann, M. (2017). *Designing Data-Intensive Applications.* O'Reilly Media.
2. Official Documentation for {stack_main.split(',')[0]} and {stack_main.split(',')[1] if ',' in stack_main else 'Kubernetes'}.
3. IEEE / ACM Conference proceedings on Distributed Systems and Cloud Computing.
"""

for folder, data in projects_data.items():
    md = generate_markdown(folder, data)
    write_readme(folder, md)

print("Batch processing complete.")
