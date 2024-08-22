from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, Airflow!")

default_args = {
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
}

with DAG(dag_id='hello_airflow', default_args=default_args, schedule_interval='@daily') as dag:
    task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
