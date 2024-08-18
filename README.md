# NLP-MLOps-Pipeline
Automated sentiment analysis of Ryanair reviews using NLP and MLOps. Classifies reviews as positive, negative, or neutral with LSTM and BERT models. Includes automated data pipelines, Docker/Kubernetes deployment, CI/CD, and drift detection. Dashboards offer insights into trends and customer feedback.

# Project Status

**Work in Progress**

This project is currently a work in progress, including the README file itself. The details provided here will be updated as the project advances and as tools and technologies are implemented or chosen. Please check back for updates as new information becomes available.

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

## Detailed Infrastructure Documentation

### Required Infrastructure
- **Computational Resources:** Use cloud instances (Google Colab for development, AWS or Azure for deployment) for NLP model training.
- **Storage:** Utilize services like Google Drive, AWS S3, or Azure Blob Storage for storing data, models, and analysis results.
- **MLOps Tools:** Implement Docker for environment containment, GitHub for version control, and CI/CD pipelines for automation.
- **API Services:** Configure a platform for API deployment, such as AWS Lambda, Google Cloud Functions, or a dedicated server.

### Data Flow Diagram
1. **Data Collection:** Extract data from airquality.com via web scraping.
2. **Preprocessing and Cleaning:** Clean and prepare data for analysis.
3. **Model Training:** Train NLP models using processed data.
4. **Model Evaluation:** Evaluate model accuracy and adjust hyperparameters.
5. **Model Deployment:** Deploy the model in an API for real-time queries.
6. **Monitoring and Maintenance:** Monitor performance and update data as needed.

### Deployment Mode: Batch Processing
Batch processing is suitable as it does not require continuous data flow. The model will be updated periodically (e.g., monthly).

#### Advantages
- **Simplicity:** Easier to implement and manage for non-real-time data.
- **Cost-Effective:** Lower infrastructure and resource costs.
- **Suitable for Non-Continuous Data:** Ideal for data updated at regular intervals.

#### Disadvantages
- **Latency:** Results are not immediately available, as processing occurs in batches.

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



