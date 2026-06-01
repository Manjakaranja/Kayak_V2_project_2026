from airflow import DAG
from airflow.operators.bash import BashOperator # type: ignore
from datetime import datetime, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

default_args = {
    'owner' : 'manjaka',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='kayak_etl_pipeline',
    default_args=default_args,
    description='Full ETL: Weather and Booking data extraction to S3/RDS with Analytics',
    schedule='@weekly',
    start_date=datetime(2026, 5, 31),
    catchup=False,
) as dag :
    
    # Weather pipeline

    Coordinates_extraction = BashOperator(
        task_id="Coordinates_extraction",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.extract.extract_coordinates"
    )

    Weather_extraction = BashOperator(
        task_id="Weather_extraction",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.extract.extract_weather"
    )

    Load_raw_weather_s3 = BashOperator(
        task_id="Load_raw_weather_s3",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_s3"
    )

    Transform_weather_data = BashOperator(
        task_id="Transform_weather_data",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.transform.transform_weather"
    )

    Load_trans_weather_data_s3 = BashOperator(
        task_id="Load_trans_weather_data_s3",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_s3"
    )

    Load_trans_weather_data_rds = BashOperator(
        task_id="Load_trans_weather_data_rds",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_rds"
    )

    Create_top_destination_table = BashOperator(
        task_id="Create_top_destination_table",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.analytics.create_top_destinations"
    )

    # Hotels pipeline

    Booking_extraction = BashOperator(
        task_id="Booking_extraction",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.extract.extract_booking"
    )

    Load_raw_booking_s3 = BashOperator(
        task_id="Load_raw_booking_s3",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_s3"
    )



    Transform_booking_data = BashOperator(
        task_id="Transform_booking_data",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.transform.transform_booking"
    )

    Load_trans_booking_data_s3 = BashOperator(
        task_id="Load_trans_booking_data_s3", 
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_s3"
    )

    Load_trans_booking_data_rds = BashOperator(
        task_id = "Load_trans_booking_data_rds",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.load.load_to_rds"
    )

   # Visualizations

    Plot_top_destinations = BashOperator(
        task_id = "Plot_top_destinations",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.visualization.plot_top_destinations"
    )
    
    Plot_top_hotels = BashOperator(
        task_id= "Plot_top_hotels",
        bash_command=f"cd {PROJECT_ROOT} && python -m src.visualization.plot_top_hotels"
    )

    Coordinates_extraction \
    >> Weather_extraction \
    >> Load_raw_weather_s3 \
    >> Transform_weather_data \
    >> Load_trans_weather_data_s3 \
    >> Load_trans_weather_data_rds \
    >> Create_top_destination_table

    Create_top_destination_table \
    >> Booking_extraction \
    >> Load_raw_booking_s3 \
    >> Transform_booking_data \
    >> Load_trans_booking_data_s3 \
    >> Load_trans_booking_data_rds  

    Load_trans_booking_data_rds >> [
        Plot_top_hotels,
        Plot_top_destinations
    ]