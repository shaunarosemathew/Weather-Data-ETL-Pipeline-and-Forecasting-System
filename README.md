Weather Forecasting ETL Pipeline
Overview

This project demonstrates the implementation of an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, MySQL, and the OpenWeatherMap API. The pipeline automates the process of collecting weather data, cleaning and transforming it into a structured format, and storing it in a MySQL database for further analysis and forecasting.

Features
Extracts real-time weather data from the OpenWeatherMap API.
Transforms JSON data into a structured tabular format using Pandas.
Performs data cleaning and preprocessing.
Loads processed data into a MySQL database.
Implements logging and error handling for reliability.
Supports historical data collection for weather trend analysis and forecasting.
Technologies Used:
Python
Pandas
Requests
MySQL
MySQL Connector
OpenWeatherMap API
ETL Workflow
Extract – Retrieve weather data from the OpenWeatherMap API.
Transform – Clean, validate, and convert the data into a structured format.
Load – Store the processed data in a MySQL database.
Project Structure
extraction.py – Extracts weather data from the API.
transformation.py – Cleans and transforms the extracted data.
load.py – Loads transformed data into MySQL.
weather_data.csv – Processed weather dataset.
etl.log – Log file for tracking ETL operations.
Learning Outcomes
Developed practical experience with ETL processes.
Learned API integration and data extraction techniques.
Gained hands-on experience with MySQL database operations.
Improved skills in data preprocessing, automation, and data engineering.
Author

Developed as a data engineering and analytics project to demonstrate ETL pipeline implementation using Python and MySQL.
