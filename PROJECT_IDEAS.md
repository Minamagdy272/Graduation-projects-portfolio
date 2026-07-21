# 📋 100 Graduation Project Ideas

> **Grouped by Engineering Domain**
> **Format:** Project Name | Short Description | Main Technologies

---

## Cloud & Distributed Systems (10 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 1 | **Custom Container Orchestration Engine** | Build a lightweight container orchestrator from scratch that handles scheduling, health checks, service discovery, and rolling deployments across a cluster of nodes | Go, Linux containers (cgroups/namespaces), gRPC, etcd, React, Prometheus |
| 2 | **Multi-Cloud Cost Intelligence Platform** | A platform that aggregates billing data from AWS, Azure, and GCP, detects cost anomalies, recommends rightsizing, and forecasts future spending | Python, FastAPI, PostgreSQL, Redis, React, Terraform, Kafka |
| 3 | **Serverless Function Orchestration Engine** | Design a FaaS runtime that executes user-submitted functions in sandboxed containers with auto-scaling, event triggers, and workflow chaining | Go/Rust, Docker, NATS, PostgreSQL, React, Nginx |
| 4 | **Distributed Configuration Management System** | A centralized configuration service with version history, environment-aware overrides, real-time push updates, and encrypted secrets management | Go, etcd/Consul, gRPC, React, PostgreSQL, Vault |
| 5 | **Cloud-Native Service Mesh** | Implement a service mesh with sidecar proxies handling mTLS, traffic splitting, circuit breaking, and distributed tracing | Go, Envoy, gRPC, Prometheus, Jaeger, Kubernetes |
| 6 | **Multi-Tenant SaaS Platform Framework** | A reusable framework for building multi-tenant SaaS applications with tenant isolation, billing integration, RBAC, and white-labeling | Node.js, PostgreSQL (row-level security), Redis, React, Stripe API |
| 7 | **Distributed Rate Limiter Service** | A globally consistent rate limiting service using token bucket and sliding window algorithms with Redis cluster and local caching | Go, Redis Cluster, gRPC, Prometheus, Docker |
| 8 | **Auto-Scaling Decision Engine** | A system that monitors application metrics and makes intelligent scaling decisions using predictive models and custom policies | Python, Prometheus, Kubernetes API, TensorFlow Lite, Go, Grafana |
| 9 | **Cloud Migration Assessment Tool** | Analyzes on-premise applications and generates cloud migration plans with cost estimates, dependency maps, and compatibility reports | Python, Neo4j, FastAPI, React, Docker, Terraform |
| 10 | **Multi-Region Data Replication Service** | A replication engine that synchronizes data across geographic regions with configurable consistency levels and conflict resolution | Go, CockroachDB, Kafka, gRPC, Prometheus |

---

## Cybersecurity (8 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 11 | **Zero-Trust Network Access Platform** | A software-defined perimeter that authenticates every request, enforces micro-segmentation, and provides identity-aware access to internal services | Go, WireGuard, OAuth2/OIDC, PostgreSQL, React, Envoy |
| 12 | **Automated Vulnerability Assessment Platform** | Scans networks, web applications, and containers for known vulnerabilities, prioritizes by risk score, and generates remediation reports | Python, Nmap, OWASP ZAP, Docker, PostgreSQL, FastAPI, React |
| 13 | **Deception-Based Intrusion Detection System** | Deploys honeypots and honeytokens across a network, monitors attacker behavior, and correlates findings with real security events | Python, Docker, Elasticsearch, Kibana, Flask, Scapy |
| 14 | **Automated Penetration Testing Framework** | An orchestration platform that chains security testing tools, automates common attack vectors, and generates compliance-ready reports | Python, Go, Docker, Metasploit API, PostgreSQL, React, Celery |
| 15 | **Security Information & Event Management (SIEM)** | Collects, normalizes, and correlates security events from multiple sources with real-time alerting and forensic search capabilities | Python, Kafka, Elasticsearch, Kibana, PostgreSQL, Docker |
| 16 | **Encrypted Search Engine** | A search system that operates on encrypted data using searchable encryption schemes, enabling queries without decrypting the underlying dataset | Python, Rust, PostgreSQL, FastAPI, React, OpenSSL |
| 17 | **Network Traffic Anomaly Detector** | Captures and analyzes network packets in real time to detect DDoS attacks, port scans, data exfiltration, and protocol anomalies | Python, C++, Scapy, Kafka, InfluxDB, Grafana, TensorFlow |
| 18 | **Firmware Vulnerability Scanner** | Extracts, decompresses, and analyzes IoT device firmware images for hardcoded credentials, outdated libraries, and misconfigurations | Python, Binwalk, Ghidra API, Docker, PostgreSQL, React |

