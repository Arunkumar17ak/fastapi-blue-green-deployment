# FastAPI Blue-Green Deployment on AWS

This project demonstrates a **Blue-Green Deployment strategy** using FastAPI, Docker, Nginx, and AWS EC2.

It enables **zero-downtime deployments** by running two versions of the application simultaneously and switching traffic between them.

---

## Architecture

User Request
      │
      ▼
   Nginx (Reverse Proxy)
      │
 ┌────┴────┐
 │         │
 ▼         ▼
BLUE      GREEN
Port 8001 Port 8002
