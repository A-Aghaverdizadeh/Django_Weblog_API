#!/bin/bash
set -e

# If running as root, fix volume permissions then switch user
if [ "$(id -u)" = "0" ]; then
    echo "Fixing static & media permissions..."
    mkdir -p /app/static /app/media
    chown -R appuser:appuser /app/static /app/media || true
    chmod -R 755 /app/static /app/media
    
    echo "Switching to appuser..."
    exec su appuser -c "$0 $@"
fi

# Now running as appuser
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
exec "$@"
gunicorn core.wsgi
