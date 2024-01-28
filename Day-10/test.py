import boto3
ddb = boto3.client('dynamodb')
print(ddb.describe_limits())
