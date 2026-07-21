# Technology & Architecture Comparison

This document provides a comprehensive comparison matrix across the technologies, architectural patterns, and evaluation metrics for all **34 graduation projects**.

---

## 1. Programming Languages

| Language | Primary Projects | Why it's used |
|----------|------------------|---------------|
| **Go** | API Gateway (13), SD-WAN (14), Self-Healing (19), GPU Scheduler (26), DB Replication (27), SCADA IDS (28), TSDB Engine (30), Microgrid (38), SIEM (39) | Unbeatable for high-concurrency network servers, Linux primitives, time-series storage, and low-latency microservices. |
| **Python** | MLOps (06), Auto-Pentest (17), Multi-Cloud Cost (25), Robot Fleet (29), UEBA (31), 5G Slicing (32), Mfg Twin (35), Core Banking AI (37) | The undisputed standard for data engineering pipelines, scientific computing, time-series forecasting, and applied ML. |
| **Java / Scala** | Fraud Detection (02), Data Lakehouse (12), Core Banking (37) | The enterprise standard for massive streaming data processing (Apache Flink, Kafka) and banking ledgers. |
| **C / C++** | Industrial IoT (05), SCADA IDS (28), CAN Gateway (33), ECU Digital Twin (34), Mesh Network (40) | Mandatory for embedded microcontrollers (ESP32), automotive SocketCAN, real-time control loops, and custom packet parsers. |
| **TypeScript / JS**| Collab Editor (04), Digital Twin (10), P2P Energy (11), Remote Patient (20), PWA Mesh (40) | The standard for complex frontend web apps (React), 3D WebGL rendering (Three.js), and cross-platform mobile (React Native). |
| **Rust** | Log Analytics (23), TSDB Storage (30) | Used when memory safety, zero-cost abstractions, and maximum CPU throughput are critical. |

---

## 2. Infrastructure & Cloud Architecture

| Domain | Key Technologies Used Across Projects |
|--------|---------------------------------------|
| **Compute** | Kubernetes, Docker, NVIDIA MIG (GPU partitioning), Raspberry Pi, ESP32 |
| **Messaging** | Apache Kafka, RabbitMQ, MQTT (Mosquitto/EMQX), gRPC, WebSockets |
| **Storage** | MinIO/S3 (Object), Apache Iceberg (Table Format), ClickHouse (Columnar) |
| **Caching & In-Memory** | Redis (State Cache / Feature Store), InfluxDB (Time-Series) |

---

## 3. Databases

| Database Type | Primary Projects | Primary Use Case |
|---------------|------------------|------------------|
| **Relational (SQL)** | Almost all projects (PostgreSQL) | Metadata, user accounts, transactional ledgers, state definitions. |
| **Time-Series** | Lakehouse (12), TSDB Engine (30), Mfg Twin (35), Microgrid (38) | InfluxDB, TimescaleDB, Custom TSDB. High-frequency sensor/telemetry storage. |
| **Columnar Analytics**| Multi-Cloud Cost (25), UEBA (31), SIEM (39) | ClickHouse. Sub-second analytical queries over billions of log rows. |
| **Graph** | Auto-Pentest (17), Digital Twin (10) | Neo4j. Mapping complex attack paths and spatial building topologies. |
| **In-Memory / KV** | Fraud Detection (02), GPU Scheduler (26), DB Replication (27) | Redis. High-speed feature caches, vector clock state, queue locks. |

---

## 4. AI & Machine Learning Integration (Bounded 10–30%)

| AI Sub-domain | Projects | Technique / Framework |
|---------------|----------|-----------------------|
| **Time-Series Forecasting** | Multi-Cloud Cost (25), GPU Scheduler (26), 5G Slicing (32), Microgrid (38) | Prophet, ARIMA, LSTMs for predicting resource demand, traffic, or costs. |
| **Anomaly Detection** | Self-Healing (19), SCADA IDS (28), UEBA (31), CAN Gateway (33), SIEM (39) | Isolation Forest, CUSUM, Autoencoders, XGBoost alert scoring. |
| **Computer Vision / Edge**| Edge Video (09), Traffic Optimization (15), Agriculture (24) | YOLO, DeepSORT, TensorRT, CNNs for edge detection and classification. |
| **Survival & Regression** | Mfg Digital Twin (35), ECU Digital Twin (34) | Cox Proportional Hazards (RUL), Dynamic Time Warping (DTW). |
| **Reinforcement Learning**| Smart City Traffic (15) | Multi-agent Q-learning / PPO for traffic signal optimization. |

