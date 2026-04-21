import json
import time
import random
from kafka import KafkaProducer

# AWS MSK 配置
producer = KafkaProducer(
    bootstrap_servers=["msk-broker-endpoint:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

def generate_real_time_data():
    """模拟实时业务事件数据"""
    return {
        "user_id": f"user_{random.randint(1000, 9999)}",
        "event_name": random.choice(["page_view", "click", "search", "order"]),
        "event_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "device_type": random.choice(["mobile", "pc", "pad"])
    }

if __name__ == "__main__":
    topic_name = "real-time-event-topic"
    while True:
        data = generate_real_time_data()
        producer.send(topic_name, value=data)
        print(f"Send Kafka Data: {data}")
        time.sleep(1)
