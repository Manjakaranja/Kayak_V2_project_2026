from airflow import DAG
from airflow.operators.bash import BashOperator # type: ignore
from datetime import datetime, timedelta

default_args = {
    'owner' : 'manjaka',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='test_kayak',
    default_args=default_args,
    description='Test of Kayak airflow',
    schedule='@daily',
    start_date=datetime(2026, 5, 31),
    catchup=False,
) as dag :
    
    hello = BashOperator(
        task_id="hello",
        bash_command="echo Hello Airflow"
    )

    goodbye = BashOperator(
        task_id="bye",
        bash_command="echo Goodbye Airflow"
    )

    hello >> goodbye