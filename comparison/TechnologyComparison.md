# Technology & Architecture Comparison

This document provides a matrix comparing the technologies, architectural patterns, and evaluation metrics across the 25 graduation projects.

---

## 1. Programming Languages

| Language | Primary Projects | Why it's used |
|----------|------------------|---------------|
| **Go** | Custom DB (16), Container Engine (01), Serverless Engine (07), API Gateway (13), SD-WAN (14) | Unbeatable for high-concurrency network servers, interacting with Linux primitives, and compiling to static binaries. |
| **Python** | MLOps (06), Auto-Pentest (17), Multi-Cloud Cost (25), Log Analytics (23), Smart City (15) | The undisputed king of Data Science, Machine Learning, and integrating with disparate APIs/Subprocesses. |
| **Java/Scala**| Data Lakehouse (12), Fraud Detection (02) | The standard for massive distributed data processing frameworks (Flink, Kafka, Trino). |
| **C/C++** | Industrial IoT (05), Smart Agriculture (24), Chaos Engine (22) | Mandatory for embedded microcontrollers, hardware interfacing, and extreme kernel-level optimizations. |
| **TypeScript**| Collab Editor (04), Digital Twin (10), P2P Energy (11), Remote Patient (20) | The standard for robust frontend web development (React) and cross-platform mobile (React Native). |
| **Rust** | Custom DB (16), Log Shipper (23) | Used when memory safety and zero-overhead performance are critical. |

---

## 2. Infrastructure & Cloud Architecture

| Domain | Key Technologies Used Across Projects |
|--------|---------------------------------------|
| **Compute** | Kubernetes, Docker, Firecracker microVMs, AWS Fargate |
| **Messaging** | Apache Kafka, RabbitMQ, MQTT (Mosquitto/EMQX), NATS, Redis Pub/Sub |
| **Storage** | MinIO/S3 (Object), Apache Iceberg (Table Format), HDFS |
| **Caching** | Redis, Nginx (Edge Cache) |

---

## 3. Databases

| Database Type | Projects | Use Case |
|---------------|----------|----------|
| **Relational (SQL)** | Almost all | PostgreSQL is the default for metadata, user accounts, and structured state. |
| **Time-Series** | Lakehouse (12), IoT (05, 10, 24), Telehealth (20) | InfluxDB, TimescaleDB, ClickHouse. Optimized for appending high-frequency timestamped data. |
| **Graph** | Auto-Pentest (17), Digital Twin (10) | Neo4j. Used for mapping complex relationships (attack paths, spatial graphs). |
| **NoSQL / KV**| Distributed DB (16), Serverless (07) | Redis for distributed state, Cassandra for wide-column scalability. |

---

## 4. AI & Machine Learning Integration

| AI Sub-domain | Projects | Applications |
|---------------|----------|--------------|
| **Time-Series Forecasting** | Multi-Cloud Cost (25), Energy Trading (11), Digital Twin (10) | Prophet, ARIMA, LSTMs for predicting future costs, energy use, or server loads. |
| **Anomaly Detection** | Self-Healing (19), Fraud Detection (02), Log Analytics (23), API Gateway (13) | Isolation Forests, Autoencoders to find needles in haystacks. |
| **Computer Vision** | Edge Video (09), Smart City (15), Agriculture (24) | YOLO, DeepSORT, CNNs for object detection, tracking, and disease classification at the edge. |
| **Federated Learning** | Healthcare Data Exchange (08) | PySyft, Flower for training models without moving sensitive data. |
| **Reinforcement Learning** | Smart City Traffic (15) | Training an agent to optimize complex grid timings via trial and error. |

---

## 5. Security & Networking

| Technology | Projects | Purpose |
|------------|----------|---------|
| **Zero-Trust & mTLS**| Zero-Trust (03), Healthcare (08) | Mutual TLS to cryptographically verify both client and server identities. |
| **Web3 / Cryptography**| Decentralized Identity (18), P2P Energy (11) | ZK-SNARKs, Smart Contracts, W3C Verifiable Credentials. |
| **Linux Networking** | SD-WAN (14), Chaos Engine (22) | `tc`, `iproute2`, `iptables`, eBPF for deep packet manipulation. |
| **Protocols** | API Gateway (13), Video Streaming (21) | gRPC, HTTP/2, HLS, WebRTC, WebSockets. |

---

## 6. Project Difficulty vs. Implementation Time

*Note: Time assumes a 5-person team working over an 8-month academic year.*

| Project | Difficulty (1-10) | Est. Implementation Time | Highest Risk Factor |
|---------|-------------------|--------------------------|---------------------|
| Custom Distributed KV Store | 10 | 8 months | Distributed consensus bugs (Raft) |
| Container Engine | 9 | 7 months | Linux kernel namespace complexity |
| Real-time Data Lakehouse | 9 | 8 months | Integrating Kafka/Flink/Trino securely |
| Zero-Trust Network | 8 | 6 months | High-performance proxy latency |
| Remote Patient Monitoring | 7 | 5 months | Mobile-to-Hardware BLE reliability |
| Smart Agriculture | 7 | 5 months | Hardware surviving in the physical field |

---

## 7. Career Value Mapping

| If you want to be a... | Choose these projects |
|------------------------|-----------------------|
| **Site Reliability Engineer (SRE)** | Self-Healing Infra (19), Chaos Engine (22), Distributed Log Analytics (23) |
| **Data Engineer** | Data Lakehouse (12), Multi-Cloud Cost (25), MLOps (06) |
| **Systems / Backend Engineer (Go/Rust)** | Distributed DB (16), Serverless Engine (07), API Gateway (13), Container Engine (01) |
| **Cybersecurity Engineer** | Auto-Pentest (17), Zero-Trust (03), Decentralized Identity (18) |
| **IoT / Edge Engineer** | Industrial IoT (05), Smart Agriculture (24), Edge Video Analytics (09) |
| **Frontend / Graphics Engineer** | Collab Editor (04), Digital Twin (10) |
| **AI / Machine Learning Engineer** | Smart City Traffic (15), Healthcare Exchange (08), MLOps (06) |
