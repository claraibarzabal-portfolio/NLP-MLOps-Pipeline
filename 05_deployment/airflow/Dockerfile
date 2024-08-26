# Utilizar una imagen base oficial de Airflow
FROM apache/airflow:2.7.2

# Copiar los archivos de configuración, DAGs y plugins al contenedor
COPY ./airflow.cfg /usr/local/airflow/airflow.cfg
COPY ./dags /usr/local/airflow/dags
COPY ./plugins /usr/local/airflow/plugins

# Copiar el script de creación de usuario
COPY create_airflow_user.sh /usr/local/airflow/create_airflow_user.sh

# Dar permisos de ejecución al script
RUN chmod +x /usr/local/airflow/create_airflow_user.sh

# Configurar el directorio de trabajo
WORKDIR /usr/local/airflow

# Instalar dependencias adicionales si es necesario para los DAGs
# RUN pip install --no-cache-dir <paquete>

# Exponer el puerto para el webserver
EXPOSE 8080

# Ejecutar el script de creación de usuario al inicio
RUN /usr/local/airflow/create_airflow_user.sh

# Iniciar tanto el scheduler como el webserver
CMD ["bash", "-c", "airflow db upgrade && airflow scheduler & airflow webserver"]





