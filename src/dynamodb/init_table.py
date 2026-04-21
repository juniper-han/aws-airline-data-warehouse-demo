import boto3

dynamodb = boto3.client("dynamodb")

def create_dim_table():
    """初始化维度配置表"""
    response = dynamodb.create_table(
        TableName="user_dim_config",
        KeySchema=[{"AttributeName": "user_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "user_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
    )
    print("DynamoDB dimension table created")

if __name__ == "__main__":
    create_dim_table()
