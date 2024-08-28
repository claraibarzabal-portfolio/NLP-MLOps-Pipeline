from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta

import pandas as pd
import sqlite3

# Función para obtener el timestamp de la última reseña procesada
def get_last_scraped_timestamp():
    conn = sqlite3.connect('/path/to/your/database.db')  # Conexión a la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(timestamp) FROM scraped_reviews')
    last_timestamp = cursor.fetchone()[0]
    conn.close()
    return last_timestamp

# Función para actualizar la base de datos con nuevas reseñas
def update_database(new_reviews):
    conn = sqlite3.connect('/path/to/your/database.db')
    new_reviews.to_sql('scraped_reviews', conn, if_exists='append', index=False)
    conn.close()

def web_scraping():
    try:
        last_timestamp = get_last_scraped_timestamp()
        
        # Código para extraer nuevas reseñas de Ryanair
        new_reviews = scrape_reviews()  # Implementa esta función según tu necesidad
        
        # Filtrar reseñas nuevas basadas en el timestamp
        if last_timestamp:
            new_reviews = new_reviews[new_reviews['timestamp'] > last_timestamp]
        
        if not new_reviews.empty:
            update_database(new_reviews)
        else:
            print("No hay nuevas reseñas para procesar.")
    
    except Exception as e:
        print(f"Error en el web scraping: {e}")
        raise

def scrape_reviews():
    # Implementar el scraping real - requests BeautifulSoup
    #  'timestamp' esté incluido en los datos de las reseñas
    pass


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['claraibarzabalr@gmail.com'],
}

with DAG('web_scraping_dag',
         default_args=default_args,
         description='DAG para web scraping de reseñas de Ryanair',
         schedule_interval='@monthly', 
         catchup=False) as dag:

    scrape = PythonOperator(
        task_id='web_scraping',
        python_callable=web_scraping,
        dag=dag
    )

    trigger_data_processing = TriggerDagRunOperator(
        task_id='trigger_data_processing',
        trigger_dag_id='data_processing_and_model_update_dag',
        dag=dag
    )

    scrape >> trigger_data_processing
