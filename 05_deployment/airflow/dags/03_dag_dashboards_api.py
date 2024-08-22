from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def api_deployment():
    # Código para desplegar el API de predicción de sentimientos
    pass

def dashboard_creation():
    # Código para crear dashboards interactivos
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('api_and_dashboard_dag',
         default_args=default_args,
         description='DAG para API y dashboards',
         schedule_interval='@monthly',
         catchup=False) as dag:

    deploy_api = PythonOperator(
        task_id='api_deployment',
        python_callable=api_deployment
    )

    create_dashboard = PythonOperator(
        task_id='dashboard_creation',
        python_callable=dashboard_creation
    )

    deploy_api >> create_dashboard
