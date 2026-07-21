# Multi-Tenant GPU Scheduling Platform

---

## Executive Summary

This project proposes the design and implementation of a **Multi-Tenant GPU Scheduling Platform** — a cloud-native infrastructure system that allows multiple teams or users to share a pool of GPU resources fairly and efficiently. The platform manages job queuing, resource isolation, priority scheduling, and billing, while a predictive demand-forecasting module anticipates workload surges and pre-provisions capacity before queues back up.

**Motivation:** GPUs are expensive. A single NVIDIA A100 GPU costs over $10,000 to buy or $3/hour to rent on AWS. In universities, research labs, and AI startups, GPU clusters are shared among dozens of teams — but without proper scheduling infrastructure, idle GPUs sit unused while urgent jobs queue for hours, causing massive inefficiency and team frustration. Building a proper multi-tenant scheduling system teaches the deepest aspects of operating systems, resource management, distributed queues, and fair-share scheduling algorithms.

**Objectives:**
- Design a job submission API that accepts training/inference workloads with resource declarations (GPU count, VRAM, runtime limit).
- Implement a priority-aware, fair-share scheduling algorithm (e.g., Dominant Resource Fairness — DRF) that allocates GPUs across competing teams without starvation.
- Enforce tenant isolation using Linux cgroups, NVIDIA MIG (Multi-Instance GPU), or Kubernetes resource quotas.
- Build a predictive demand-forecasting module that analyzes historical job submission patterns and pre-scales node capacity.
- Provide a web dashboard for cluster administrators and individual users to monitor queue depth, GPU utilization, and billing.

**Expected Impact:** A production-grade GPU resource management platform demonstrating mastery of distributed scheduling, resource isolation, and capacity planning — directly applicable to cloud providers, research clusters, and AI infrastructure teams.

**Target Users:** University research labs, AI startups, enterprise ML teams, and cloud providers offering managed GPU compute.

---

## Problem Statement

Shared GPU clusters without proper scheduling suffer from critical failures:

1. **Starvation:** A high-priority team submits a large job and monopolizes all GPUs for 12 hours, blocking dozens of smaller jobs.
2. **Fragmentation:** GPU memory is not fully utilized because jobs are scheduled to whole GPUs even when they only need 10% of VRAM.
3. **No Isolation:** A runaway job (memory leak, infinite loop) degrades the performance of neighboring jobs on the same node.
4. **Reactive Scaling:** Cluster operators only add nodes after queues are already 3 hours deep.
5. **Opacity:** Users have no visibility into why their job is queued or how long until it runs.

---

## Existing Solutions

### Commercial Solutions
- **NVIDIA Base Command Platform:** Enterprise GPU cluster management. Very expensive, proprietary.
- **AWS SageMaker Training Jobs:** Managed but completely black-box and vendor-locked.
- **Coreweave / Lambda Labs:** Cloud GPU providers with proprietary scheduling.

### Open-Source Solutions
- **Kubernetes + NVIDIA Device Plugin:** Schedules GPUs as K8s resources. Lacks fair-share scheduling and GPU-specific features like MIG.
- **Slurm:** HPC job scheduler, mature but designed for static batch workloads, not dynamic cloud environments.
- **Apache Hadoop YARN:** Generic resource scheduler, not GPU-aware.
- **Volcano:** Kubernetes batch scheduling system for ML workloads (closest open-source analogue).

### Limitations of Existing Solutions
- Slurm lacks Kubernetes integration and modern cloud elasticity.
- Kubernetes + device plugin lacks sophisticated fair-share policies and GPU sub-allocation (MIG).
- No open-source solution combines fair-share scheduling, MIG partitioning, real-time monitoring, and predictive autoscaling in a single cohesive platform.

---

## Proposed Solution

Build **AeroGPU**, a complete multi-tenant GPU scheduling platform:

1. **Job API Service:** A REST/gRPC API where users submit jobs (container image, GPU request, priority class, time limit). Validates resource declarations and enqueues jobs.
2. **Scheduler Engine:** A Go service implementing Dominant Resource Fairness (DRF) or Weighted Fair Queuing across tenant quotas. Makes bin-packing decisions to minimize GPU fragmentation.
3. **Isolation Layer:** Integrates with NVIDIA MIG (Multi-Instance GPU) to partition a single A100 into 7 isolated instances, or uses Kubernetes resource quotas and cgroups for process-level isolation.
4. **Node Manager Agent:** A daemon running on each GPU node, reporting real-time GPU utilization (via NVIDIA SMI), memory usage, and running job states back to the scheduler.
5. **Demand Forecasting Module:** A time-series model (Prophet or ARIMA) trained on historical job submission patterns. Outputs a "next 4-hour demand forecast," which the autoscaler uses to pre-provision cloud GPU nodes before the queue backs up.
6. **Admin & User Dashboard:** A React web application showing cluster-wide GPU utilization heatmaps, per-tenant quota usage, live queue, and individual job logs.

