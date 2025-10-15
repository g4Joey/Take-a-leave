# Leave Request Management (Generic)

This is a generic, unbranded version of the Leave Request Management app.
It includes only local development and DigitalOcean deployment assets.

## Quick start (local)

```bash
# 1) Create virtualenv (optional) and install dependencies
python -m venv .venv
. .venv/Scripts/activate  # on Windows
pip install -r requirements.txt

# 2) Run database migrations and start server
python manage.py migrate
python manage.py runserver
```

## Docker (local)

```bash
# Build and run
docker build -t leave-request-app:latest .
# With compose (local)
docker compose up --build
```

## DigitalOcean App Platform

- Build from Dockerfile at repo root
- Expose port 8000 (Gunicorn in entrypoint binds to 0.0.0.0:8000)
- Set environment variables:
  - DJANGO_SETTINGS_MODULE=leave_management.settings_production
  - SECRET_KEY=your-production-secret
  - DATABASE_URL=mysql://USER:PASS@HOST:3306/DBNAME  (Managed MySQL)
  - RUN_SEED_ON_DEPLOY=1 (optional) to seed initial users

Ensure you add a Managed MySQL database and link it (prefer SSL required).