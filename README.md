# Kayak Travel Recommendation Platform

## Project Overview

This project was developed as part of the Jedha Data Science & Engineering curriculum.

The objective is to build a complete cloud-based data engineering pipeline capable of collecting, storing, transforming and visualizing travel-related data in order to recommend the best destinations in France based on weather conditions and hotel availability.

The project combines API ingestion, web scraping, cloud storage, orchestration, ETL processes, data warehousing and dashboard deployment.

Live applications:

* Streamlit Dashboard: https://huggingface.co/spaces/stoneray/kayak_2026
* Airflow UI: https://kayak-v2-project-2026.onrender.com

---

## Business Objective

Kayak's marketing team wants to help users choose where to travel by providing additional information about destinations.

The application recommends destinations using:

* Weather forecasts
* Hotel availability
* Hotel ratings

The current scope focuses on 35 popular French destinations.

---

## Architecture

OpenWeather API
+
Booking.com

↓

Apache Airflow

↓

AWS S3 Data Lake

↓

AWS RDS PostgreSQL Data Warehouse

↓

Streamlit Dashboard

↓

Hugging Face Spaces

---

## Data Sources

### Weather Data

Weather forecasts are collected using the OpenWeather API.

Collected information includes:

* Temperature
* Feels-like temperature
* Humidity
* Wind speed
* Rain forecasts
* Weather conditions

### Hotel Data

Hotel information is collected from Booking.com using Scrapy and Playwright.

Collected information includes:

* Hotel name
* Rating
* Description
* Address
* Latitude
* Longitude
* Booking URL

---

## ETL Pipeline

The project follows a complete ETL architecture.

### Extract

* GPS coordinates retrieved using Nominatim
* Weather forecasts collected from OpenWeather
* Hotel information scraped from Booking.com

### Load to Data Lake

Raw datasets are stored in AWS S3.

### Transform

Cleaning operations include:

* Duplicate removal
* Missing value handling
* Datatype standardization
* City name normalization

### Load to Warehouse

Cleaned datasets are loaded into AWS RDS PostgreSQL.

---

## Workflow Orchestration

Apache Airflow orchestrates the entire pipeline.

Main DAG steps:

1. Extract coordinates
2. Extract weather forecasts
3. Upload raw weather data to S3
4. Transform weather dataset
5. Load cleaned weather data to PostgreSQL
6. Compute destination rankings
7. Scrape Booking.com hotels
8. Upload raw hotel data to S3
9. Transform hotel dataset
10. Load cleaned hotel data to PostgreSQL
11. Generate visualizations

Average execution time is approximately 10 minutes.

---

## Dashboard Features

### Destinations

* Top 5 recommended destinations
* Interactive weather-based map
* Destination ranking table

### Hotels

* Top rated hotels
* Interactive hotel map
* City filtering

### Analytics

* Hotel rating distribution
* Destination weather score comparison
* Hotels collected per destination
* Access to cleaned datasets

---

## Technologies

### Data Collection

* Python
* Requests
* Scrapy
* Playwright

### Data Processing

* Pandas
* NumPy

### Cloud Services

* AWS S3
* AWS RDS PostgreSQL

### Orchestration

* Apache Airflow

### Visualization

* Plotly
* Streamlit

### Deployment

* Docker
* Hugging Face Spaces
* Render

---

## Engineering Decisions

### Airflow Deployment

Airflow is deployed on Render and remains publicly accessible for demonstration purposes.

Due to the execution time required by the Scrapy + Playwright extraction process and free-tier compute limitations, production DAG executions are triggered from a local Dockerized Airflow environment.

This approach preserves orchestration capabilities while minimizing cloud costs.

### PostgreSQL Strategy

AWS RDS PostgreSQL is used as the project Data Warehouse to satisfy the project requirements.

A separate PostgreSQL instance is also used for Airflow metadata storage in order to keep orchestration concerns isolated from analytical workloads.

---

## Repository Structure

```text
src/
├── analytics
├── extract
├── transform
├── load
├── visualization
└── orchestration

data/
├── raw
└── outputs

config/
logs/
```

---

## Author

Manjakasoaa R.

Data Engineering Portfolio Project — Jedha Bootcamp
