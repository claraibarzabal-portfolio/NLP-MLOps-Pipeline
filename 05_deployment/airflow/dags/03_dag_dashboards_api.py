from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
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

with DAG(
    dag_id='api_and_dashboard_dag',
    default_args=default_args,
    description='DAG para API y dashboards',
    schedule_interval='@monthly',
    catchup=False
) as dag:

    # Agrupación de tareas usando TaskGroup
    with TaskGroup(group_id='api_tasks') as api_tasks:
        deploy_api = PythonOperator(
            task_id='api_deployment',
            python_callable=api_deployment
        )

    with TaskGroup(group_id='dashboard_tasks') as dashboard_tasks:
        create_dashboard = PythonOperator(
            task_id='dashboard_creation',
            python_callable=dashboard_creation
        )

    # Definir el orden de ejecución
    deploy_api >> create_dashboard
