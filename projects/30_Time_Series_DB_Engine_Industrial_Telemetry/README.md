# Time-Series Database Engine for Industrial Telemetry

---

## Executive Summary

This project proposes the design and implementation of a **purpose-built Time-Series Database (TSDB) Engine optimized for industrial telemetry workloads** — high-frequency sensor data (temperature, pressure, vibration, current) from manufacturing equipment, energy systems, and infrastructure. The system implements a custom storage engine (based on LSM-tree concepts adapted for time-ordered data) with native compression, downsampling, and a built-in anomaly-flagging subsystem as a first-class database feature.

**Motivation:** Industrial IoT generates massive volumes of time-stamped numerical data. General-purpose databases (PostgreSQL, MySQL) are extremely inefficient for this workload — they are designed for random reads/writes, not sequential time-ordered appends followed by range scans. Specialized TSDBs (InfluxDB, TimescaleDB) exist, but their internal architectures are opaque. Building a TSDB from scratch reveals the fundamental algorithms behind time-series storage: chunk-based storage, delta-delta encoding, Gorilla compression, and write-ahead logs — all while adding an ML-powered anomaly detection layer as a native query function.

**Objectives:**
- Design a custom storage engine using chunk-based, time-partitioned files with Gorilla-style compression.
- Implement a Write-Ahead Log (WAL) for crash recovery.
- Build a query engine supporting time-range scans, aggregations (mean, max, min, stddev), and downsampling (LTTB algorithm).
- Implement a Prometheus-compatible remote_write endpoint for seamless integration with existing monitoring stacks.
- Add a native `DETECT_ANOMALIES()` query function backed by a streaming anomaly detection algorithm (CUSUM or Isolation Forest).

**Expected Impact:** A working custom TSDB demonstrating mastery of storage engine design, data compression, and query optimization — one of the most sought-after skills in the database and infrastructure engineering space.

**Target Users:** Industrial IoT operators, data engineers, and infrastructure monitoring teams who need a lightweight, self-hosted TSDB for sensor data.

---

## Problem Statement

Time-series workloads are fundamentally different from relational workloads:

