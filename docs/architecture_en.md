# Overall Architecture Design
## Project Overview
This solution delivers a stream-batch unified data lakehouse system based on AWS cloud services and Apache Kafka (AWS MSK).
It implements the full data pipeline including real-time message queuing, data lake storage, ETL integration, data warehouse modeling, workflow orchestration, automated operation, monitoring and alerting.

## Technical Components
### Real-Time Layer
- AWS MSK (Managed Kafka): Real-time event ingestion, message buffering and system decoupling
- Lambda: Event-driven data consumption and automated integration

### Data Lake Layer
- Amazon S3: Central storage for offline files and real-time incremental data
- Lake Formation: Data access control, metadata management and resource isolation

### Data Integration Layer
- AWS Glue: Fully managed ETL for data cleansing, transformation and batch scheduling

### Data Warehouse Layer
- Amazon Redshift: Cloud data warehouse for layered modeling and analytical query
- Amazon DynamoDB: Low-latency storage for dimension data and configuration

### Orchestration & Monitoring
- Step Functions: Visual workflow orchestration for multi-task collaboration
- CloudWatch: Full-link metrics, log aggregation and latency monitoring
- SNS: Exception notification and operational alerting

## Core Data Flow
1. Real-time business events are produced into AWS MSK Kafka topics.
2. Streaming data is consumed and persisted into Amazon S3 data lake.
3. Lake Formation manages cross-service permission and metadata governance.
4. AWS Glue standardizes data format and filters invalid records.
5. Processed data is ingested into Redshift with layered warehouse rules.
6. Dimension data from DynamoDB is joined to enrich business information.
7. Step Functions automates end-to-end pipeline scheduling.
8. CloudWatch monitors pipeline health, while SNS delivers alerts for anomalies.

## Architecture Highlights
1. Stream-batch unified architecture for consistent data caliber
2. Cloud-native managed services to reduce maintenance costs
3. Loosely coupled modules for independent scaling and iteration
4. Built on AWS Free Tier, easy to verify locally and migrate to production
