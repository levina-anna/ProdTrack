#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Load initial data
echo "Loading initial data..."
python manage.py loaddata 'prod_project/initial_data.json'

# Create superuser
echo "Creating superuser..."
python create_superuser.py

# Start server
echo "Starting server..."
exec "$@"