---

## IoT & Edge Computing (8 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 19 | **Industrial IoT Predictive Maintenance Platform** | Collects vibration, temperature, and pressure data from industrial sensors, processes at the edge, and predicts equipment failures before they occur | Python, C (ESP32/STM32), MQTT, Kafka, InfluxDB, TensorFlow Lite, Grafana, Docker |
| 20 | **Smart Agriculture Monitoring & Automation** | An end-to-end farm monitoring system with soil moisture, weather, and crop health sensors, edge-based irrigation control, and a cloud analytics dashboard | C++ (Arduino/ESP32), Python, MQTT, FastAPI, PostgreSQL, React, LoRaWAN |
| 21 | **Edge-Native Video Analytics Pipeline** | Processes video streams from IP cameras at the edge for object detection, counting, and anomaly alerting without streaming raw video to the cloud | Python, C++ (OpenCV), NVIDIA Jetson, MQTT, Kafka, MinIO, FastAPI, React |
| 22 | **Smart Home Energy Management System** | Monitors electricity consumption per appliance, provides usage insights, automates scheduling for cost optimization, and integrates with smart meters | Python, ESP32, MQTT, InfluxDB, FastAPI, React Native, Docker |
| 23 | **Environmental Sensor Mesh Network** | Deploys a mesh network of air quality, noise, and weather sensors across a campus or neighborhood with self-healing routing and centralized monitoring | C (nRF52/ESP32), Zigbee/BLE Mesh, Python, MQTT, TimescaleDB, Grafana, React |
| 24 | **Connected Vehicle Telemetry Platform** | Collects OBD-II data from vehicles, processes driving behavior at the edge, and provides fleet-level analytics through a cloud dashboard | Python, C (Raspberry Pi), OBD-II, MQTT, Kafka, PostgreSQL, React, Docker |
| 25 | **Wearable Health Monitor with Edge Processing** | A wrist-worn device that measures heart rate, SpO2, and activity, processes data locally for anomaly detection, and syncs with a mobile app | C (nRF52840), BLE, Python, FastAPI, PostgreSQL, React Native, TensorFlow Lite |
| 26 | **Smart Warehouse Inventory System** | Uses RFID readers, weight sensors, and cameras to track inventory in real time, detect misplacements, and trigger reorder alerts | Python, C++ (Arduino), RFID, MQTT, PostgreSQL, FastAPI, React, Docker |

---

