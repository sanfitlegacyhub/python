import boto3
#ec2=boto3.client('ec2',region_name="us-east-1")
ec2_client = boto3.client('ec2', region_name='us-east-1')
#to get list of instances 
response=ec2_client.describe_instances(InstanceIds=[])
#print(ec2list) #it will give the whole list 
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for taglist in instance['Tags']:#data parsing thourgh the tags 
            print(taglist)
            print('====================')

