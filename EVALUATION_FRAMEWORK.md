# 📐 Evaluation Framework for Graduation Projects

> **Document Classification:** Internal Evaluation Standard
> **Applicable To:** Final-Year Computer Engineering Graduation Projects
> **Version:** 2.0 — July 2026

---

## 1. Philosophy

A graduation project is not a homework assignment. It is the culmination of four to five years of engineering education — the moment where a student transitions from a learner to a builder. An excellent graduation project should demonstrate that the team can **identify a real problem**, **architect a non-trivial solution**, **implement it with professional-grade engineering practices**, and **deliver a working system** that could reasonably exist outside the walls of a university.

This framework rejects the common trap of evaluating projects purely on novelty or AI hype. Instead, it measures projects across 15 carefully weighted dimensions that collectively answer one question:

> *"If this team walked into a software company tomorrow, would this project prove they are ready?"*

---

## 2. The 15 Evaluation Dimensions

Each dimension is scored on a **1–5 scale** with clearly defined level descriptors.

---

### 2.1 Engineering Complexity — Weight: 10%

**Definition:** The degree of architectural sophistication, system design depth, and technical challenge embedded in the project. This measures whether the project forces the team to make non-trivial engineering decisions — choosing between trade-offs, designing communication protocols, managing state across distributed components, or handling concurrency and fault tolerance.

**Why It Matters:** A graduation project that can be built with a single Flask app and a SQLite database does not demonstrate engineering maturity. Complexity is not about making things complicated for the sake of it — it is about solving a problem that inherently demands multiple interacting subsystems, careful interface design, and thoughtful abstraction.

| Score | Level           | Description |
|-------|-----------------|-------------|
| 1     | **Trivial**     | Single-tier application with no meaningful architectural decisions. CRUD operations with a web framework. No concurrency, no real-time processing, no inter-service communication. |
| 2     | **Basic**       | Two-tier architecture (client-server) with a relational database. Some API design but no complex data flows. Limited use of design patterns. Minimal error handling strategy. |
| 3     | **Moderate**    | Multi-tier architecture with at least three distinct components (e.g., frontend, backend API, background workers). Uses message queues or event-driven patterns. Implements caching, rate limiting, or connection pooling. Handles at least one cross-cutting concern (auth, logging, monitoring) systematically. |
| 4     | **High**        | Distributed system with multiple services communicating via well-defined protocols (gRPC, WebSockets, MQTT). Implements at least two of: real-time data pipelines, event sourcing, CQRS, or saga patterns. Handles partial failure gracefully. Includes a data processing layer separate from the application layer. |
| 5     | **Exceptional** | Systems-level engineering involving custom protocols, kernel-level interactions, hardware-software co-design, compiler/interpreter construction, or distributed consensus. Requires deep understanding of networking, operating systems, or embedded systems. The architecture itself is a significant engineering contribution. |

---

### 2.2 Research Contribution — Weight: 8%

**Definition:** The extent to which the project advances existing knowledge, applies a novel method to an underexplored domain, or produces results that could be published in an academic venue. This is not about using a pre-trained model — it is about generating new insight.

**Why It Matters:** While not every graduation project needs to be a research paper, projects that push beyond known solutions demonstrate intellectual depth. A team that benchmarks three existing approaches on a new dataset and draws actionable conclusions has contributed more than a team that simply calls an API.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **None**           | Purely implementation-focused. No literature review, no comparison with existing approaches, no hypothesis testing. |
| 2     | **Minimal**        | Includes a surface-level literature review. Uses existing tools and methods without modification. No original experimentation or benchmarking. |
| 3     | **Moderate**       | Conducts a structured comparison of at least two existing approaches. Adapts an existing method to a new domain or dataset. Documents findings with quantitative metrics. |
| 4     | **Significant**    | Proposes a meaningful modification to an existing algorithm, architecture, or pipeline. Validates the modification with rigorous experimentation. Results are of sufficient quality for a workshop paper or poster presentation. |
| 5     | **Publishable**    | Introduces a novel approach, dataset, or framework. Includes ablation studies, statistical significance testing, and comparison against strong baselines. The work could be submitted to a peer-reviewed conference or journal. |

---

### 2.3 Innovation — Weight: 8%

