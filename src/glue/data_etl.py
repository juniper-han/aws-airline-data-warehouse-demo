from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.transforms import *

sc = SparkContext()
glue_context = GlueContext(sc)

# 1. 读取 S3 原始数据
raw_dynamic_frame = glue_context.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://data-lake-demo-bucket/kafka-data/"]},
    format="json"
)

# 2. 数据清洗：过滤空值、标准化字段
clean_frame = raw_dynamic_frame.drop_nulls()

# 3. 写入 Redshift 数仓
glue_context.write_dynamic_frame.from_jdbc_conf(
    frame=clean_frame,
    catalog_connection="redshift-connection-demo",
    connection_options={"dbtable": "data_warehouse.event_fact"},
    redshift_tmp_dir="s3://data-lake-demo-bucket/tmp/"
)

print("Glue ETL Job Finished")
