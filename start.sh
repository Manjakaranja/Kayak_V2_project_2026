#!/bin/bash
set -e

echo "Running Airflow migrations..."
airflow db migrate

echo "Starting Airflow..."
exec airflow standalone