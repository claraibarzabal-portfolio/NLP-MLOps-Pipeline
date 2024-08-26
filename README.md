# NLP-MLOps-Pipeline
Automated sentiment analysis of Ryanair reviews using NLP and MLOps. Classifies reviews as positive, negative, or neutral with LSTM and BERT models. Includes automated data pipelines, Docker/Kubernetes deployment, CI/CD, and drift detection. Dashboards offer insights into trends and customer feedback.

# Project Status

**Work in Progress**

This project is currently a work in progress, including the README file itself. The details provided here will be updated as the project advances and as tools and technologies are implemented or chosen. Please check back for updates as new information becomes available.


---
# AHORA
# DAGS
# PROXIMOS PASOS
# Próximos Pasos: DAGS, Airflow, MLFlow, CI/CD, Astro.(Dps Dockerx2, dps pruebas, despliegue (airflow, kubernetes, kubeflow, spark. )monitoreo, drift, dvc, actualizacion y reentrenamiento.)
DAGs Configuration and Management Process
Define DAGs:

Create DAGs: Write Python scripts to define your Directed Acyclic Graphs (DAGs). These DAGs will orchestrate your workflows.
Define Tasks: Within each DAG, specify tasks using operators (e.g., PythonOperator, BashOperator, TriggerDagRunOperator).
Configure DAGs in Airflow:

Place DAGs: Save your DAG files in the Airflow dags folder. This is where Airflow will automatically discover and load them.
Set Default Arguments: Define default_args such as owner, depends_on_past, start_date, retries, and retry_delay to handle task execution behavior.
Test DAGs:

Manual Testing: Trigger DAGs manually from the Airflow UI to ensure they execute as expected.
Check Logs: Monitor task logs and debug any issues. Access logs through the Airflow UI under the Logs tab for each task instance.
Run Tests: Use the Airflow CLI to test DAGs:
bash
Copiar código
airflow dags test <dag_id> <start_date>
Verify Scheduling:

Ensure Correct Schedule: Confirm that DAGs are running as per the defined schedule_interval (e.g., @daily, @monthly).
Monitor Execution: Use the Airflow UI to check the DAG runs and task statuses.
Optimize and Maintain DAGs:

Refactor Code: Periodically review and refactor your DAGs for performance improvements and code cleanliness.
Update Dependencies: Ensure that your DAGs and tasks use the latest versions of dependencies and packages.

---
---

Claro, aquí tienes los pasos adaptados para trabajar en PowerShell dentro de Visual Studio Code. Te guiaré a través de la instalación y configuración de CeleryExecutor con Redis para tu proyecto de NLP/MLOps:

### Paso 1: Instalar Dependencias

1. **Instalar Celery y Redis en tu entorno virtual**:
   - Abre PowerShell en VSCode y activa tu entorno virtual (si aún no lo has hecho):
     ```powershell
     .\venv\Scripts\Activate
     ```
   - Luego, instala Celery y Redis:
     ```powershell
     pip install apache-airflow[celery]
     pip install redis
     ```

