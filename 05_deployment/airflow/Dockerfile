# Utilizar una imagen base oficial de Airflow
FROM apache/airflow:2.7.2

# Establecer el usuario de Airflow
USER airflow

# Copiar los archivos de configuración, DAGs y plugins al contenedor
COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins
COPY ./airflow.cfg /opt/airflow/airflow.cfg

# Instalar dependencias adicionales si es necesario para los DAGs
# RUN pip install --no-cache-dir <paquete>

# Configurar el directorio de trabajo
WORKDIR /opt/airflow

# Exponer el puerto para el webserver
EXPOSE 8080

# Iniciar tanto el scheduler como el webserver
CMD ["bash", "-c", "airflow db upgrade && airflow scheduler & airflow webserver"]








