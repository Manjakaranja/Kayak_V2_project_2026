#!/bin/bash

set -e

echo "Running Airflow migrations..."
airflow db migrate

echo "Starting scheduler..."
airflow scheduler &

echo "Starting triggerer..."
airflow triggerer &

echo "Starting API server on port 8080..."
exec airflow api-server --port 8080 --hostname 0.0.0.0