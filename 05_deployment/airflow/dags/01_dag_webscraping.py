from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime, timedelta

def web_scraping():
    # Código para extraer nuevas reseñas de Ryanair
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('web_scraping_dag',
         default_args=default_args,
         description='DAG para web scraping',
         schedule_interval='@monthly',
         catchup=False) as dag:

    scrape = PythonOperator(
        task_id='web_scraping',
        python_callable=web_scraping
    )

    trigger_data_processing = TriggerDagRunOperator(
        task_id='trigger_data_processing',
        trigger_dag_id='data_processing_and_model_update_dag'
    )

    scrape >> trigger_data_processing

