#!/usr/bin/env bash
# Generate SEED_USERS JSON from local/seed_users.json for production deployment

set -euo pipefail

if [ -f "local/seed_users.json" ]; then
  SEED_USERS_JSON=$(cat local/seed_users.json | jq -c .)
  echo "SEED_USERS='${SEED_USERS_JSON}'"
  echo "# Paste the above into your DO App env (SEED_USERS) and set RUN_SEED_ON_DEPLOY=1 for a one-time seed."
else
  echo "local/seed_users.json not found" >&2
  exit 1
fi
