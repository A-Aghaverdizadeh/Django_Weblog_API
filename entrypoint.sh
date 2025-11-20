#!/bin/sh

# Exit on error
set -e

echo "Create migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000