## Data Engineering & Databases (8 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 27 | **Real-time Data Lakehouse Platform** | A unified analytics platform that combines batch and streaming data processing with a queryable lakehouse storage layer | Python, Apache Spark, Apache Flink, MinIO (S3), Apache Iceberg, Trino, Airflow, React |
| 28 | **Custom Distributed Key-Value Store** | Build a distributed key-value database from scratch with Raft consensus, consistent hashing, replication, and a client SDK | Go, Raft (custom implementation), gRPC, Prometheus, Docker |
| 29 | **Automated Data Quality & Governance Platform** | Profiles datasets automatically, infers quality rules, monitors for violations, and tracks data lineage across transformation pipelines | Python, Great Expectations, Apache Airflow, PostgreSQL, FastAPI, React, Docker |
| 30 | **Change Data Capture Pipeline System** | Captures database changes in real time using log-based CDC and replicates them to downstream systems (data warehouse, search index, cache) | Java/Python, Debezium, Kafka, PostgreSQL, Elasticsearch, Redis, Docker |
| 31 | **Time-Series Database Engine** | Design a storage engine optimized for time-series data with columnar compression, time-based partitioning, and a SQL-compatible query layer | Go/Rust, Custom storage engine, gRPC, React (query UI), Docker |
| 32 | **Data Catalog & Lineage Tracker** | A metadata management platform that crawls data sources, builds a searchable catalog, and visualizes end-to-end data lineage as a graph | Python, Neo4j, FastAPI, React, Apache Airflow, Docker, Elasticsearch |
| 33 | **Stream Processing Framework** | A lightweight stream processing engine supporting windowed aggregations, joins, and exactly-once semantics | Java/Scala, Kafka, RocksDB, gRPC, Docker, Prometheus |
| 34 | **Graph Database for Social Network Analysis** | A custom graph storage engine with Cypher-like query language, shortest path algorithms, and community detection capabilities | Go/Rust, Custom storage, gRPC, React (visualization with D3.js), Docker |

---

## DevOps & Platform Engineering (7 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 35 | **Self-Healing Infrastructure Platform** | Monitors infrastructure health, detects failures automatically, and executes predefined remediation playbooks without human intervention | Python, Prometheus, Ansible, Kubernetes, PostgreSQL, FastAPI, React, Docker |
| 36 | **Feature Flag Management System** | A centralized service for managing feature flags with percentage rollouts, user targeting, A/B testing support, and real-time flag evaluation SDKs | Go, PostgreSQL, Redis, gRPC, React, Docker, WebSocket |
| 37 | **Deployment Pipeline Orchestrator** | A CI/CD platform that builds, tests, and deploys applications with parallel stages, approval gates, rollback support, and deployment analytics | Go, Docker, PostgreSQL, Redis, React, gRPC, MinIO |
| 38 | **Infrastructure Drift Detection System** | Compares actual cloud infrastructure state against declared Infrastructure-as-Code definitions and alerts on unauthorized changes | Python, Terraform, AWS/GCP SDK, PostgreSQL, FastAPI, React, Docker |
| 39 | **Chaos Engineering Platform** | Injects controlled failures (network latency, pod kills, CPU stress) into production-like environments and measures system resilience | Go, Kubernetes API, Prometheus, Grafana, PostgreSQL, React, gRPC |
| 40 | **Developer Portal & Service Catalog** | An internal developer portal that catalogs all microservices, their APIs, ownership, dependencies, health status, and documentation | Node.js, PostgreSQL, Elasticsearch, React, Docker, OAuth2 |
| 41 | **GitOps Continuous Deployment Controller** | A Kubernetes controller that watches Git repositories for changes and automatically reconciles cluster state with declared manifests | Go, Kubernetes API, Git, PostgreSQL, Prometheus, React |

---

## MLOps & AI Infrastructure (6 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 42 | **End-to-End MLOps Platform** | A complete ML lifecycle platform covering data versioning, experiment tracking, model training, registry, serving, and monitoring for data drift | Python, MLflow, Kubeflow, Docker, PostgreSQL, FastAPI, React, MinIO |
| 43 | **Model Serving & A/B Testing Platform** | Serves multiple ML model versions simultaneously with traffic splitting, canary deployments, latency tracking, and automatic rollback | Python, FastAPI, Docker, Kubernetes, Redis, Prometheus, React |
| 44 | **Data Labeling & Annotation Pipeline** | A collaborative platform for labeling images, text, and audio with quality control, active learning suggestions, and labeler performance tracking | Python, FastAPI, PostgreSQL, React, MinIO, Docker, Redis |
| 45 | **Feature Store System** | A centralized repository for ML features with offline (batch) and online (real-time) serving, feature versioning, and lineage tracking | Python, Apache Spark, Redis, PostgreSQL, FastAPI, Kafka, Docker |
| 46 | **ML Experiment Tracking Platform** | Tracks hyperparameters, metrics, artifacts, and code versions across experiments with comparison dashboards and reproducibility guarantees | Python, FastAPI, PostgreSQL, MinIO, React, Docker, Git |
| 47 | **AutoML Pipeline Builder** | A visual workflow builder that automates feature engineering, model selection, hyperparameter tuning, and generates deployable pipelines | Python, scikit-learn, FastAPI, PostgreSQL, React (drag-and-drop), Docker, Celery |

