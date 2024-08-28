from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 21),
}

with DAG(
    'test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval='@daily',
    catchup=False
) as dag:

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    start >> end
