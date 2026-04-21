import boto3

glue = boto3.client("glue")
sns = boto3.client("sns")

def lambda_handler(event, context):
    # 触发 Glue ETL 任务
    try:
        glue.start_job_run(JobName="demo-data-etl-job")
        return {
            "statusCode": 200,
            "message": "Kafka data pipeline trigger success"
        }
    except Exception as e:
        # 异常 SNS 告警
        sns.publish(
            TopicArn="arn:aws:sns:region:account:data-alert",
            Message=f"ETL Task Failed: {str(e)}"
        )
        raise e