---

## Healthcare Technology (6 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 48 | **Privacy-Preserving Healthcare Data Exchange** | Enables hospitals and clinics to share patient data for research using federated queries and differential privacy without exposing raw records | Python, FastAPI, PostgreSQL, Docker, PySyft, React, HL7 FHIR, gRPC |
| 49 | **Remote Patient Monitoring Platform** | Collects vital signs from wearable devices, processes locally for anomaly detection, and alerts healthcare providers through a clinical dashboard | Python, C (ESP32/nRF52), BLE, MQTT, FastAPI, PostgreSQL, React, Docker |
| 50 | **Clinical Decision Support System** | Assists physicians by analyzing patient history against clinical guidelines and providing evidence-based recommendations and drug interaction warnings | Python, FastAPI, PostgreSQL, Neo4j, React, HL7 FHIR, Docker |
| 51 | **Medical Image Archive (PACS) System** | A DICOM-compliant picture archiving system with image viewing, annotation, search, and role-based access for radiology departments | Python, FastAPI, PostgreSQL, MinIO, DICOM (pydicom), React, Docker |
| 52 | **Healthcare Appointment & Resource Scheduler** | An intelligent scheduling system for clinics that optimizes doctor availability, room allocation, and equipment usage while minimizing patient wait times | Python, FastAPI, PostgreSQL, Redis, React, Docker, OR-Tools |
| 53 | **Pharmacy Management & Drug Interaction Checker** | Manages pharmacy inventory, processes prescriptions, checks for drug-drug interactions, and generates regulatory compliance reports | Python, FastAPI, PostgreSQL, React, Docker, RxNorm API |

---

## FinTech (6 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 54 | **Real-time Fraud Detection Pipeline** | A streaming analytics system that scores financial transactions in real time, detects fraudulent patterns, and blocks suspicious transactions within milliseconds | Python, Java, Kafka, Apache Flink, Redis, PostgreSQL, FastAPI, React |
| 55 | **Peer-to-Peer Digital Payment System** | A mobile payment platform with wallet management, QR code payments, transaction history, and compliance with financial regulations | Node.js, PostgreSQL, Redis, React Native, Docker, Stripe/Payment API |
| 56 | **Algorithmic Trading Backtesting Platform** | A platform for designing, backtesting, and paper-trading algorithmic strategies with historical data, performance metrics, and risk analysis | Python, FastAPI, PostgreSQL, Redis, React, TimescaleDB, Docker |
| 57 | **Personal Finance Aggregation Engine** | Aggregates financial accounts (banks, investments, crypto) into a unified dashboard with budgeting, categorization, and financial health scoring | Python, FastAPI, PostgreSQL, Redis, React, Plaid API, Docker |
| 58 | **KYC/AML Compliance Automation Platform** | Automates Know Your Customer identity verification and Anti-Money Laundering transaction screening with document verification and risk scoring | Python, FastAPI, PostgreSQL, Elasticsearch, React, Tesseract OCR, Docker |
| 59 | **Micro-Lending Risk Assessment Platform** | Evaluates loan applications using alternative data sources (mobile usage, utility payments) with explainable credit scoring and portfolio management | Python, FastAPI, PostgreSQL, React, scikit-learn, Docker, Celery |

---

