# Scaling Plan

- Django: stateless; auto-scale on CPU > 60% or 95th percentile request latency > 300ms.
- Celery Workers: scale based on queue length (scale out when queued tasks > 50).
- GPU Model Fleet: autoscale by model_request_queue_length per GPU or GPUUtilization > 70%. Use spot instances for additional cheap capacity.
- DB: RDS primary with read replicas for analytics and reporting.
- Redis: ElastiCache cluster when load increases.
- Cost optimization: scale GPU pool to zero when idle; keep small warm pool for low latency.
