📊 YouTube ETL Pipeline & Analytics Dashboard

An end-to-end cloud-based data engineering project designed to process, transform, and analyze YouTube trending video data at scale. This pipeline ingests raw data, applies ETL transformations, optimizes it for analytics, and presents insights through an interactive Streamlit dashboard.

🚀 Project Overview

This project automates the extraction and analysis of large volumes of YouTube trending data across multiple regions and categories. The goal is to create a scalable, production-style data pipeline and visualize meaningful insights such as engagement trends, category performance, and top videos.

🏗️ Architecture Summary
1️⃣ Data Ingestion

Raw YouTube trending datasets stored in AWS S3 (Raw Layer)

AWS Lambda used to automate ingestion and trigger downstream ETL jobs

2️⃣ ETL Processing

AWS Glue + PySpark used for cleaning, transforming, and standardizing raw data

Data enriched with computed fields and converted into Parquet format

Data lake structured into:

Raw Layer

Clean Layer

Analytics Layer (gold layer)

3️⃣ Data Optimization

Hive-style partitioning by:

region

category_id

Improves query speed and reduces scanning cost

4️⃣ Querying & Validation

AWS Athena used to query Analytics Layer using SQL

Ensures transformed datasets are accurate and analytics-ready

5️⃣ Interactive Dashboard

A multi-page Streamlit Dashboard built to visualize:

Top trending videos

Category-wise insights

Regional patterns

Engagement metrics (views, likes, comments)

Tag cloud analysis

🛠️ Tech Stack
Data Engineering

Python

PySpark

AWS Glue

AWS Lambda

AWS Athena

ETL Pipeline Development

Parquet + Hive Partitioning

Cloud Services

AWS S3

IAM (access control & security)

S3 Data Lake Architecture

Dashboard & Visualization

Streamlit

Plotly

WordCloud

Other Skills

SQL

Data Cleaning & Transformation

Exploratory Data Analysis (EDA)

📁 Project Structure
📦 youtube-etl-dashboard
 ┣ 📂 pages/
 ┃ ┣ 1_🏠_Home.py
 ┃ ┣ 2_📺_Top_Videos.py
 ┃ ┣ 3_📚_Category_Insights.py
 ┃ ┣ 4_🌍_Region_Insights.py
 ┃ ┣ 5_📈_Channel_Leaderboard.py
 ┃ ┗ 6_🏷_Tag_Analysis.py
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md

📊 Key Features

Automated ingestion with AWS Lambda

Scalable ETL processing with Glue + PySpark

Multi-layered S3 data lake (Raw → Clean → Analytics)

Optimized storage using Parquet + partitioning

Analytics-ready querying with Athena

Fully interactive Streamlit dashboard

Clear visual insights across regions, categories, and engagement metrics

🚀 Future Enhancements

Add Airflow or Step Functions orchestration

Add real-time ingestion with Kinesis

Add ML-based prediction (video virality forecasting)

Integrate authentication for dashboard access

🤝 Contributions

Contributions, suggestions, and improvements are welcome!
