# backend-design-test


# Low-Level Design Test
# 🌐 Translation API (Django + Celery + Redis)

This project provides a RESTful backend for handling translation jobs asynchronously using **Django REST Framework**, **Celery**, and **Redis**.  
It supports **JWT authentication**, **rate limiting**, and **request validation**.

---

## 🚀 Features

- Submit translation jobs asynchronously  
- Fetch translation job status and translated results  
- Celery worker integration with Redis  
- JWT authentication for secure endpoints  
- Rate limiting to prevent abuse  
- Input validation and error handling  

---

## ⚙️ Setup

###  Clone Repository

```bash
https://github.com/Sumishaparthas15/backend-design-test.git
cd low_level_design 



## Components
- **API Layer (Django REST Framework)** — handles job creation, status, and result fetching.
- **Database (PostgreSQL)** — stores job metadata, queue info, and statuses.
- **Worker Layer (Celery/Redis)** — processes queued translations asynchronously.
- **Autoscaler** — dynamically adjusts worker instances based on queue length.

## Files
- `api_spec.md` — REST API definitions
- `db_schema.sql` — database schema
- `pseudocode.md` — queue & scaling pseudocode





POSTMAN 
https://documenter.getpostman.com/view/33255970/2sB3WvMdEe

🔗 **Postman API Documentation:**  
[https://documenter.getpostman.com/view/33255970/2sB3WvMdEe](https://documenter.getpostman.com/view/33255970/2sB3WvMdEe)



