# Technical Component Specification
## Real-Time Messaging
### AWS MSK (Managed Kafka)
Core middleware for high-throughput real-time data ingestion.
Realize traffic peak shaving, system decoupling and asynchronous incremental data transmission.

## Data Lake & Governance
### Amazon S3
Massive object storage as the central data lake for offline logs and semi-structured Kafka data.
### Lake Formation
Unified management of data lake permissions, metadata and access policies to standardize enterprise data governance.

## ETL & Data Integration
### AWS Glue
Fully managed distributed ETL service for data extraction, cleansing and transformation,
connecting S3 data lake and Redshift data warehouse.

## Warehouse & KV Storage
### Amazon Redshift
Enterprise cloud data warehouse for layered modeling, complex SQL query and indicator calculation.
### Amazon DynamoDB
High-performance key-value database for fast lookup of dimension data and system configuration.

## Automation & Orchestration
### AWS Lambda
Serverless event-driven compute for Kafka consumption, scheduled trigger and lightweight automation.
### Step Functions
Visual workflow orchestration to coordinate multiple AWS services with error retry and process control.

## Monitoring & Alerting
### CloudWatch
Full-link observability for logs, metrics and pipeline latency to ensure data stability.
### Amazon SNS
Unified notification service, providing real-time alerts for task failure, data delay and system exceptions.
