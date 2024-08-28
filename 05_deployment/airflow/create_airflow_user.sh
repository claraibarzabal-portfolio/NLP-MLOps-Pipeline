#!/bin/bash

#!/bin/bash

# Esperar a que Airflow esté listo para aceptar comandos
sleep 30 # Asegúrate de ajustar el tiempo según sea necesario

# Crear usuario de Airflow con permisos de administrador
airflow users create \
    --username admin \
    --firstname Clara \
    --lastname Ibarzabal \
    --role Admin \
    --email claraibarzabalr@gmail.com \
    --password 789456



