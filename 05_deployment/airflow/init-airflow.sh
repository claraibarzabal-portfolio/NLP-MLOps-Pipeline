#!/bin/bash

# Esperar a que PostgreSQL esté disponible
/opt/airflow/wait-for-it.sh postgres:5432 --timeout=60

# Inicializar la base de datos de Airflow
airflow db init

# Iniciar el scheduler y el webserver
airflow scheduler &
airflow webserver &
wait
