# Kayak Travel Recommendation Platform

## Overview

This project was developed as part of the Jedha Data Science & Engineering curriculum.

The objective is to build a complete cloud-based data engineering platform capable of collecting, storing, transforming and visualizing travel-related data in order to recommend the best destinations in France based on weather conditions and hotel availability.

The project combines API ingestion, web scraping, cloud storage, orchestration, ETL processes, data warehousing, containerization and dashboard deployment.

---

## Live Applications

### Dashboard

https://huggingface.co/spaces/stoneray/kayak_2026

Interactive Streamlit dashboard deployed on Hugging Face Spaces.

### Airflow

https://kayak-v2-project-2026.onrender.com

Public Airflow instance used to demonstrate orchestration and DAG execution.

---

## Business Objective

Kayak's marketing team wants to help users identify the best destinations in France by combining:

* Weather forecasts
* Hotel availability
* Hotel ratings

The platform generates destination recommendations and highlights highly-rated hotels located in the selected destinations.

The current scope focuses on 35 popular French destinations.

---

# Architecture

OpenWeather API
+
Booking.com

↓

Data Engineering Repository

↓

Apache Airflow

↓

AWS S3 Data Lake

↓

AWS RDS PostgreSQL

↓

Dashboard Repository

↓

Streamlit Application

↓

Hugging Face Spaces

---

## Repository Organization

The project is intentionally split into two repositories.

### 1. Data Engineering Repository

This repository contains the complete ETL platform and infrastructure layer.

Responsibilities:

* API ingestion
* Web scraping
* ETL processing
* Data Lake management
* Data Warehouse loading
* Workflow orchestration
* Analytics generation
* Visualization generation

Project structure:

```text
KAYAK/
├── config/
│   └── cities.json
│
├── dags/
│   ├── kayak.py
│   └── test_kayak.py
│
├── data/
│   ├── raw/
│   │   ├── booking/
│   │   ├── coordinates/
│   │   └── weather/
│   │
│   └── outputs/
│       ├── hotels_cleaned.csv
│       ├── weather_cleaned.csv
│       ├── top_5_destinations.csv
│       ├── top_5_destinations.html
│       └── top_20_hotels_map.html
│
├── logs/
├── notebooks/
├── plugins/
│
├── src/
│   ├── analytics/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── orchestration/
│   └── visualization/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── start.sh
```

This repository is responsible for building and maintaining the complete data pipeline.

---

### 2. Dashboard Repository

A dedicated repository is used to deploy the dashboard on Hugging Face Spaces.

Responsibilities:

* Streamlit application
* PostgreSQL connection
* Interactive visualizations
* Business-facing presentation layer

Project structure:

```text
kayak_2026/
├── coordinates.json
├── Dockerfile
├── README.md
├── requirements.txt
└── src/
    └── streamlit_app.py
```

The dashboard directly queries AWS RDS PostgreSQL and remains independent from the ETL codebase.

This separation simplifies deployment and follows a production-oriented separation of concerns between data engineering and analytics layers.

---

# Data Sources

## Weather Data

Weather forecasts are collected using the OpenWeather API.

Collected information includes:

* Temperature
* Feels-like temperature
* Humidity
* Wind speed
* Rain forecasts
* Weather conditions

---

## Hotel Data

Hotel information is collected from Booking.com using Scrapy and Playwright.

Collected information includes:

* Hotel name
* Hotel rating
* Description
* Address
* Latitude
* Longitude
* Booking URL

---

# ETL Pipeline

The project follows a complete ETL architecture.

## Extract

### Coordinates

GPS coordinates are retrieved using Nominatim.

### Weather

Weather forecasts are collected through the OpenWeather API.

### Hotels

Hotel information is scraped from Booking.com using Scrapy and Playwright.

---

## Load to Data Lake

Raw datasets are uploaded to AWS S3.

Stored datasets include:

* Coordinates
* Weather forecasts
* Hotel information

---

## Transform

Data cleaning operations include:

* Duplicate removal
* Missing value handling
* Datatype standardization
* City name normalization
* Quality control checks

---

## Load to Data Warehouse

Cleaned datasets are loaded into AWS RDS PostgreSQL.

Main analytical tables:

* weather_cleaned
* hotels_cleaned
* top_5_destinations

These tables are directly consumed by the dashboard.

---

# Workflow Orchestration

Apache Airflow orchestrates the complete ETL pipeline.

Main DAG steps:

1. Extract coordinates
2. Extract weather forecasts
3. Upload raw weather data to S3
4. Transform weather dataset
5. Load weather dataset to PostgreSQL
6. Compute destination rankings
7. Scrape Booking.com hotels
8. Upload raw hotel data to S3
9. Transform hotel dataset
10. Load hotel dataset to PostgreSQL
11. Generate destination visualizations
12. Generate hotel visualizations

Average execution time is approximately 10 minutes.

---

# Dashboard Features

## Destinations

* Top 5 recommended destinations
* Interactive destination map
* Weather ranking table

---

## Hotels

* Top-rated hotels
* Interactive hotel map
* City-level filtering

---

## Analytics

The dashboard includes additional analytics built directly from the PostgreSQL warehouse:

* Hotel rating distribution
* Destination weather score comparison
* Hotels collected per destination
* Full access to cleaned datasets

---

# Technology Stack

## Data Collection

* Python
* Requests
* Scrapy
* Playwright

## Data Processing

* Pandas
* NumPy

## Cloud Services

* AWS S3
* AWS RDS PostgreSQL

## Orchestration

* Apache Airflow

## Visualization

* Plotly
* Streamlit

## Containerization

* Docker
* Docker Compose

## Deployment

* Hugging Face Spaces
* Render

---

# Engineering Decisions

## Airflow Deployment

Airflow is deployed on Render and remains publicly accessible for demonstration purposes.

The pipeline was successfully tested on Render. However, due to the execution time required by the Scrapy and Playwright extraction process and the compute limitations of the free tier, production executions are triggered from a local Dockerized Airflow environment.

This approach preserves orchestration capabilities while minimizing cloud costs.

---

## PostgreSQL Strategy

AWS RDS PostgreSQL is used as the analytical Data Warehouse.

A separate PostgreSQL instance hosted on Neon is used for Airflow metadata storage.

This separation keeps orchestration concerns isolated from analytical workloads.

---

## Repository Separation

The ETL platform and dashboard application are maintained in separate repositories.

This design choice was made to:

* isolate infrastructure code from presentation code
* simplify Hugging Face deployment
* reduce container size
* allow independent updates of the dashboard
* follow a production-oriented architecture

The dashboard acts as a lightweight analytics application consuming curated data directly from PostgreSQL.

---

# Results

The pipeline processes:

* 35 French destinations
* Weather forecasts from OpenWeather
* 125 hotels scraped from Booking.com
* Top 5 recommended destinations
* Interactive destination and hotel maps

The final datasets are stored in AWS S3 and AWS RDS PostgreSQL before being exposed through a Streamlit dashboard.

---

# Future Improvements

Potential improvements include:

* Incremental data ingestion
* Automated monitoring and alerting
* CI/CD integration
* Infrastructure as Code deployment
* Historical trend analysis
* Additional destination recommendation metrics

---

# Author

Manjakasoa R.

Jedha Bootcamp — Fullstack Data Science & Engineering
