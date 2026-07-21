# Career Path Mapping

This document maps all **34 graduation projects** to specific software engineering, systems, and computer engineering career paths. Choosing a project aligned with your desired career will give you a significant advantage in job interviews by providing a highly relevant, production-grade portfolio piece.

---

## 1. Site Reliability Engineer (SRE) / DevOps / Platform Engineer
*Focus: Infrastructure, automation, observability, multi-tenant scheduling, and system resilience.*

**Core Projects:**
- **Project 19: Self-Healing Infrastructure Platform** (The ultimate SRE project: automated K8s remediation)
- **Project 26: Multi-Tenant GPU Scheduling Platform** (K8s operator, DRF scheduling, MIG partitioning)
- **Project 23: Distributed Log Analytics & Anomaly Detection** (Observability stack with Rust/ClickHouse)
- **Project 06: End-to-End MLOps Platform** (DevOps applied to machine learning models)
- **Project 25: Multi-Cloud Cost Intelligence Platform** (FinOps & cloud cost analytics)
- **Project 39: SIEM Correlation Engine** (High-throughput stream processing & log correlation)

**Key Skills Gained:** Kubernetes Operators, Terraform, Prometheus, Go, ClickHouse, CI/CD, Linux Cgroups/Namespaces.

---

## 2. Distributed Systems / Systems Software Engineer
*Focus: High-concurrency systems, low-level network programming, database engines, and consensus algorithms.*

**Core Projects:**
- **Project 27: Multi-Region Active-Active DB Replication Platform** (Vector clocks, WAL CDC, conflict resolution)
- **Project 30: Time-Series DB Engine for Industrial Telemetry** (Storage engine, WAL, Gorilla compression)
- **Project 26: Multi-Tenant GPU Scheduling Platform** (Bin-packing, DRF fair-share algorithm)
- **Project 13: Intelligent API Gateway** (High-concurrency Go proxy, rate limiting, WAF)
- **Project 04: Real-time Collaborative Code Editor** (CRDT algorithms, WebSockets, code sandboxing)

**Key Skills Gained:** Go, Rust, C++, Concurrency, gRPC, Protobuf, Vector Clocks, WAL Storage Engine design.

---

## 3. Data Engineer / Big Data Developer
*Focus: Moving, transforming, and querying massive streaming data efficiently.*

**Core Projects:**
- **Project 12: Real-time Data Lakehouse Platform** (Apache Iceberg, Trino, Flink, Kafka)
- **Project 02: Real-time Fraud Detection Pipeline** (Low-latency Flink streaming & Redis feature store)
- **Project 31: Insider-Threat Behavioral Monitoring (UEBA)** (Flink feature extraction, ClickHouse analytics)
- **Project 39: SIEM Correlation Engine** (Columnar log aggregation & temporal stream processing)
- **Project 25: Multi-Cloud Cost Intelligence Platform** (Batch ETL, ClickHouse OLAP querying)

**Key Skills Gained:** Apache Kafka, Apache Flink, ClickHouse, Apache Iceberg, Trino, SQL Optimization, Redis.

---

## 4. Cybersecurity / SOC / Security Software Engineer
*Focus: Offensive security, defensive architecture, protocol inspection, and behavioral security analytics.*

**Core Projects:**
- **Project 28: IDS for Industrial Control Networks (SCADA)** (Modbus/DNP3 parsing, passive anomaly detection)
- **Project 31: Insider-Threat Behavioral Monitoring (UEBA)** (User baseline analytics, SHAP explainability)
- **Project 39: SIEM Correlation Engine** (Elastic Common Schema, Flink CEP correlation rules, MITRE ATT&CK)
- **Project 33: In-Vehicle Network Gateway / CAN-Bus Security** (Automotive CAN filtering, UDS diagnostics)
- **Project 03: Zero-Trust Network Access Platform** (mTLS, WireGuard, continuous posture evaluation)
- **Project 17: Automated Penetration Testing Framework** (Neo4j graph exploit paths, automated orchestration)

**Key Skills Gained:** Network Security, Protocol Parsing (Modbus/DNP3/CAN), Syslog, mTLS, ClickHouse, Isolation Forest.

---

## 5. Automotive & Embedded Systems Engineer
*Focus: Microcontrollers, automotive CAN/LIN networks, real-time control, and cyber-physical systems.*

**Core Projects:**
- **Project 33: In-Vehicle Network Gateway with CAN-Bus Security** (SocketCAN, DBC parsing, ONNX inference)
- **Project 34: Automotive Digital Twin for ECU Testing** (Virtual CAN/LIN, HiL interface, DTW regression)
- **Project 40: Mesh Networking for Disaster Communication** (ESP32 LoRa, 802.11s Wi-Fi mesh, DTN routing)
- **Project 38: Microgrid Control System for Islanded Operation** (IEEE 2030.7, Modbus TCP, droop control)
- **Project 05: Industrial IoT Predictive Maintenance** (ESP32 sensors, FFT signal processing, InfluxDB)

**Key Skills Gained:** Embedded C/C++, SocketCAN, DBC/LDF files, ESP32, Modbus TCP, RTOS, Hardware Interfacing.

---

## 6. FinTech & Financial Systems Engineer
*Focus: Ledger accounting, payment rails, multi-currency netting, and financial compliance.*

**Core Projects:**
- **Project 36: Cross-Border Micropayment Settlement Infrastructure** (Bilateral netting engine, double-entry ledger)
- **Project 37: Core Banking Microservices Platform** (Spring Boot neobank, ISO 8583 card simulation, SEPA)
- **Project 02: Real-time Fraud Detection Pipeline** (Sub-50ms transaction fraud scoring)
- **Project 11: Peer-to-Peer Energy Trading Platform** (Smart grid financial matching engine)

**Key Skills Gained:** Double-Entry Ledger Accounting, Java Spring Boot, Go, ISO 8583, GARCH Volatility Models, ACID compliance.

---

## 7. Robotics, Autonomous Systems & Telecom Engineer
*Focus: Multi-agent coordination, 5G network slicing, computer vision, and edge AI.*

**Core Projects:**
- **Project 29: Multi-Robot Coordination Platform for Warehouse Fleets** (ROS 2, Gazebo, CBS pathfinding)
- **Project 32: 5G Network Slicing Management Platform** (3GPP standards, ns-3 simulation, SLA monitoring)
- **Project 09: Edge-Native Video Analytics Pipeline** (NVIDIA Jetson, TensorRT, RTSP streams)
- **Project 15: Smart City Traffic Optimization System** (Multi-agent Reinforcement Learning, SUMO simulation)

**Key Skills Gained:** ROS 2, Gazebo, ns-3 Simulator, Python, C++, TensorRT, 3GPP 5G Specs, Multi-Agent RL.

---

## How to Use This Guide for Team Formation

When forming a graduation project team, choose a project that allows each team member to specialize in their desired career trajectory. For example, **Project 35 (Digital Twin for Manufacturing)** is perfect for a 5-person team composed of:

1. **Embedded/IoT Lead:** Focuses on Raspberry Pi sensor nodes & FFT signal processing (Target Career: Embedded Engineer).
2. **Data Pipeline Lead:** Manages Kafka ingestion & Flink feature streaming (Target Career: Data Engineer).
3. **AI Specialist:** Trains survival analysis (RUL) models (Target Career: ML Engineer).
4. **Backend Developer:** Builds twin state engine in Go & PostgreSQL API (Target Career: Systems Engineer).
5. **Frontend Developer:** Builds Three.js 3D factory floor dashboard (Target Career: Fullstack/Graphics Engineer).