**Definition:** The originality of the problem framing, the creativity of the proposed solution, or the uniqueness of the application domain. Innovation can come from combining existing technologies in an unprecedented way, applying a known technique to a novel context, or rethinking an established workflow.

**Why It Matters:** The world does not need another to-do app. Innovation is what separates a graduation project from a course assignment. It signals that the team can think beyond tutorials and identify gaps that others have not addressed.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Clone**          | A direct replica of an existing product or tutorial project. No original thinking in problem selection or solution design. |
| 2     | **Incremental**    | Minor improvements to an existing open-source project or well-known application. Adds a feature but does not rethink the approach. |
| 3     | **Applied**        | Takes a known technique and applies it meaningfully to a less-explored domain. The combination of technology and domain is not commonly seen in existing projects. |
| 4     | **Creative**       | Introduces a novel system design, an unconventional data pipeline, or a unique user experience that solves a real problem in a way that existing solutions do not. |
| 5     | **Pioneering**     | Addresses a problem that has not been systematically tackled before. The project defines a new category, creates a new tool where none existed, or proposes a paradigm shift in how a problem is approached. |

---

### 2.4 Software Engineering Depth — Weight: 10%

**Definition:** The rigor of software engineering practices applied throughout the project lifecycle. This includes requirements engineering, system design documentation, version control discipline, testing strategy, CI/CD pipelines, code review practices, and adherence to SOLID principles and clean architecture.

**Why It Matters:** A working demo is not a software project. Software engineering depth is what makes the difference between a prototype that breaks in production and a system that can be handed off to another team. This dimension evaluates whether the team operates like professional engineers or like students hacking together a submission.

| Score | Level             | Description |
|-------|-------------------|-------------|
| 1     | **Ad Hoc**        | No version control or single-commit repository. No documentation beyond inline comments. No testing. Monolithic codebase with no separation of concerns. |
| 2     | **Basic**         | Uses Git with feature branches. Has a README with setup instructions. Some unit tests exist but coverage is below 30%. Basic project structure but no consistent coding standards. |
| 3     | **Structured**    | Follows a consistent project structure (e.g., Clean Architecture, MVC). Maintains a living design document. Unit test coverage above 50%. Uses linting and formatting tools. Has a basic CI pipeline that runs tests on push. |
| 4     | **Professional**  | Comprehensive test suite including unit, integration, and end-to-end tests. CI/CD pipeline with automated deployment to staging. Uses dependency injection, interface segregation, and other SOLID principles. Maintains ADRs (Architecture Decision Records). Code review process is enforced. |
| 5     | **Industry-Grade**| Full observability stack (structured logging, metrics, distributed tracing). Feature flags for gradual rollouts. Database migration strategy. API versioning. Security scanning in CI pipeline. Load testing as part of the release process. The repository could pass a professional code audit. |

---

### 2.5 AI Integration — Weight: 8%

**Definition:** The meaningfulness, depth, and technical sophistication of AI/ML integration within the project. This is not about slapping a ChatGPT API call onto a CRUD app — it is about using AI as a core component that solves a problem that cannot be effectively solved with traditional programming alone.

**Why It Matters:** AI integration is increasingly expected in modern software systems, but it must be purposeful. A project that fine-tunes a model on domain-specific data, builds a custom inference pipeline, or designs an AI-powered feedback loop demonstrates far more engineering skill than one that simply calls a hosted API.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **None**           | No AI/ML component. Entirely rule-based or traditional software. |
| 2     | **Superficial**    | Uses a pre-trained model via a third-party API (e.g., OpenAI, Google Vision) without any customization, fine-tuning, or pipeline design. AI is a feature, not a core component. |
| 3     | **Integrated**     | Trains or fine-tunes at least one model on project-specific data. Implements a proper ML pipeline (data preprocessing, training, evaluation, serving). Understands and documents model performance metrics. |
| 4     | **Deep**           | Designs a multi-model architecture or uses AI for multiple interconnected tasks. Implements custom training loops, loss functions, or architectures. Handles model versioning, A/B testing, or online learning. Includes explainability or interpretability mechanisms. |
| 5     | **Advanced**       | Pushes the boundary of applied AI — involves techniques such as reinforcement learning with real-world feedback, generative model fine-tuning with RLHF, multimodal fusion, federated learning, or on-device model optimization. The AI component itself is a significant engineering and research achievement. |

---

### 2.6 Scalability — Weight: 7%

