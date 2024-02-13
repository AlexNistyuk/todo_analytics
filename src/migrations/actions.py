async def create_actions_table(dynamodb):
    table_name = "actions"
    key_schema = [
        {"AttributeName": "id", "KeyType": "HASH"},
    ]
    attribute_definitions = [
        {"AttributeName": "id", "AttributeType": "S"},
    ]

    provisioned_throughput = {"ReadCapacityUnits": 10, "WriteCapacityUnits": 10}

    try:
        await dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput,
        )
    except Exception:
        ...