---

## 5. Security, Networking & Embedded Protocols

| Technology Domain | Projects | Key Protocols & Standards |
|-------------------|----------|---------------------------|
| **Zero-Trust & Cryptography**| Zero-Trust (03), Healthcare (08), Micropayment (36) | mTLS, WireGuard, HMAC-SHA256, AES-GCM-256, Curve25519. |
| **Industrial & Power Protocols**| SCADA IDS (28), Manufacturing Twin (35), Microgrid (38) | Modbus TCP/RTU, DNP3, IEC 60870-5-104, IEEE 2030.7. |
| **Automotive Networks** | CAN Gateway (33), ECU Digital Twin (34) | SocketCAN, CAN-FD, DBC files, ISO 14229 (UDS), ISO 21434. |
| **Telecom & Wireless Mesh** | 5G Slicing (32), Disaster Mesh (40) | 3GPP TS 28.530, ns-3, LoRa (868/915 MHz), 802.11s Wi-Fi Mesh. |
| **Banking & Payments** | Micropayment (36), Core Banking (37) | ISO 13616 (IBAN), ISO 8583 (Cards), SEPA XML, OFAC screening. |

---

## 6. Project Difficulty vs. Estimated Implementation Time

*Note: Time assumes a 5-person team working over an 8-month academic year.*

| Project | Difficulty (1-10) | Est. Implementation Time | Highest Risk Factor |
|---------|-------------------|--------------------------|---------------------|
| Multi-Region DB Replication (27) | 10 | 8 months | Vector clock concurrency & split-brain recovery |
| Multi-Tenant GPU Scheduler (26) | 9 | 8 months | NVIDIA MIG hardware partitioning & DRF logic |
| Custom Time-Series DB Engine (30) | 9 | 8 months | Crash-safe WAL recovery & Gorilla compression |
| 5G Network Slicing Platform (32) | 9 | 7 months | Translating 3GPP specs to ns-3 simulation |
| Microgrid Control System (38) | 9 | 7 months | Sub-50ms islanding control loop stability |
| In-Vehicle CAN Security Gateway (33)| 8 | 6 months | Real-time SocketCAN filtering (<1ms latency) |
| Core Banking Platform (37) | 9 | 7 months | Strict ACID double-entry ledger atomicity |
| Disaster Mesh Network (40) | 9 | 7 months | Hybrid LoRa/Wi-Fi packet collision avoidance |

---

## 7. Comprehensive Career Alignment Matrix

| Career Path | Top Recommended Projects |
|-------------|--------------------------|
| **Site Reliability Engineer (SRE)** | Self-Healing Infra (19), GPU Scheduler (26), Log Analytics (23), SIEM (39) |
| **Data Engineer / Big Data Developer** | Data Lakehouse (12), Multi-Cloud Cost (25), UEBA (31), SIEM (39) |
| **Systems / Distributed Software Engineer**| Active-Active DB (27), TSDB Engine (30), GPU Scheduler (26), API Gateway (13) |
| **Cybersecurity / SOC Engineer** | SCADA IDS (28), UEBA (31), CAN Gateway (33), SIEM (39), Zero-Trust (03) |
| **Automotive / Embedded Engineer** | CAN Gateway (33), ECU Digital Twin (34), Disaster Mesh (40), Microgrid (38) |
| **FinTech / Banking Systems Engineer** | Micropayment Settlement (36), Core Banking (37), Fraud Detection (02) |
| **Robotics & Autonomous Systems Eng.** | Warehouse Robot Fleet (29), Edge Video Analytics (09), Traffic Optimization (15) |
| **Telecom / 5G Network Engineer** | 5G Network Slicing (32), SD-WAN Controller (14), Disaster Mesh (40) |