## Smart Infrastructure (6 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 60 | **Digital Twin for Smart Building Management** | Creates a real-time virtual replica of a building with IoT sensor data, HVAC optimization, energy monitoring, and predictive maintenance | Python, C (ESP32), MQTT, InfluxDB, FastAPI, Three.js, React, Docker |
| 61 | **Smart City Traffic Flow Optimization** | Processes traffic camera feeds and sensor data to optimize signal timing, detect congestion, and provide real-time routing recommendations | Python, OpenCV, MQTT, Kafka, PostgreSQL (PostGIS), FastAPI, React (Leaflet), Docker |
| 62 | **Intelligent Parking Management System** | Uses ultrasonic sensors and cameras to detect parking occupancy, guides drivers to available spots, and handles automated billing | Python, C (Arduino/ESP32), MQTT, PostgreSQL, FastAPI, React Native, Docker |
| 63 | **Water Distribution Monitoring System** | Monitors water pressure, flow rates, and quality across a distribution network, detects leaks, and optimizes pump scheduling | Python, C (ESP32), MQTT, InfluxDB, FastAPI, React (Leaflet), Grafana, Docker |
| 64 | **Public Transit Real-time Tracking** | Tracks buses/trams via GPS, predicts arrival times, provides passenger information displays, and generates operational analytics | Python, C (Raspberry Pi), MQTT, PostgreSQL (PostGIS), FastAPI, React, GTFS |
| 65 | **Smart Street Lighting System** | Controls street lights based on ambient light, motion detection, and time schedules with centralized monitoring and energy reporting | C (ESP32), Python, MQTT, InfluxDB, FastAPI, React, LoRaWAN |

---

## Software Engineering & Developer Tools (7 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 66 | **Real-time Collaborative Code Editor** | A browser-based code editor supporting simultaneous editing by multiple users with CRDT-based conflict resolution, syntax highlighting, and live cursors | TypeScript, Node.js, Y.js (CRDT), WebSocket, Monaco Editor, PostgreSQL, Docker |
| 67 | **Intelligent API Gateway** | A high-performance API gateway with dynamic routing, authentication, rate limiting, request transformation, caching, and real-time analytics | Go, Redis, PostgreSQL, Prometheus, React, Docker, Lua (plugins) |
| 68 | **Static Code Analysis Platform** | Parses source code into ASTs, applies configurable rule sets, detects code smells, security vulnerabilities, and generates quality reports | Python, Java, ANTLR, PostgreSQL, FastAPI, React, Docker, Git |
| 69 | **Automated API Documentation Generator** | Analyzes API source code and runtime traffic to generate and keep API documentation synchronized, with interactive testing sandbox | Python, Node.js, FastAPI, PostgreSQL, React, Docker, OpenAPI |
| 70 | **Load Testing as a Service Platform** | A distributed load testing platform that generates realistic traffic patterns, measures response times, and identifies performance bottlenecks | Go, Python, Kubernetes, InfluxDB, Grafana, React, gRPC, Docker |
| 71 | **Dependency Vulnerability Scanner** | Scans project dependencies (npm, pip, Maven) against vulnerability databases, prioritizes by severity, and suggests upgrade paths | Python, Go, PostgreSQL, FastAPI, React, Docker, NVD API |
| 72 | **Database Migration Manager** | A version-controlled database migration tool supporting multiple database engines, rollback, dry-run, and CI/CD integration | Go, PostgreSQL, MySQL, MongoDB, React (admin UI), Docker |

---

## Networking (5 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 73 | **Software-Defined WAN Controller** | A centralized controller that manages WAN routing policies, optimizes traffic across multiple links, and provides network-wide visibility | Python, Go, OpenFlow, PostgreSQL, React, Docker, Mininet |
| 74 | **Network Performance Monitoring Dashboard** | Continuously measures latency, jitter, packet loss, and bandwidth across network paths with historical trending and alerting | Go, Python, SNMP, InfluxDB, Grafana, FastAPI, React, Docker |
| 75 | **DNS Resolution & Caching System** | A custom recursive DNS resolver with intelligent caching, query logging, DNS-over-HTTPS support, and ad/malware domain blocking | Go/Rust, Redis, PostgreSQL, React (admin UI), Docker |
| 76 | **Protocol Analyzer & Packet Inspector** | Captures, decodes, and visualizes network protocols in real time with filtering, statistics, and exportable capture files | Python, C++, libpcap, Scapy, FastAPI, React, Elasticsearch, Docker |
| 77 | **Mesh Networking Protocol Implementation** | Implements a self-organizing wireless mesh network protocol with dynamic routing, node discovery, and bandwidth optimization | C/C++ (ESP32), Python, MQTT, PostgreSQL, React, Grafana |

