from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime, timedelta

def data_processing():
    # Código para procesar los datos extraídos
    pass

def model_training():
    # Código para entrenar los modelos LSTM y BERT
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('data_processing_and_model_update_dag',
         default_args=default_args,
         description='DAG para procesamiento de datos y actualización del modelo',
         schedule_interval='@monthly',
         catchup=False) as dag:

    process = PythonOperator(
        task_id='data_processing',
        python_callable=data_processing
    )

    train = PythonOperator(
        task_id='model_training',
        python_callable=model_training
    )

    deploy_api = TriggerDagRunOperator(
        task_id='trigger_api_and_dashboard',
        trigger_dag_id='api_and_dashboard_dag'
    )

    process >> train >> deploy_api
