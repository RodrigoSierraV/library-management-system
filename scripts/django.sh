#!/bin/bash
echo "Starting Migrations..."
python manage.py migrate
echo ====================================

python manage.py loaddata books/books.json

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000