2. **Instalar Redis**:
   - Puedes descargar e instalar Redis desde [la página oficial de Redis](https://redis.io/download). Si estás usando Windows, puedes utilizar [Redis para Windows](https://github.com/microsoftarchive/redis/releases).
   - Después de descargar el instalador, sigue las instrucciones para instalar Redis.

### Paso 2: Configurar Redis

1. **Iniciar Redis**:
   - Abre una nueva ventana de PowerShell y navega a la carpeta donde instalaste Redis.
   - Inicia el servidor Redis ejecutando el siguiente comando:
     ```powershell
     .\redis-server.exe
     ```
   - Asegúrate de que Redis esté funcionando correctamente ejecutando:
     ```powershell
     .\redis-cli.exe ping
     ```
   - Deberías recibir una respuesta `PONG`.

### Paso 3: Configurar Airflow para Usar CeleryExecutor

1. **Editar `airflow.cfg`**:
   - Abre el archivo `airflow.cfg` con un editor de texto. Por lo general, se encuentra en el directorio de instalación de Airflow (dentro del entorno virtual).
   - Realiza los siguientes cambios:

   ```ini
   [core]
   # Cambia el executor a CeleryExecutor
   executor = CeleryExecutor

   [celery]
   # Configuración del broker y backend de resultados para Redis
   broker_url = redis://localhost:6379/0
   result_backend = redis://localhost:6379/0

   # Configura los trabajadores y el número de procesos
   worker_concurrency = 4
   ```

2. **Configurar Variables de Entorno** (opcional pero recomendado):
   - Puedes configurar las variables de entorno en PowerShell de la siguiente manera:
     ```powershell
     $env:AIRFLOW__CELERY__BROKER_URL = "redis://localhost:6379/0"
     $env:AIRFLOW__CELERY__RESULT_BACKEND = "redis://localhost:6379/0"
     $env:AIRFLOW__CORE__EXECUTOR = "CeleryExecutor"
     ```

### Paso 4: Configurar y Ejecutar Celery Workers

1. **Iniciar los Workers de Celery**:
   - Abre una nueva ventana de PowerShell y navega a la carpeta de tu proyecto Airflow.
   - Ejecuta el siguiente comando para iniciar los workers de Celery:
     ```powershell
     airflow celery worker
     ```

2. **Configurar el Webserver de Airflow**:
   - Abre una nueva ventana de PowerShell y navega a la carpeta de tu proyecto Airflow.
   - Inicia el webserver de Airflow en el puerto 8080:
     ```powershell
     airflow webserver --port 8080
     ```

3. **Configurar el Scheduler de Airflow**:
   - Abre otra ventana de PowerShell y navega a la carpeta de tu proyecto Airflow.
   - Inicia el scheduler de Airflow:
     ```powershell
     airflow scheduler
     ```

### Paso 5: Verificar la Configuración

1. **Acceder a la Interfaz Web de Airflow**:
   - Abre tu navegador y ve a `http://localhost:8080`. Deberías poder acceder a la interfaz de usuario de Airflow.

2. **Revisar los Logs**:
   - Asegúrate de que no haya errores en los logs de los workers, el scheduler y el webserver. Los logs suelen estar en el directorio `logs` dentro de la instalación de Airflow.

### Consideraciones Adicionales

- **Seguridad**: Asegúrate de configurar adecuadamente los permisos y la seguridad para Redis y Airflow en un entorno de producción.
- **Escalabilidad**: Ajusta el número de workers y su concurrencia según las necesidades de procesamiento de tu proyecto.

### Alternativa: Astronomer

Si prefieres una solución gestionada y profesional, **Astronomer** puede ser una excelente opción. Te ofrece una infraestructura administrada y soporte especializado. La configuración básica es similar a la de CeleryExecutor, pero Astronomer maneja muchos aspectos de la infraestructura y la administración por ti.

**Pasos para usar Astronomer**:

1. **Registrarse en Astronomer**:
   - Regístrate en [Astronomer](https://www.astronomer.io/) y sigue las instrucciones para configurar tu entorno.

2. **Migrar Tu Proyecto**:
   - Sigue las guías proporcionadas por Astronomer para desplegar y gestionar tu proyecto en su plataforma.

3. **Utilizar Soporte y Herramientas**:
   - Aprovecha el soporte y las herramientas de Astronomer para gestionar la infraestructura y resolver problemas.

Esta guía debería proporcionarte un camino claro para configurar CeleryExecutor en tu entorno de Airflow usando PowerShell en VSCode. Si necesitas más ayuda con Astronomer o cualquier otra opción, no dudes en decírmelo.
# Flujo de Trabajo para el Proyecto

## 1. Configurar y Probar Airflow

- **Configurar los DAGs en Airflow**: Definir y probar los DAGs necesarios para la orquestación de los pipelines.
- **Probar los DAGs**: Verificar que los DAGs funcionen correctamente.

## 2. Implementar MLflow

- **Configurar MLflow**: Establecer el entorno de MLflow para el seguimiento de experimentos y la gestión de modelos.
- **Integrar MLflow con Airflow**: Crear tareas en los DAGs que interactúen con MLflow si es necesario.

## 3. Realizar Pruebas Unitarias con pytest

- **Escribir Pruebas Unitarias**: Desarrollar pruebas unitarias para los scripts, modelos y cualquier otra lógica del proyecto.
- **Ejecutar las Pruebas**: Usar pytest para ejecutar las pruebas y verificar que el código funcione correctamente.
- **Corregir Errores**: Corregir los errores encontrados durante las pruebas antes de continuar.

## 4. Configurar CI/CD

- **Configurar el Pipeline de CI/CD**:
  - **GitHub Actions, GitLab CI/CD o Jenkins**: Configurar el pipeline para la automatización del proceso de integración y despliegue.
  - **Terraform**: Utilizar Terraform para gestionar la infraestructura como código.

## 5. Construir y Ejecutar Contenedores Docker

- **Construir Contenedores Docker**:
  - **FastAPI**:
    ```bash
    cd 05_deployment/fastapi
    docker build -t fastapi-lstm .
    ```
  - **Streamlit**:
    ```bash
    cd 05_deployment/streamlit
    docker build -t streamlit-frontend .
    ```
- **Ejecutar Contenedores Docker**:
  - **FastAPI**:
    ```bash
    docker run -d -p 8000:8000 fastapi-lstm
    ```
  - **Streamlit**:
    ```bash
    docker run -d -p 8501:8501 streamlit-frontend
    ```

## 6. Configurar Astro

- **Configurar Astro**: Usar Astro para gestionar el despliegue y la escalabilidad de Airflow en producción.
- **Integrar Astro con Airflow**: Conectar Astro con el entorno de Airflow.

## 7. Desplegar

- **Configurar el Despliegue en Producción**: Preparar el entorno de producción y realizar el despliegue de Airflow, MLflow, FastAPI y Streamlit usando Astro para la gestión.

## 8. Configurar Monitoreo y Detección de Drift

- **Implementar Monitoreo**: Configurar herramientas de monitoreo y detección de drift como Prometheus, Evidently AI o Alibi Detect.

## 9. Implementar Versionamiento de Datos y Actualización de Modelos

- **Configurar DVC**: Implementar DVC para el control de versiones de datos.
- **Actualizar y Reentrenar Modelos**: Establecer procesos para la actualización y reentrenamiento de modelos basado en monitoreo y detección de drift.


## DOCKERx2
## A. Construcción de Contenedores Docker

### Para FastAPI:
1. Navegar al directorio `05_deployment/fastapi`:
    ```bash
    cd 05_deployment/fastapi
    ```
2. Construir la imagen de Docker para FastAPI:
    ```bash
    docker build -t fastapi-lstm .
    ```

### Para Streamlit:
1. Navegar al directorio `05_deployment/streamlit`:
    ```bash
    cd 05_deployment/streamlit
    ```
2. Construir la imagen de Docker para Streamlit:
    ```bash
    docker build -t streamlit-frontend .
    ```

## B. Ejecución de Contenedores Docker

### Ejecutar FastAPI:
1. Correr el contenedor de FastAPI en el puerto 8000:
    ```bash
    docker run -d -p 8000:8000 fastapi-lstm
    ```

### Ejecutar Streamlit:
1. Correr el contenedor de Streamlit en el puerto 8501:
    ```bash
    docker run -d -p 8501:8501 streamlit-frontend
    ```

## C. Pruebas

### FastAPI:
1. Abrir el navegador y acceder a [http://localhost:8000/docs](http://localhost:8000/docs) para verificar la documentación interactiva.

### Streamlit:
1. Abrir el navegador y acceder a [http://localhost:8501](http://localhost:8501) para interactuar con la interfaz de usuario.

## D. Verificación de Comunicación

1. Asegurarme de que el frontend de Streamlit se comunique con el backend de FastAPI a través de [http://localhost:8000/predict](http://localhost:8000/predict).

## E. Revisión y Depuración

1. Si encuentro problemas, revisar los logs de los contenedores:
    ```bash
    docker logs <container_id>
    ```
2. Obtener el ID del contenedor con:
    ```bash
    docker ps
    ```

## F. Documentación y Versionado

1. Actualizar la documentación.
2. Versionar las imágenes Docker y considerar subirlas a un registro como Docker Hub o GitHub Container Registry.

##  Contexto Macro del Proyecto

### 1. Orquestación y Pipelines: - Apache Airflow, Metaflow, o Kubeflow. (Kubernetes)
1. Implementar la orquestación y gestión de pipelines con Apache Airflow, Metaflow, o Kubeflow.
2. Considerar Kubernetes para la orquestación de contenedores, especialmente si se requiere escalabilidad o despliegue distribuido.

### 2. Implementar MLflow:
1. Configurar MLflow para gestionar experimentos y modelos.
2. Registrar métricas, artefactos y modelos.

### 3. CI/CD: - GitHub Actions o GitLab CI/CD - Jenkins - Terraform
1. Desarrollar un pipeline de CI/CD robusto para automatizar el proceso de integración y despliegue.

### 4. Pruebas Unitarias: - Pytest
1. Implementar pruebas unitarias con pytest para asegurar la calidad del código.

### 5. Infraestructura como Código (IaC): - Terraform
1. Utilizar Terraform para gestionar la infraestructura de manera automatizada.

### 6. Despliegue del Modelo: - Apache Airflow // Kubernetes + Kubeflow // Apache Spark
1. Configurar el despliegue del modelo en modo batch y asegurar que se implemente correctamente. 

### 7. Monitoreo y Drift Detection: -  Prometheus, Evidently AI, Alibi detect
1. Implementar mecanismos de monitoreo y detección de drift para mantener la calidad del modelo. //

### 8. Versionamiento de Datos: DVC! - MLflow
1. Implementar un sistema de control de versiones para los datos utilizados en el entrenamiento y evaluación del modelo.

### 9. Actualización y Reentrenamiento:  Airflow/Kubeflow y MLflow 
1. Establecer un proceso para actualizar y reentrenar modelos basado en el monitoreo continuo.

### 10. MLOps terminado: AGREGAR graficos si llego
I want to focus on enhancing the application by adding graphs to both app_lstm (FastAPI) and the Streamlit interface. 

Bar Charts:  to display the number of positive, negative, and neutral sentiments. This can provide a clear visual representation of the sentiment distribution.

Confusion Matrix:  to analyze the performance of your model, showing the true positives, true negatives, false positives, and false negatives.

Additional Analysis: charts or plots that analyze the distribution of sentiments over time, or visualize the performance metrics such as precision, recall, and F1 score.

---

# Automated Sentiment Analysis of Ryanair Reviews

## Problem Definition and Objectives

### Problem Clarity
This project focuses on the automated analysis of Ryanair customer reviews to identify the sentiment expressed in them. Given the high volume and variability of reviews, manual analysis is inefficient and error-prone. The goal is to implement a Natural Language Processing (NLP) system that automatically classifies reviews into emotional categories (positive, negative, and neutral) using advanced techniques such as LSTM and BERT. This will provide Ryanair with a clear and accurate understanding of customer perceptions and help identify areas for service improvement.

### Context and Motivation
In the highly competitive aviation industry, customer satisfaction is crucial for airline success. Online reviews provide valuable insights into customer experiences and areas needing improvement. With the growing impact of the low-cost model in Europe, it is vital for Ryanair to understand how its services are perceived to stay competitive. An automated sentiment analysis system will allow Ryanair to respond more quickly and effectively to customer concerns, improving user experience and strengthening brand loyalty.

### Clear and Achievable Objectives
The project aims to achieve the following specific objectives:
- **Sentiment Classification:** Develop a model using LSTM and BERT to classify Ryanair reviews into sentiment categories (positive, negative, neutral).
- **Data Automation:** Automate data extraction by creating a web scraping system compliant with data usage policies.
- **API Deployment:** Deploy an API for real-time sentiment prediction queries.
- **Interactive Dashboards:** Develop dashboards that provide a clear view of key sentiment analysis insights.

### Measurable Goals
- **Model Accuracy:** Achieve 85% accuracy in sentiment classification. LSTM and BERT models have exceeded this target, with BERT reaching 91% and LSTM 86%.
- **Web Scraping Automation:** Implement an efficient scraping process that extracts new reviews monthly.
- **API Performance:** Deploy an API that responds in under 2 seconds.
- **Data Visualization:** Create interactive dashboards to clearly present sentiment analysis results.

### Deployment Mode: Batch Processing
Batch processing is suitable as it does not require continuous data flow. The model will be updated periodically (e.g., monthly).

#### Advantages
- **Simplicity:** Easier to implement and manage for non-real-time data.
- **Cost-Effective:** Lower infrastructure and resource costs.
- **Suitable for Non-Continuous Data:** Ideal for data updated at regular intervals.

#### Disadvantages
- **Latency:** Results are not immediately available, as processing occurs in batches.

## Detailed Infrastructure Documentation

### Required Infrastructure

- **Computational Resources:** Utilize cloud instances for training NLP models. Options include:
  - **Development:** Google Colab
  - **Deployment:** AWS, Azure

- **Storage:** Use storage services to manage data, models, and analysis results:
  - Google Drive
  - AWS S3
  - Azure Blob Storage

- **MLOps Tools:** Implement tools to streamline the ML lifecycle:
  - **Containerization:** Docker
  - **Version Control:** GitHub
  - **CI/CD:** GitHub Actions, GitLab CI/CD, Jenkins
  - **Model Management:** MLflow (for model registration and management)

- **API Services:** Set up a platform for API deployment:
  - FastAPI (for API development and deployment)
  - AWS Lambda
  - Google Cloud Functions
  - Dedicated server

### 1. Orchestration and Pipelines
- Implement orchestration and pipeline management using:
  - Apache Airflow
  - Metaflow
  - Kubeflow
- Use Kubernetes for container orchestration, especially for scalability or distributed deployments.

### 2. Implement MLflow
- Configure MLflow to manage experiments and models.
- Register metrics, artifacts, and models.

### 3. CI/CD
- Develop a robust CI/CD pipeline to automate integration and deployment using:
  - GitHub Actions
  - GitLab CI/CD
  - Jenkins
  - Terraform

### 4. Unit Testing
- Implement unit tests to ensure code quality using pytest.

### 5. Infrastructure as Code (IaC)
- Use Terraform for automated infrastructure management.

### 6. Model Deployment
- Configure batch processing deployment for the model. Consider:
  - Apache Airflow
  - Kubernetes + Kubeflow
  - Apache Spark

### 7. Monitoring and Drift Detection
- Implement monitoring and drift detection mechanisms using:
  - Prometheus
  - Evidently AI
  - Alibi Detect

### 8. Data Versioning
- Use DVC or MLflow for data version control.

### 9. Model Updates and Retraining
- Establish a process for updating and retraining models based on continuous monitoring using:
  - Airflow
  - Kubeflow
  - MLflow

### 10. Post-MLOps Enhancements
- **Add Graphs:** Enhance both `app_lstm` (FastAPI) and the Streamlit interface with visualizations:
  - **Bar Charts:** Display the distribution of positive, negative, and neutral sentiments.
  - **Confusion Matrix:** Analyze model performance with true positives, true negatives, false positives, and false negatives.
  - **Additional Analysis:** Create charts or plots to analyze sentiment distribution over time, and visualize performance metrics such as precision, recall, and F1 score.

### Data Flow Diagram
1. **Data Collection:** Extract data from airquality.com via web scraping.
2. **Preprocessing and Cleaning:** Clean and prepare data for analysis.
3. **Model Training:** Train NLP models using processed data.
4. **Model Evaluation:** Evaluate model accuracy and adjust hyperparameters.
5. **Model Deployment:** Deploy the model in an API for real-time queries.
6. **Monitoring and Maintenance:** Monitor performance and update data as needed.

### Diagram in Detail

1. **Data Collection**
   - **Action:** Extract data from airquality.com via web scraping.
   - **Tools:** Custom scripts or web scraping frameworks.
   
2. **Preprocessing and Cleaning**
   - **Action:** Clean and prepare data for analysis.
   - **Tools:** Python libraries (e.g., Pandas, Numpy).

3. **Model Training**
   - **Action:** Train NLP models using processed data.
   - **Tools:** Python libraries (e.g., TensorFlow, PyTorch), Google Colab for development.

4. **Model Evaluation**
   - **Action:** Evaluate model accuracy and adjust hyperparameters.
   - **Tools:** MLflow for tracking experiments, metrics, and model versions.

5. **Model Deployment**
   - **Action:** Deploy the model in an API for real-time queries.
   - **Tools:** 
     - **API Development:** FastAPI
       - **Deployment Options:** AWS Lambda, Google Cloud Functions, Dedicated server.
     - **Containerization:** Docker for packaging the application and dependencies.

6. **Monitoring and Maintenance**
   - **Action:** Monitor performance and update data as needed.
   - **Tools:** 
     - **Monitoring:** Prometheus for system monitoring.
     - **Drift Detection:** Evidently AI or Alibi Detect for detecting model performance degradation.
   
### MLOps Process Details

1. **Orchestration and Pipelines**
   - **Action:** Implement orchestration and pipeline management.
   - **Tools:**
     - **Orchestration:** Apache Airflow, Metaflow, Kubeflow.
     - **Container Orchestration:** Kubernetes for managing containerized applications.

2. **Implement MLflow**
   - **Action:** Configure MLflow for managing experiments and models.
   - **Tasks:**
     - **Metrics Tracking:** Register metrics.
     - **Artifact Management:** Register artifacts.
     - **Model Management:** Register and version models.

3. **CI/CD**
   - **Action:** Develop a robust CI/CD pipeline to automate integration and deployment.
   - **Tools:**
     - **CI/CD Platforms:** GitHub Actions, GitLab CI/CD, Jenkins.
     - **IaC:** Terraform for automated infrastructure management.

4. **Unit Testing**
   - **Action:** Implement unit tests to ensure code quality.
   - **Tools:** pytest for testing code functionality.

5. **Infrastructure as Code (IaC)**
   - **Action:** Use Terraform for automated infrastructure management.
   - **Tasks:** Define and provision infrastructure resources.

6. **Model Deployment**
   - **Action:** Configure batch processing deployment for the model.
   - **Tools:**
     - **Batch Processing:** Apache Airflow, Kubernetes + Kubeflow, Apache Spark.

7. **Monitoring and Drift Detection**
   - **Action:** Implement monitoring and drift detection mechanisms.
   - **Tools:**
     - **Monitoring:** Prometheus.
     - **Drift Detection:** Evidently AI, Alibi Detect.

8. **Data Versioning**
   - **Action:** Implement a system for versioning data used in training and evaluation.
   - **Tools:** DVC or MLflow.

9. **Model Updates and Retraining**
   - **Action:** Establish a process for updating and retraining models based on continuous monitoring.
   - **Tools:** Airflow, Kubeflow, MLflow.
  
- # Project Management and Technical Implementation

## 2. Experiment and Model Management (15%)

### Experiment Tracking System
- **Tool Usage:** Implement a system using MLflow or another tool to track experiments, metrics, and artifacts.

### Parameter and Metric Logging
- **Detailed Documentation:** Ensure all important parameters and metrics are well-documented.

### Model Versioning
- **Version Control:** Use tools like DVC or MLflow to version models and ensure traceability.

### Model Selection and Promotion Process
- **Clear Process:** Define how to select and promote the best models based on performance metrics.

### Experiment Documentation
- **Clear Reporting:** Document the results and learnings from each experiment clearly.

## 3. ML Orchestration and Pipelines (20%) - Docker, Apache Airflow, or Metaflow

### Design of Reproducible and Scalable Pipelines
- **Tool Usage:** Implement pipelines using tools like Apache Airflow or Metaflow to ensure they are reproducible and scalable.

### Workflow Automation
- **Complete Automation:** Ensure preprocessing, training, and evaluation workflows are fully automated.

### Dependency Management
- **Task Management:** Set up mechanisms to handle dependencies between tasks in pipelines.

### Task Parallelization and Distribution
- **Optimization:** Implement parallelization where possible to improve efficiency.

### Integration with Resource Management Systems
- **Proper Configuration:** Integrate pipelines with resource management systems for effective administration.

## 4. Continuous Integration Including Testing (15%)

### CI/CD Pipeline
- **Automation:** Set up a robust CI/CD pipeline to ensure continuous integration and automated deployment.

### Infrastructure as Code (IaC)
- **Tool Usage:** Use tools like Terraform for infrastructure deployment.

### Automated Testing Execution
- **Unit and Integration Tests:** Implement automated tests to ensure code quality.

### Automation of Training and Evaluation Process
- **Complete Automation:** Ensure training, evaluation, and deployment processes are fully automated.

## 5. Model Deployment (15%) - Docker

### Model Deployment
- **Deployment Mode:** Implement the model using the most suitable mode (batch, online, streaming) based on project needs.

### Prediction Query Examples
- **API Testing:** Provide examples of how to query predictions from the model's API.

### API Documentation
- **Clear Documentation:** Create clear documentation on how to use the model API, including endpoints and parameters.

## 6. Model Monitoring (15%)

### Logging System
- **Robust Implementation:** Ensure an effective logging system to track model performance.

### Alert Configuration
- **Performance Alerts:** Set up alerts to detect any degradation in model performance.

### Drift Detection
- **Continuous Monitoring:** Implement mechanisms to detect data drift and concept drift.

### Key Metrics Dashboards
- **Visualization:** Design dashboards to visualize key metrics and facilitate model performance analysis.

## 7. Additional Aspects

### Use of Real Infrastructure via IaC
- **Complete Automation:** Use IaC to manage infrastructure in an automated manner.

### Identification of Improvement Areas
- **Self-Evaluation:** Identify and document areas for improvement and weaknesses in the implementation.

### Data Versioning
- **Version Control:** Implement versioning for data used in model training and evaluation.

### Model Update and Re-training
- **Update Process:** Establish processes for updating and re-training models based on continuous monitoring.



