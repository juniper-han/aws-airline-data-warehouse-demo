import json
import boto3
from kafka import KafkaConsumer

# 初始化 S3
s3 = boto3.client("s3")
bucket_name = "data-lake-demo-bucket"

consumer = KafkaConsumer(
    "real-time-event-topic",
    bootstrap_servers=["msk-broker-endpoint:9092"],
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

def save_to_s3(data):
    """Kafka 数据落地 S3 数据湖"""
    file_key = f"kafka-data/{data['event_time'].split(' ')[0]}/{data['user_id']}.json"
    s3.put_object(
        Bucket=bucket_name,
        Key=file_key,
        Body=json.dumps(data)
    )

if __name__ == "__main__":
    for msg in consumer:
        event_data = msg.value
        save_to_s3(event_data)
        print(f"Consume & Save to S3: {event_data}")
