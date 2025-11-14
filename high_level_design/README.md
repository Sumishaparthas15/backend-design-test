# backend-design-test


# High-Level Design Test
<!-- how requests flow through the system, how scaling works, how performance is optimized, and how monitoring and costs are tracked. -->


# Key Features

System Flow – Step-by-step explanation of how translation requests move from user → API → worker → database/cache → back to user.

Scaling Plan – Strategies for horizontal (more servers/workers) and vertical scaling (stronger CPUs/GPUs) to handle high traffic.

Performance Plan – Techniques like batching, chunking, GPU pooling, caching, and async processing to speed up translations.

Monitoring & Costs – Tracks system health using Prometheus/Grafana, logs key metrics, triggers alerts, and estimates operational costs for different workloads.


## ⚙️ Setup

###  Clone Repository
```bash
https://github.com/Sumishaparthas15/backend-design-test.git
cd high_level_design