---

## Supply Chain & Logistics (5 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 78 | **Supply Chain Visibility & Tracking Platform** | Provides end-to-end tracking of goods from manufacturer to consumer using IoT sensors, geofencing, and real-time event notifications | Python, Node.js, PostgreSQL (PostGIS), Kafka, MQTT, React, Docker |
| 79 | **Warehouse Management System** | Manages receiving, putaway, picking, packing, and shipping with barcode scanning, zone optimization, and workforce scheduling | Python, FastAPI, PostgreSQL, Redis, React, React Native (mobile scanner), Docker |
| 80 | **Last-Mile Delivery Optimization** | Optimizes delivery routes for a fleet of drivers considering time windows, vehicle capacity, traffic, and real-time order changes | Python, OR-Tools, FastAPI, PostgreSQL (PostGIS), React (Leaflet), Docker |
| 81 | **Inventory Demand Forecasting System** | Predicts product demand using historical sales, seasonality, and external signals to optimize stock levels and prevent stockouts | Python, FastAPI, PostgreSQL, React, Prophet/statsmodels, Airflow, Docker |
| 82 | **Fleet Management & Route Optimization** | Tracks vehicle locations, monitors driver behavior, plans optimal routes, and manages maintenance schedules for commercial fleets | Python, FastAPI, PostgreSQL (PostGIS), Redis, React, MQTT, Docker |

---

## Energy & Sustainability (4 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 83 | **Peer-to-Peer Energy Trading Platform** | Enables prosumers (solar panel owners) to sell excess energy directly to neighbors using smart meter integration and automated settlement | Python, Node.js, PostgreSQL, Kafka, MQTT, React, Docker, Smart Meter API |
| 84 | **Smart Grid Load Balancing System** | Forecasts electricity demand, optimizes generation dispatch, and manages demand response programs across a distribution network | Python, FastAPI, PostgreSQL, InfluxDB, React, Grafana, OR-Tools, Docker |
| 85 | **Carbon Footprint Tracking Platform** | Tracks organizational carbon emissions across Scope 1, 2, and 3, integrates with ERP/procurement systems, and generates ESG reports | Python, FastAPI, PostgreSQL, React, Airflow, Docker, Celery |
| 86 | **Renewable Energy Output Forecasting** | Predicts solar and wind energy production using weather data, satellite imagery, and historical generation patterns | Python, FastAPI, PostgreSQL, TimescaleDB, React, Grafana, scikit-learn, Docker |

---

## Digital Identity & Authentication (4 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 87 | **Decentralized Identity Verification Platform** | Implements W3C Verifiable Credentials for self-sovereign identity with issuance, verification, and selective disclosure | Go, Python, DID/VC standards, PostgreSQL, React, Docker, Hyperledger Aries |
| 88 | **Multi-Factor Authentication Service** | A standalone MFA service supporting TOTP, WebAuthn/FIDO2, push notifications, and SMS with risk-based authentication policies | Go, PostgreSQL, Redis, React, Docker, WebAuthn API |
| 89 | **Biometric Access Control System** | A physical access control system using facial recognition and fingerprint sensors with audit logging and emergency override capabilities | Python, C++ (OpenCV), ESP32, FastAPI, PostgreSQL, React, Docker |
| 90 | **Single Sign-On Federation Gateway** | Implements SAML 2.0 and OpenID Connect federation allowing users to authenticate once across multiple applications and identity providers | Go, PostgreSQL, Redis, React, Docker, SAML/OIDC libraries |

---