---

## System Architecture

### Backend
- **Language:** Go for the Scheduler Engine and Node Manager Agent (performance-critical, goroutine concurrency).
- **Job API:** FastAPI (Python) for job submission and status queries.
- **Scheduler Algorithm:** DRF (Dominant Resource Fairness) with priority classes (critical, high, normal, batch).

### Frontend
- **Dashboard:** React with TypeScript.
- **Visualization:** Recharts for utilization time-series, D3.js heatmap for per-node GPU usage.

### Cloud
- **Orchestration:** Kubernetes (GKE or self-managed) as the underlying compute layer.
- **Auto-scaling:** Kubernetes Cluster Autoscaler + custom controller that pre-scales based on forecasted demand.
- **Node Types:** GPU nodes (NVIDIA T4 or A100 for MIG testing), CPU nodes for the control plane.

### Security
- **Multi-tenancy Isolation:** Kubernetes Namespaces + RBAC per tenant; NVIDIA MIG for hardware-level GPU partitioning.
- **Network Policies:** Kubernetes NetworkPolicy preventing tenant-to-tenant traffic.
- **API Authentication:** OAuth2 + JWT tokens with tenant-scoped permissions.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Demand Forecasting | Predict next 4-hour job submission volume per tenant | Prophet / ARIMA time-series model | ~15% |
| Scheduling Hint (Optional) | Suggest optimal node placement based on job history | Simple rule-based regression, not deep learning | ~5% |

**Total AI effort: ~15–20% of project.** Remove forecasting → scheduler still works perfectly via reactive autoscaling.

### Databases
- **PostgreSQL:** Job metadata, tenant configurations, quota definitions, billing records.
- **Redis:** Live job queue state, scheduler lock, real-time GPU metrics (fast read/write for the scheduler hot path).
- **InfluxDB:** Time-series storage for GPU utilization metrics and historical job patterns (feeds the forecasting model).

### Networking
- **gRPC:** Node Manager Agent → Scheduler (low-latency telemetry streaming).
- **REST:** User-facing Job API, dashboard API.
- **Kubernetes CNI:** Calico or Cilium for network policy enforcement between tenant pods.

### DevOps
- **Docker:** All services containerized.
- **Helm Charts:** Kubernetes deployment packaging for the entire platform.
- **GitHub Actions:** CI/CD — build, test, lint, push images, deploy to staging cluster.
- **Terraform:** Provision the Kubernetes cluster and GPU node pools.

### MLOps
- **Model Retraining:** The forecasting model is retrained weekly on the latest 90 days of submission history using a scheduled Kubernetes CronJob.
- **Model Versioning:** MLflow tracks model versions and metrics.

### Infrastructure
- Kubernetes control plane (3 nodes), GPU worker nodes (1–3 for testing), PostgreSQL (primary + replica), Redis cluster, InfluxDB.

### Monitoring
- **Prometheus:** Scrapes NVIDIA SMI metrics (via `dcgm-exporter`), queue depth, scheduler latency.
- **Grafana:** Cluster-wide GPU utilization dashboards, per-tenant usage, autoscaler activity.
- **Alerting:** Alert when GPU utilization drops below 40% (under-provisioned cluster) or queue wait time exceeds 30 minutes.

### APIs
- `POST /api/v1/jobs` — Submit a job
- `GET /api/v1/jobs/{id}` — Get job status and logs
- `GET /api/v1/queues` — View current queue state and estimated wait time
- `GET /api/v1/tenants/{id}/quota` — View tenant quota usage
- `GET /api/v1/forecast` — Get the 4-hour demand forecast
- `POST /api/v1/admin/nodes` — Add/remove GPU nodes

---

## AI Components

| Component | Technique | Training Data | Inference Latency | Justification |
|-----------|-----------|---------------|-------------------|---------------|
| Job Submission Demand Forecasting | Prophet (additive seasonality model) | Historical job submission timestamps + GPU hours requested | Batch (runs hourly) | Predicts cluster load 4 hours ahead, allowing proactive node provisioning. This is bounded, transparent, and interpretable — not a black box. |

---

## Research Opportunities

