# Data Modeling Design Document
## Design Principles
1. Layered architecture: Standard three-tier warehouse including ODS, DWD and DWS
2. Dimensional modeling: Star schema for multi-dimensional analysis scenarios
3. Unified standard: Consistent metrics and dimension logic for stream and batch jobs
4. Cloud optimization: Balance query performance and storage cost for cloud data warehouse

## Data Warehouse Layers
### ODS Layer
Store raw logs and original Kafka data, retain full fields for data tracing and backfill.
### DWD Layer
Complete data cleansing, format unification and null filtering, retain detailed business records and basic dimension information.
### DWS Layer
Aggregate indicators by multiple dimensions, reduce repeated calculation and accelerate analysis.

## Table Design
### Event Fact Table
Store business behavior and event details, sourced from MSK real-time streaming and offline batch data.
### Dimension Table
Cover user, region and device reference data.
Dual storage design: DynamoDB for low-latency query, Redshift for offline analysis.

## Data Quality Standards
1. Primary key constraint to avoid duplicate data
2. Unified timestamp format to align stream and batch data
3. Mandatory validation for core fields and invalid data isolation
4. Data lifecycle management for cold-hot tiered storage and cost control
