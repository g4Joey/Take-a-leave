# 🏖️ Leave Request Management (Generic)

Streamlined leave requests, approvals, and tracking with a clean Django backend and a modern frontend, packaged for local development and DigitalOcean App Platform.

## 🌟 Features

- 📝 Submit and track leave requests
- ✅ Manager approval workflow
- 📊 Dashboard and leave balance tracking
- 🔔 Notifications and status updates
- 🔒 JWT authentication and role-based access
- 🗄️ MySQL for production; SQLite-friendly for local dev

## 🚀 Quick Start (Local)

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Local endpoints:
- API: http://127.0.0.1:8000/api/
- Admin: http://127.0.0.1:8000/admin/

## 🐳 Docker (Local Only)

```cmd
docker compose up --build
```

The Dockerfile is intended for local/dev workflows. Production on DigitalOcean uses source-based deploys.

## ☁️ DigitalOcean App Platform (Production)

This repository deploys from source via `.do/app.yaml` (no Dockerfile build in production).

What’s included:
- API service (Gunicorn) served under `/api`
- Frontend static site from `frontend/` at `/`
- Pre-deploy job to run `migrate` and `collectstatic`

Minimal setup on DigitalOcean:
1) Create an App from this repo (DO auto-detects `.do/app.yaml`).
2) Add a Managed MySQL database and attach it to the `api` service.
3) Set environment variables on the `api` service:
  - `DJANGO_SETTINGS_MODULE=leave_management.settings_production`
  - `SECRET_KEY=your-production-secret`
  - `DATABASE_URL=mysql://USER:PASS@HOST:3306/DBNAME` (auto-provisioned when attached)
  - `RUN_SEED_ON_DEPLOY=1` (optional on first deploy)
4) Deploy. Frontend is served at `/` and the API at `/api`.

One‑click deploy:

[![Deploy on Hostinger](https://assets.hostinger.com/vps/deploy.svg)](https://www.hostinger.com/vps/docker-hosting?compose_url=https://github.com/g4Joey/Take-a-leave/)

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/g4Joey/Take-a-leave/tree/main)

## 🌱 Seeding and initial users

On first deploy, you can seed users safely and idempotently:

- Set `RUN_SEED_ON_DEPLOY=1` on the API service to run `setup_production_data` during deploy.
- Optionally provide `SEED_USERS` as a JSON array of users to create/update (non-sensitive fields only). Passwords are only set on create.

Example `SEED_USERS` snippet (do not commit real credentials):

```json
[
  { "username": "manager1", "first_name": "Ato", "last_name": "Lastname", "email": "manager1@example.com", "role": "manager", "department": "IT", "password": "<set-at-deploy>" }
]
```

You can also set `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_PASSWORD`, and HR admin vars (`HR_ADMIN_USERNAME`, `HR_ADMIN_PASSWORD`, etc.) for initial access.

## 🧱 Tech Stack

- Backend: Django 5 + Django REST Framework
- Auth: JWT (Simple JWT)
- Database: MySQL (production), SQLite (local)
- Frontend: React + Tailwind (built to static `/frontend/build`)

## 📁 Project Structure (Top-level)

```
generic_export/
├── leave_management/   # Django project settings & URLs
├── users/              # User accounts, roles
├── leaves/             # Leave request domain
├── notifications/      # Notification hooks
├── frontend/           # Frontend source (built by DO)
├── .do/app.yaml        # DigitalOcean App Platform spec
├── Dockerfile          # Local/dev only
├── docker-compose.yml  # Local/dev only
└── README.md
```

## 🔐 Production Notes

- Always use a strong `SECRET_KEY` and set `DEBUG=False` in production.
- Attach a Managed MySQL database and enforce SSL.
- Update `ALLOWED_HOSTS` and CSRF settings to match your DO domains.

