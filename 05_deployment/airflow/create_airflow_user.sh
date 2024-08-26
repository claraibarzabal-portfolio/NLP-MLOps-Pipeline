#!/bin/bash

# Crear usuario de Airflow con permisos de administrador
airflow users create \
    --username admin \
    --firstname Clara \
    --lastname Ibarzabal \
    --role Admin \
    --email claraibarzabalr@gmail.com \
    --password 789456
