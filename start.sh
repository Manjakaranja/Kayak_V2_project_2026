#!/bin/bash

set -e

echo "Running Airflow migrations..."
airflow db migrate

echo "Starting scheduler..."
airflow scheduler &

echo "Starting triggerer..."
airflow triggerer &

echo "Starting API server..."
exec airflow api-server