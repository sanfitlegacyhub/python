import boto3
#ec2=boto3.client('ec2',region_name="us-east-1")
ec2_client = boto3.client('ec2', region_name='us-east-1')
#to get list of instances 
ec2list=ec2_client.describe_instances(InstanceIds=[])
#print(ec2list) #it will give the whole list 
print(ec2list['Reservations'][0]['Instances'][0]['InstanceId'])
#to get the value of the key  by going level by level 
