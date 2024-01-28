import boto3

def list_instance_ids():
    try:
        # Create an EC2 client
        ec2 = boto3.client('ec2')

        # Describe EC2 instances
        response = ec2.describe_instances()

        # Display instance IDs one by one
        for reservation in response['Reservations']:#outer loop travers , one reservation may has n number of instances disct
            for instance in reservation['Instances']:#inner loop for instannces 
                instance_id = instance['InstanceId']#fetch the ID of instances 
                print(f"Instance ID: {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])#to stop the instances whichever runnning 

    except Exception as e:
        print(f"An error occurred: {str(e)}")#throw an actual error accoure in console

# Call the function to list EC2 instance IDs
list_instance_ids()