**Definition:** The system's ability to handle increasing load, data volume, and user concurrency without degradation. This includes horizontal and vertical scaling strategies, database sharding or replication, caching layers, asynchronous processing, and load balancing.

**Why It Matters:** A system that works for 10 users but crashes at 1,000 is not a scalable system. Scalability thinking forces teams to consider bottlenecks, resource constraints, and growth patterns — skills that are essential in industry.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Not Considered** | Single-server deployment with no thought given to scaling. Application state stored in memory. Database queries are unoptimized. |
| 2     | **Acknowledged**   | Team discusses scaling in documentation but does not implement any scaling mechanisms. May use an ORM without query optimization. |
| 3     | **Designed For**   | Architecture is stateless where possible. Uses connection pooling, database indexing, and basic caching (Redis/Memcached). Background jobs are offloaded to a task queue. Can demonstrate handling 10x the demo load. |
| 4     | **Implemented**    | Containerized deployment with orchestration (Kubernetes, Docker Swarm). Implements auto-scaling policies. Uses read replicas or database partitioning. CDN for static assets. Can demonstrate handling 100x the demo load with measured performance metrics. |
| 5     | **Production-Grade** | Multi-region deployment strategy. Event-driven architecture with back-pressure handling. Implements circuit breakers, bulkheads, and graceful degradation. Has a documented capacity planning model. Performance benchmarks are part of the CI pipeline. |

---

### 2.7 Industrial Value — Weight: 7%

**Definition:** The degree to which the project solves a real problem faced by businesses, organizations, or industries. A project with high industrial value addresses a pain point that existing commercial solutions either ignore, handle poorly, or price out of reach for certain market segments.

**Why It Matters:** Industrial value validates that the team can identify and solve real-world problems. It also increases the project's chances of receiving sponsorship, being adopted post-graduation, or serving as a foundation for a startup.

| Score | Level               | Description |
|-------|---------------------|-------------|
| 1     | **Academic Only**   | The project exists solely to fulfill graduation requirements. No identifiable industry user or use case. |
| 2     | **Tangential**      | The project touches an industry domain but solves a toy problem within it. No validated user need. |
| 3     | **Relevant**        | Addresses a genuine industry pain point. At least one potential user or organization has been consulted or identified. The problem is validated through interviews, surveys, or market research. |
| 4     | **High Demand**     | Solves a problem that multiple organizations actively face. Comparable commercial solutions exist but are expensive, proprietary, or inadequate. The project could save measurable time or money. |
| 5     | **Critical**        | Addresses a regulatory requirement, safety concern, or market gap with no adequate existing solution. Industry stakeholders have expressed interest. The project could be deployed in a production environment with minimal additional engineering. |

---

### 2.8 Sponsor Potential — Weight: 5%

**Definition:** The likelihood that a corporation, government agency, NGO, or research institution would fund, co-develop, or adopt the project. Sponsor potential depends on alignment with organizational priorities, the project's maturity level, and its potential return on investment for the sponsor.

**Why It Matters:** Sponsorship validates industrial relevance and provides teams with resources, mentorship, and real-world constraints. Sponsored projects tend to produce higher-quality outcomes because they have external accountability.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **None**           | No identifiable sponsor interest. The project is purely academic with no commercial or institutional appeal. |
| 2     | **Low**            | A loose connection to an industry vertical, but no specific sponsor has been identified. The project would require significant modification to appeal to a sponsor. |
| 3     | **Moderate**       | The project aligns with the stated priorities of at least one type of organization (e.g., healthcare providers, logistics companies). A pitch deck could be prepared with minimal effort. |
| 4     | **High**           | Specific organizations have been identified as potential sponsors. The project addresses a known gap in their operations. Initial conversations or letters of interest could be obtained. |
| 5     | **Guaranteed**     | A sponsor has already expressed formal interest, or the project is being developed in partnership with an external organization. Resources (data, APIs, mentorship) are provided. |

---

### 2.9 Startup Potential — Weight: 5%

**Definition:** The viability of the project as the foundation for a commercial venture. This considers market size, competitive landscape, revenue model feasibility, intellectual property potential, and the team's ability to iterate beyond the graduation scope.

