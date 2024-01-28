import boto3# importing bot3 package kind of SDK for AWS
client=boto3.client('ec2')#bot3 i want to use the ec2 instance service 
#data input
instanceID= {"id":'i-0d7ae384c37af610a'}
#business logic
response = client.stop_instances(
    InstanceIds=[
      instanceID['id']#you can give mutiple instances ids for actions
    ],
    # Hibernate=True|False,
    # DryRun=True|False,
    # Force=True|False
)

print(response)