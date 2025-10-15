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

This repo is set up to deploy from source on DigitalOcean App Platform (no Dockerfile needed in production).

- The spec in `.do/app.yaml` defines:
  - A Python service for the API at path `/api` running Gunicorn
  - A static site for the frontend built from `frontend/` and served at `/`
  - A pre-deploy job that runs `migrate` and `collectstatic`

Minimal steps on DO:
1) Create an App from this repo. DO will detect `.do/app.yaml`.
2) Add a Managed MySQL database and attach it to the `api` service.
3) Configure env vars on the `api` service:
   - DJANGO_SETTINGS_MODULE=leave_management.settings_production
   - SECRET_KEY=your-production-secret
   - DATABASE_URL=mysql://USER:PASS@HOST:3306/DBNAME (auto-set if attached)
   - RUN_SEED_ON_DEPLOY=1 (optional on first deploy)
4) Deploy. The API will be available under `/api` and the frontend at `/`.

Note: The Dockerfile remains for local/dev builds only.