## Observability & Monitoring (4 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 91 | **Distributed Log Analytics & Anomaly Detection** | Aggregates logs from distributed systems, indexes them for full-text search, and detects anomalous patterns using statistical methods | Go, Python, Kafka, Elasticsearch, Kibana, PostgreSQL, Docker |
| 92 | **Application Performance Monitoring System** | Instruments applications with distributed tracing, collects performance metrics, and provides service dependency maps with latency analysis | Go, OpenTelemetry, Jaeger, Prometheus, Grafana, PostgreSQL, React, Docker |
| 93 | **Synthetic Monitoring & Uptime Platform** | Runs scheduled checks (HTTP, TCP, DNS, SSL) from multiple geographic locations and provides uptime reports, SLA tracking, and incident timelines | Go, PostgreSQL, Redis, React, Docker, Prometheus, Alertmanager |
| 94 | **Cost-Aware Observability Pipeline** | An observability data pipeline that intelligently samples, aggregates, and routes logs/metrics/traces based on cost and importance | Go, Kafka, ClickHouse, Prometheus, React, Docker, Vector |

---

## Media & Content (3 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 95 | **Adaptive Video Streaming Platform** | A complete video platform with upload, transcoding, adaptive bitrate streaming (HLS/DASH), CDN distribution, and viewer analytics | Go, Python, FFmpeg, MinIO, Redis, PostgreSQL, React, HLS.js, Docker |
| 96 | **Content Moderation Pipeline** | Processes user-generated content (text, images, video) through automated moderation rules with human-in-the-loop review queues | Python, FastAPI, PostgreSQL, Redis, Kafka, React, Docker, Celery |
| 97 | **Real-time Collaborative Whiteboard** | A digital whiteboard supporting simultaneous drawing, sticky notes, shapes, and embedded media with real-time synchronization | TypeScript, Node.js, WebSocket, Canvas API, PostgreSQL, React, Docker |

---

## Cross-Domain (3 Projects)

| # | Project Name | Description | Main Technologies |
|---|-------------|-------------|-------------------|
| 98 | **Multiplayer Game Server Infrastructure** | A scalable backend for real-time multiplayer games with authoritative game state, matchmaking, leaderboards, and anti-cheat detection | Go, UDP/WebSocket, Redis, PostgreSQL, Docker, Prometheus, React (admin) |
| 99 | **Online Examination & Proctoring Platform** | A secure examination system with randomized question pools, browser lockdown, webcam proctoring, and automated grading with plagiarism detection | Python, FastAPI, PostgreSQL, Redis, React, WebRTC, Docker, Celery |
| 100 | **Disaster Response Coordination Platform** | Coordinates emergency response with real-time mapping, resource allocation, volunteer management, and multi-agency communication | Python, FastAPI, PostgreSQL (PostGIS), Redis, React (Leaflet), WebSocket, Docker |

---

## Domain Distribution Summary

| Domain | Count | Project Numbers |
|--------|-------|----------------|
| Cloud & Distributed Systems | 10 | 1–10 |
| Cybersecurity | 8 | 11–18 |
| IoT & Edge Computing | 8 | 19–26 |
| Data Engineering & Databases | 8 | 27–34 |
| DevOps & Platform Engineering | 7 | 35–41 |
| MLOps & AI Infrastructure | 6 | 42–47 |
| Healthcare Technology | 6 | 48–53 |
| FinTech | 6 | 54–59 |
| Smart Infrastructure | 6 | 60–65 |
| Developer Tools | 7 | 66–72 |
| Networking | 5 | 73–77 |
| Supply Chain & Logistics | 5 | 78–82 |
| Energy & Sustainability | 4 | 83–86 |
| Digital Identity | 4 | 87–90 |
| Observability & Monitoring | 4 | 91–94 |
| Media & Content | 3 | 95–97 |
| Cross-Domain | 3 | 98–100 |
| **Total** | **100** | |

---

*All 100 projects will be evaluated using the scoring rubric defined in EVALUATION.md. The top 25 will receive complete proposals.*
