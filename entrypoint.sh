#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python create_superuser.py

# Load initial data
echo "Loading initial data..."
python manage.py loaddata initial_data.json

# Start server
echo "Starting server..."
exec "$@"