**Why It Matters:** Projects with startup potential motivate teams to think about users, markets, and sustainability — not just technical features. They also provide a career path for the team beyond graduation.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **None**           | The project has no commercial potential. It solves a problem that no one would pay for, or the market is fully saturated with free alternatives. |
| 2     | **Unlikely**       | A vague commercial angle exists, but the market is small, the competition is fierce, or the revenue model is unclear. |
| 3     | **Possible**       | A viable niche market exists. A freemium or SaaS revenue model is plausible. The project differentiates itself from at least one competitor in a meaningful way. |
| 4     | **Strong**         | Clear product-market fit for an underserved segment. A defensible competitive advantage exists (proprietary data, unique algorithm, network effects). The team has outlined a go-to-market strategy. |
| 5     | **Venture-Ready**  | The project addresses a large, growing market with a clear revenue model. An MVP could be launched within 3 months of graduation. The team has validated demand through user testing, waitlists, or pilot deployments. |

---

### 2.10 Educational Value — Weight: 8%

**Definition:** The breadth and depth of technical skills, engineering practices, and professional competencies that team members will acquire or strengthen by completing the project. A project with high educational value exposes students to technologies, patterns, and challenges they have not encountered in their coursework.

**Why It Matters:** The primary purpose of a graduation project is learning. Even a brilliantly conceived project fails as a graduation project if the team does not grow from building it. Educational value ensures that the project stretches the team's capabilities while remaining achievable.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Minimal**        | The project uses only technologies and patterns already covered extensively in coursework. No new skills are required. |
| 2     | **Low**            | One or two new technologies are introduced, but the core challenge is familiar. The team could complete the project using only lecture notes and basic tutorials. |
| 3     | **Moderate**       | The project requires learning at least one new domain (e.g., real-time systems, NLP, computer vision, cloud infrastructure). Team members must read documentation, research papers, or industry best practices independently. |
| 4     | **High**           | Multiple new technical domains are covered. The project requires systems thinking, cross-domain integration, and independent problem-solving. Team members will emerge with marketable skills not taught in their curriculum. |
| 5     | **Transformative** | The project fundamentally reshapes the team's engineering capabilities. It requires mastering advanced topics such as distributed systems, compiler design, ML infrastructure, or security engineering. Completing the project is equivalent to several months of professional experience. |

---

### 2.11 Difficulty — Weight: 7%

**Definition:** The overall implementation challenge, considering algorithmic complexity, system integration challenges, domain knowledge requirements, and the gap between the team's current skills and the skills required. Difficulty is calibrated for a team of 3–5 final-year Computer Engineering students over a 6–9 month timeline.

**Why It Matters:** A project that is too easy does not demonstrate competence. A project that is too hard results in an incomplete, frustrating submission. The sweet spot is a project that is challenging enough to impress evaluators but achievable enough to deliver a working system.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Trivial**        | A competent student could complete the entire project solo in 2–4 weeks. No algorithmic complexity, no integration challenges, no domain learning curve. |
| 2     | **Easy**           | Achievable by a single student in 2–3 months. Straightforward architecture with well-documented libraries and tutorials available for every component. |
| 3     | **Moderate**       | Requires a full team working for 4–6 months. At least one component involves non-trivial algorithmic or integration work. Some trial-and-error is expected. |
| 4     | **Hard**           | Requires a full team working for 6–9 months with disciplined project management. Multiple components involve significant technical risk. The team will encounter problems not covered in any tutorial. |
| 5     | **Very Hard**      | At the upper boundary of what a student team can achieve. Requires exceptional technical skill, strong project management, and some amount of luck. Even partial completion would be impressive. |

---

### 2.12 Data Availability — Weight: 5%

**Definition:** The accessibility, quality, and sufficiency of data required to build, train, and evaluate the project. This includes public datasets, APIs, synthetic data generation capabilities, and the feasibility of collecting original data within the project timeline.

**Why It Matters:** Many ambitious projects fail not because of engineering shortcomings but because the team cannot access the data they need. Evaluating data availability upfront prevents teams from committing to projects that are doomed by data constraints.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Unavailable**    | The required data does not exist publicly, cannot be generated synthetically, and would require months or legal agreements to collect. |
| 2     | **Difficult**      | Data exists but is behind paywalls, requires institutional access, or needs extensive cleaning and labeling. Collection is possible but risky within the timeline. |
| 3     | **Accessible**     | Public datasets exist and are suitable with moderate preprocessing. APIs provide necessary data with reasonable rate limits. Some original data collection may be needed but is feasible. |
| 4     | **Abundant**       | Multiple high-quality public datasets are available. Well-documented APIs provide rich data. Benchmark datasets exist for evaluation. Synthetic data generation is straightforward if needed. |
| 5     | **Ideal**          | Large-scale, well-curated benchmark datasets are freely available. The domain has an active data-sharing community. Pre-labeled data exists. The team can focus on engineering rather than data wrangling. |

