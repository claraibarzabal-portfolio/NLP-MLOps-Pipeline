-- init.sql
CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;

