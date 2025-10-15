@echo off
REM Generate SEED_USERS JSON from local\seed_users.json for production deployment

if exist "local\seed_users.json" (
  for /f "usebackq delims=" %%a in (`type local\seed_users.json`) do set "JSON=%%a"
  echo SEED_USERS=%JSON%
  echo # Paste the above into your DO App env (SEED_USERS) and set RUN_SEED_ON_DEPLOY=1 for a one-time seed.
) else (
  echo local\seed_users.json not found 1>&2
  exit /b 1
)