1. **Write-Heavy:** Sensors write data continuously — potentially 10,000+ data points per second. General-purpose databases cannot sustain this without tuning.
2. **Temporal Ordering:** Data always arrives in time order (approximately). Storage engines can exploit this to avoid random I/O.
3. **Retention and Downsampling:** Storing raw sensor data at 1-second granularity forever is unsustainable. The system must automatically downsample old data (e.g., keep raw for 7 days, hourly averages for 1 year).
4. **Compression Opportunity:** Adjacent timestamps and values in a time series are highly correlated (temperature doesn't jump from 20°C to 200°C between seconds). This enables extremely efficient delta-delta encoding.
5. **Anomaly Detection Integration:** The most common query pattern is "show me anomalies in this sensor's last 24 hours." Implementing this as an external query is slow; it should be a native database function.

---

## Existing Solutions

### Commercial / Open-Source Solutions
- **InfluxDB:** The most popular open-source TSDB. Opaque internals; complex license.
- **TimescaleDB:** PostgreSQL extension for time-series. Good but relies entirely on Postgres internals.
- **Prometheus:** Monitoring-focused TSDB with limited retention and no SQL-like query language.
- **VictoriaMetrics:** High-performance Prometheus-compatible TSDB. Excellent but massive codebase.
- **OpenTSDB:** Hadoop-based, designed for massive scale but operationally complex.

### Limitations
- All existing solutions are mature, complex codebases — using them is a configuration exercise, not a learning experience.
- None expose their internal storage mechanics (chunking, compression, WAL design) in a clean, understandable architecture.
- Building a custom TSDB is the only way to truly understand the algorithmic trade-offs.

---

## Proposed Solution

Build **AeroTSDB**, a custom time-series database engine:

1. **Ingestion Layer:** A Prometheus `remote_write`-compatible endpoint and a custom HTTP API for writing time-series data points `{metric_name, labels, timestamp, value}`.
2. **In-Memory Buffer (Head Block):** Recent data lives in a sorted in-memory structure (like a red-black tree keyed by timestamp). Handles high-rate writes without disk I/O.
3. **Chunk Encoding & Compression:** When the head block fills (e.g., 2 hours of data), it is compressed and flushed to disk using:
   - **Timestamp compression:** Delta-of-delta encoding (Gorilla paper by Facebook).
   - **Value compression:** XOR-based floating-point compression (Gorilla).
4. **Write-Ahead Log (WAL):** All writes are first appended to a WAL file before the in-memory buffer. On crash recovery, the WAL replays uncommitted data.
5. **Query Engine:** Supports time-range scans, aggregations (max/min/mean/count/stddev over a time window), and downsampling using the LTTB (Largest-Triangle-Three-Buckets) algorithm to reduce points while preserving visual shape.
6. **Native Anomaly Detection Function:** `DETECT_ANOMALIES(metric, window, sensitivity)` — a query function that applies CUSUM (Cumulative Sum Control Chart) or Z-score scoring to return anomalous time windows without data leaving the database.

---

## System Architecture

### Storage Engine (Core)
- **Language:** Go or Rust (performance-critical; must minimize allocations).
- **Data Format:** Custom binary chunk format with chunk index files.
- **WAL Format:** Append-only binary log file.

### Query Engine
- **Language:** Go (same process as storage engine).
- **Query Protocol:** Custom binary protocol + PromQL-compatible HTTP endpoint.

### Frontend / Admin
- **Grafana Integration:** Exposes a Prometheus-compatible `/api/v1/query_range` endpoint so existing Grafana dashboards work without modification.
- **Admin UI:** Simple React dashboard for monitoring database internals (chunk count, compression ratio, write throughput).

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Native Anomaly Detection | `DETECT_ANOMALIES()` query function — returns time windows where a metric behaves abnormally | CUSUM (statistical process control) or Z-score on rolling window | ~15% |

**Total AI effort: ~15%.** Remove it → the database still stores, compresses, and queries time-series data perfectly. Anomaly detection is an additive feature, not the database's purpose.

### Databases
- This project IS the database. No external database dependency.
- **WAL files + Chunk files:** On local disk (SSDs for performance).

### Networking
- **HTTP/2:** Database API endpoint.
- **Prometheus remote_write protocol:** For ingestion from existing Prometheus setups.

### DevOps
- **Docker:** Single-container deployment of the database.
- **GitHub Actions:** CI/CD with automated benchmark runs.
- **Benchmarking:** Custom benchmark suite comparing write throughput and query latency against InfluxDB OSS.

---

## Research Opportunities

1. **Gorilla Compression Efficiency on Industrial Data:** Benchmark the compression ratio of Gorilla delta-delta encoding on real industrial sensor data (temperature, pressure, current) vs. gzip.
2. **Head Block Size vs. Query Latency Trade-off:** Study how varying the in-memory head block size affects write throughput and query latency for recent data.
3. **LTTB Downsampling Accuracy:** Measure the information loss (mean squared error vs. raw data) when using LTTB to reduce 1-second data to 1-minute granularity.
4. **CUSUM vs. Isolation Forest for Streaming Anomaly Detection:** Compare false positive rates and detection latency on realistic industrial sensor anomalies.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Languages** | Go / Rust | Storage engine, WAL, query engine |
| | Python | Benchmark scripts, anomaly detection prototype |
| | TypeScript | Admin UI |
| **Algorithms** | Gorilla Compression | Timestamp + value delta encoding |
| | LTTB | Visual downsampling algorithm |
| | CUSUM | Streaming anomaly detection |
| **Frontend** | React, Recharts | Admin monitoring dashboard |
| **Testing** | `pprof` (Go profiling) | Performance bottleneck identification |
| | Custom benchmark suite | Throughput and latency testing |
| **DevOps** | Docker, GitHub Actions | Packaging and CI/CD |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Technologies |
|--------|------|-----------------|--------------|
| **Member 1** | Storage Engine & WAL | Implement the chunk format, disk flushing logic, and crash-recovery WAL. Design the file layout. | Go/Rust, Binary I/O, File Systems |
| **Member 2** | Compression & Encoding | Implement Gorilla delta-delta encoding for timestamps and XOR compression for float values. Benchmark compression ratios. | Go/Rust, Bit Manipulation |
| **Member 3** | Query Engine | Implement time-range scan, aggregations, and the LTTB downsampling algorithm. Design the query API. | Go, Algorithms |
| **Member 4** | Anomaly Detection Module | Implement the `DETECT_ANOMALIES()` query function using CUSUM; integrate into the query engine interface. | Go/Python, Statistics |
| **Member 5** | API Layer, Prometheus Integration & Dashboard | Implement the remote_write endpoint, PromQL-compatible HTTP API, and React admin dashboard. | Go, React, Prometheus protocol |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| Cloud VMs for benchmarking (high-CPU, fast NVMe SSD) | 8,000 | ~160 |
| Domain for demo deployment (optional) | 500 | ~10 |
| **Total** | **~8,500 EGP** | **~170 USD** |

---

## Difficulty
**Score: 9/10** — Implementing a correct, crash-safe storage engine with WAL recovery and custom binary compression from first principles is one of the hardest pure software engineering challenges available to a student team.

## Innovation
**Score: 8/10** — A TSDB engine with anomaly detection as a native query function (not a separate service) is a genuinely novel architectural idea.

## Sponsor Potential
**Score: 7/10** — Industrial IoT companies, monitoring SaaS providers, and infrastructure-focused engineering firms.

## Career Value
**Database Engineer / Storage Systems Engineer:** ⭐⭐⭐⭐⭐
**Systems Software Engineer:** ⭐⭐⭐⭐⭐
**Data Engineer:** ⭐⭐⭐⭐

---

## References

1. Pelkonen, T., et al. (2015). "Gorilla: A Fast, Scalable, In-Memory Time Series Database." *VLDB.*
2. Prometheus Remote Write Protocol: https://prometheus.io/docs/specs/remote_write_spec/
3. Steinarsson, S. (2013). "Downsampling Time Series for Visual Representation." *MSc Thesis, University of Iceland.* (LTTB Algorithm)
4. Page, E.S. (1954). "Continuous Inspection Schemes." *Biometrika.* (CUSUM)
5. InfluxDB IOx Storage Engine: https://github.com/influxdata/influxdb_iox