1. **Fair-Share Scheduling in Heterogeneous GPU Clusters:** Research the performance of DRF vs. Weighted Fair Queuing vs. Max-Min Fairness when job resource profiles vary widely (1 GPU vs. 64 GPUs).
2. **GPU Fragmentation under MIG Partitioning:** Empirically measure how NVIDIA MIG affects utilization efficiency compared to whole-GPU allocation.
3. **Demand Forecasting Accuracy vs. Pre-provisioning Cost:** Quantify the tradeoff between forecasting errors (over-provisioning costs money; under-provisioning causes queuing delays) across different forecast horizons.
4. **Preemption Policies:** Study the performance impact of job preemption strategies (checkpoint-and-resume vs. kill-and-requeue) on cluster-wide throughput.

---

## Technology Stack

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Languages** | Go | 1.22+ | Scheduler engine, node agent |
| | Python | 3.11+ | Job API (FastAPI), forecasting model |
| | TypeScript | 5.x | Dashboard frontend |
| **Frameworks** | FastAPI | 0.110+ | Job submission REST API |
| | React | 18.x | Admin and user dashboard |
| **Scheduling** | Custom DRF | — | Fair-share GPU scheduling |
| **GPU** | NVIDIA MIG | — | GPU partitioning and isolation |
| | DCGM Exporter | — | GPU metrics collection |
| **Databases** | PostgreSQL | 16+ | Job and tenant metadata |
| | Redis | 7+ | Queue state and real-time metrics |
| | InfluxDB | 2.x | Time-series telemetry |
| **AI** | Prophet | 1.1+ | Demand forecasting |
| | MLflow | 2.x | Model tracking |
| **Cloud** | Kubernetes | 1.28+ | Compute orchestration |
| | Terraform | 1.7+ | Infrastructure as Code |
| | Helm | 3.x | K8s deployment packaging |
| **Monitoring** | Prometheus | 2.50+ | Metrics collection |
| | Grafana | 10.x | Dashboards |
| **CI/CD** | GitHub Actions | — | Build and deploy pipeline |

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Operating Systems — CPU/GPU Scheduling Algorithms | Essential | OS textbooks (Tanenbaum), NVIDIA MIG documentation |
| NVIDIA GPU Architecture (CUDA, MIG) | Essential | NVIDIA Developer documentation |
| Kubernetes Operator Pattern and Custom Controllers | Essential | "Programming Kubernetes" (O'Reilly) |
| Go Concurrency (goroutines, channels) | Essential | "The Go Programming Language" |
| Fair-Share Scheduling (DRF algorithm) | Essential | DRF paper (Ghodsi et al., NSDI 2011) |
| Time-Series Forecasting (Prophet) | Important | Meta Prophet documentation |
| gRPC Protocol Buffers | Important | gRPC official documentation |
| PostgreSQL + Redis Data Modeling | Important | PostgreSQL docs, Redis University |

---

## Required Skills

| Skill | Level | Notes |
|-------|-------|-------|
| Go Programming | Advanced | Scheduler engine is performance-critical |
| Kubernetes API (client-go) | Advanced | Custom controller development |
| Linux Systems (cgroups, processes) | Intermediate | Understanding isolation mechanisms |
| GPU Programming Concepts | Intermediate | Understanding CUDA, MIG, VRAM limits |
| Python / FastAPI | Intermediate | Job API service |
| Time-Series ML (Prophet) | Beginner–Intermediate | Forecasting module only |
| React / TypeScript | Intermediate | Dashboard development |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Technologies |
|--------|------|-----------------|--------------|
| **Member 1** | Scheduler Engine Lead | Implement the DRF scheduler in Go. Manage job queues, priority classes, and bin-packing decisions. | Go, Redis, Scheduling Algorithms |
| **Member 2** | GPU Infrastructure Engineer | Configure NVIDIA MIG partitioning, build the Node Manager Agent, integrate DCGM exporter for GPU telemetry. | Go, NVIDIA MIG, Kubernetes |
| **Member 3** | Platform & API Engineer | Build the Job submission API, tenant management system, quota enforcement, and billing tracking. | Python, FastAPI, PostgreSQL |
| **Member 4** | AI & Forecasting Engineer | Train and deploy the demand forecasting model. Build the autoscaler controller that acts on forecasts. | Python, Prophet, MLflow, K8s |
| **Member 5** | Frontend & Monitoring Engineer | Build the React dashboard, integrate Prometheus/Grafana, implement real-time queue and utilization views. | React, TypeScript, Prometheus, Grafana |

---

## Development Roadmap

### Summer Preparation (8 weeks)
- Study DRF scheduling algorithm paper deeply
- Complete NVIDIA CUDA/MIG fundamentals
- Master Kubernetes Operator pattern with `client-go`
- Set up a development Kubernetes cluster (Minikube or K3s)

### Fall Semester (16 weeks)
- **Weeks 1–4:** Implement basic job submission API + PostgreSQL schema + Redis queue
- **Weeks 5–8:** Build the core scheduler engine with DRF algorithm; implement Node Manager Agent
- **Weeks 9–12:** Integrate NVIDIA MIG partitioning; implement cgroup isolation; build job log streaming
- **Weeks 13–16:** Dashboard v1 (queue view, GPU utilization); mid-semester demo

### Spring Semester (16 weeks)
- **Weeks 1–4:** Train demand forecasting model; implement autoscaler controller
- **Weeks 5–8:** Billing system; per-tenant quota reporting; job preemption
- **Weeks 9–12:** Performance benchmarking (scheduling latency, GPU utilization rates); load testing
- **Weeks 13–16:** Final polish, documentation, defense preparation

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| No access to physical NVIDIA MIG-capable GPUs | High | High | Use Google Cloud T4/A100 instances with GCP credits; simulate MIG with software mocking |
| DRF implementation bugs causing starvation | Medium | High | Implement extensive unit tests with synthetic workloads; start with simpler FIFO, then layer DRF |
| Kubernetes operator complexity | Medium | Medium | Start with basic Reconcile loops; use `controller-runtime` framework |
| Forecasting model accuracy insufficient to justify pre-scaling | Medium | Low | Forecasting is bounded — system falls back to reactive scaling without it |

---

## Deliverables

- Scheduler Engine (Go binary + Kubernetes Operator)
- Node Manager Agent (Go daemon)
- Job Submission API (Python/FastAPI)
- React Admin Dashboard
- Demand Forecasting Service + retrain pipeline
- Helm Chart for full platform deployment
- Benchmarking report (scheduling fairness, GPU utilization rates)
- Architecture Design Document

---

## Sponsor Analysis

| Sponsor | Reason |
|---------|--------|
| **NVIDIA** | Direct alignment with GPU infrastructure; actively sponsors academic research |
| **Google Cloud / AWS** | Research into GPU scheduling efficiency improves their managed products |
| **Inception AI (Egypt)** | Egyptian AI startup with GPU infrastructure needs |
| **Cairo University AI Lab** | Primary end-user — researchers competing for GPU time |
| **Smart Village companies** | Egyptian tech companies running ML training workloads |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| GCP / AWS GPU compute (T4 instances, 4 months) | 20,000 | ~400 |
| Kubernetes cluster (control plane nodes) | 5,000 | ~100 |
| Domain + TLS cert | 500 | ~10 |
| **Total** | **~25,500 EGP** | **~510 USD** |

---

## Difficulty
**Score: 9/10** — Implementing a correct, starvation-free fair-share scheduler while managing GPU hardware-level isolation is one of the hardest infrastructure engineering challenges a student team can attempt.

## Innovation
**Score: 9/10** — No open-source project combines DRF scheduling, NVIDIA MIG partitioning, and predictive pre-scaling in a single cohesive, production-grade platform.

## Research Depth
**Score: 8/10** — Strong publication opportunity benchmarking DRF variants on heterogeneous GPU workloads.

## Sponsor Potential
**Score: 9/10** — Every university lab and AI startup with GPU needs will sponsor this.

## Startup Potential
**Score: 8/10** — GPU-as-a-Service is a massive market. A multi-tenant scheduler targeting African/MENA universities and AI companies has a clear niche.

---

## Career Value

| Career Path | Relevance |
|-------------|-----------|
| Cloud Platform / Infrastructure Engineer | ⭐⭐⭐⭐⭐ |
| Systems Software Engineer (Go) | ⭐⭐⭐⭐⭐ |
| ML Infrastructure / MLOps Engineer | ⭐⭐⭐⭐⭐ |
| Site Reliability Engineer | ⭐⭐⭐⭐ |

---

## Future Extensions

1. **Spot/Preemptible Instance Support:** Auto-checkpoint and migrate jobs when spot instances are reclaimed.
2. **Multi-Cloud GPU Arbitrage:** Route jobs to the cheapest available GPU cloud (AWS vs. GCP vs. Lambda Labs) based on real-time pricing.
3. **Gang Scheduling:** Schedule all N nodes of a distributed training job simultaneously or not at all (avoiding deadlock).
4. **Federated Scheduling:** Allow multiple university clusters to share spare capacity.

---

## References

1. Ghodsi, A., et al. (2011). "Dominant Resource Fairness: Fair Allocation of Multiple Resource Types." *NSDI 2011.*
2. NVIDIA MIG User Guide: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/
3. Kubernetes Scheduling Framework: https://kubernetes.io/docs/concepts/scheduling-eviction/
4. Volcano Scheduler (open source): https://volcano.sh/
5. Taylor, S.J., & Letham, B. (2018). "Forecasting at Scale." *The American Statistician.*