---

### 2.13 Deployment Complexity — Weight: 4%

**Definition:** The operational challenge of deploying, configuring, and running the system in a realistic environment. This includes infrastructure requirements, dependency management, environment configuration, security hardening, and monitoring setup.

**Why It Matters:** A project that only runs on the developer's laptop is not a deployed system. Deployment complexity measures whether the team has thought about operations, infrastructure, and the gap between development and production environments.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Laptop Only**    | The project runs only in a local development environment. No deployment strategy. No containerization. "It works on my machine." |
| 2     | **Manual Deploy**  | Can be deployed to a single server with manual configuration. Requires a list of manual steps. No health checks or monitoring. |
| 3     | **Containerized**  | Dockerized application with docker-compose for local development. Can be deployed to a cloud VM with documented steps. Basic health check endpoint exists. |
| 4     | **Automated**      | CI/CD pipeline deploys to a cloud environment automatically. Infrastructure is defined as code (Terraform, Pulumi). Environment variables are managed securely. Rollback strategy exists. |
| 5     | **Production-Ready** | Multi-environment deployment (dev, staging, production). Blue-green or canary deployment strategy. Automated scaling, monitoring dashboards, alerting, and incident response runbook. Secrets management with a vault. |

---

### 2.14 Maintainability — Weight: 4%

**Definition:** The ease with which the system can be understood, modified, extended, and debugged by someone who did not build it. Maintainability is a function of code quality, documentation completeness, architectural clarity, and dependency management.

**Why It Matters:** Graduation projects are often abandoned after submission. A maintainable project can be handed off to the next cohort, open-sourced, or continued by the team post-graduation. Maintainability also reflects the team's maturity as engineers — writing code that others can read is harder than writing code that works.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Unmaintainable** | No documentation. No consistent code style. No separation of concerns. Hardcoded values everywhere. No one outside the team could understand or modify the system. |
| 2     | **Fragile**        | Some documentation exists but is outdated. Code is loosely organized. Changing one component frequently breaks another. No tests to catch regressions. |
| 3     | **Adequate**       | Clear project structure with documented setup instructions. Moderate test coverage protects core functionality. Configuration is externalized. A new developer could onboard in 1–2 days. |
| 4     | **Good**           | Comprehensive documentation including API docs, architecture diagrams, and development guides. High test coverage. Modular design allows independent component updates. Dependency updates are managed. |
| 5     | **Excellent**      | The project is structured as if it were an open-source project seeking contributors. Includes CONTRIBUTING.md, issue templates, coding standards guide, and architectural overview. Any competent developer could extend the system within hours. |

---

### 2.15 Team Distribution — Weight: 4%

**Definition:** The degree to which the project's work can be divided into independent, well-scoped modules that allow team members to work in parallel without constant coordination overhead. This also considers whether each team member's contribution is substantial and assessable independently.

**Why It Matters:** Graduation projects are team efforts, and evaluators need to assess individual contributions. A project where all work is sequential or where only one person can work on the core component leads to uneven contributions, frustration, and lower overall quality.

| Score | Level              | Description |
|-------|--------------------|-------------|
| 1     | **Monolithic**     | The project is a single, tightly coupled component. Only one person can effectively work on it at a time. Work cannot be parallelized. |
| 2     | **Weakly Split**   | Two loosely defined areas of work, but significant overlap and dependency. One team member is likely to become a bottleneck. |
| 3     | **Balanced**       | Three or more distinct modules with clear interfaces. Each team member owns at least one module. Integration points are well-defined. Some coordination is needed but parallelism is possible. |
| 4     | **Well-Distributed** | Each team member owns a clearly scoped subsystem (e.g., frontend, backend API, ML pipeline, data pipeline, DevOps). Interfaces are documented via API contracts or schemas. Weekly integration is sufficient. |
| 5     | **Independently Parallel** | Each module can be developed, tested, and deployed independently. Contributions are tracked via version control. Each team member's work is independently demonstrable and assessable. Cross-module contracts are enforced by automated tests. |

