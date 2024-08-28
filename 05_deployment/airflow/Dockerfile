FROM apache/airflow:2.7.2

# Copia archivos necesarios
COPY ./airflow.cfg /opt/airflow/airflow.cfg
COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins
COPY ./wait-for-it.sh /opt/airflow/wait-for-it.sh 

COPY ./create_airflow_user.sh /opt/airflow/create_airflow_user.sh
COPY ./init-airflow.sh /opt/airflow/init-airflow.sh

# Cambia permisos para los scripts
USER root
RUN chmod +x /opt/airflow/wait-for-it.sh /opt/airflow/create_airflow_user.sh /opt/airflow/init-airflow.sh

# Cambia al usuario airflow
USER airflow

# Instala paquetes con pip
RUN pip install 'apache-airflow[celery, redis]'

# Establece el directorio de trabajo
WORKDIR /opt/airflow

# Comando por defecto para inicializar la base de datos y crear el usuario
CMD ["bash", "-c", "/opt/airflow/wait-for-it.sh postgres:5432 -- /opt/airflow/init-airflow.sh && airflow webserver"]



