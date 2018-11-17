#!/bin/sh

echo "Running Release Tasks"

echo "Running Migrations"

./manage.py collectstatic --no-input
./python manage.py migrate
echo "Done"