---

## 3. Scoring Methodology

### 3.1 Composite Score Calculation

The composite score is a weighted average of all 15 dimensions:

```
Composite Score = Σ (Dimension Score × Dimension Weight)
```

With all weights summing to 100%:

| Dimension                | Weight |
|--------------------------|--------|
| Engineering Complexity   | 10%    |
| Research Contribution    | 8%     |
| Innovation               | 8%     |
| Software Engineering     | 10%    |
| AI Integration           | 8%     |
| Scalability              | 7%     |
| Industrial Value         | 7%     |
| Sponsor Potential        | 5%     |
| Startup Potential        | 5%     |
| Educational Value        | 8%     |
| Difficulty               | 7%     |
| Data Availability        | 5%     |
| Deployment Complexity    | 4%     |
| Maintainability          | 4%     |
| Team Distribution        | 4%     |
| **Total**                | **100%** |

### 3.2 Tier Assignment

| Tier        | Score Range | Verdict |
|-------------|-------------|---------|
| 🏆 **S-Tier** | 4.50 – 5.00 | **Exceptional.** This project exceeds graduation requirements. It demonstrates research-grade thinking, production-grade engineering, and real-world impact. Recommended for publication, competition submission, or startup incubation. |
| 🥇 **A-Tier** | 3.80 – 4.49 | **Excellent.** A strong project that demonstrates engineering maturity and creative problem-solving. Minor gaps in one or two dimensions do not detract from the overall quality. Recommended with confidence. |
| 🥈 **B-Tier** | 3.00 – 3.79 | **Solid.** A competent project that meets graduation requirements and demonstrates adequate engineering skill. Suitable for teams that prioritize learning and completion over ambition. |
| 🥉 **C-Tier** | 2.00 – 2.99 | **Acceptable.** Meets the minimum bar for graduation but does not distinguish the team. Evaluators may request additional work or a defense presentation to confirm understanding. |
| ❌ **D-Tier** | Below 2.00 | **Insufficient.** Does not meet graduation standards. Requires a major scope revision or complete restart. |

### 3.3 Scorecard Format

Every project proposal in this repository includes a scorecard in the following format:

```
| Dimension                | Score | Justification                    |
|--------------------------|-------|----------------------------------|
| Engineering Complexity   | 4/5   | Brief explanation of the rating  |
| Research Contribution    | 3/5   | ...                              |
| ...                      | ...   | ...                              |
| **Composite Score**      | **X.XX** | **Tier: [S/A/B/C/D]**        |
```

---

## 4. Calibration Notes

### What This Framework Rewards

- **Depth over breadth.** A project that does three things exceptionally well scores higher than one that does ten things superficially.
- **Engineering rigor.** Clean architecture, comprehensive testing, and proper deployment outweigh flashy demos.
- **Honest complexity.** Complexity that arises naturally from the problem is valued. Artificial complexity added to inflate scores is penalized.
- **Working software.** A deployed, functional system with documentation scores higher than an ambitious concept with a broken prototype.

### What This Framework Penalizes

- **API wrapper projects.** Calling a third-party API and displaying the results in a React app does not constitute a graduation project, regardless of how polished the UI is.
- **Tutorial-driven development.** Projects that are clearly assembled by following a YouTube series or Udemy course, with no original engineering decisions.
- **Scope without substance.** Proposals that promise ten features but deliver none completely.
- **Uneven contributions.** Projects where one team member did 80% of the work while others watched.

---

## 5. How This Framework Will Be Applied

1. **Pre-evaluation:** Each project proposal in this repository has been scored by the consulting team before being included. The scorecard is embedded in the proposal itself.
2. **Selection guidance:** Teams should select projects that align with their skills (ensuring feasibility) while stretching their capabilities (ensuring growth).
3. **Progress checkpoints:** The framework can be re-applied at milestone reviews to track whether the project is meeting its initial scoring expectations.
4. **Final defense:** Evaluators can use the same dimensions during the final project defense to ensure consistent, transparent assessment.

---

*This framework is a living document. It will be updated as industry standards evolve and as feedback from evaluators and students is incorporated.*
