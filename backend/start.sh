#!/bin/bash

# Activate virtual environment (if applicable)
# source /path/to/venv/bin/activate

# Export environment variables (if needed)
# export FLASK_ENV=production
# export DATABASE_URL=your_database_url
export SECRET_KEY=freshibarida

# Run database migrations (if needed)
# flask db upgrade

# Start Gunicorn server
gunicorn -b 0.0.0.0:5000 -w 4 backend.app:app --access-logfile -
