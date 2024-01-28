import boto3
def stop_ec2_instance(instance_id):
    try:
        # Create an EC2 client
        ec2_client = boto3.client('ec2')

        # Stop the EC2 instance
        response = ec2_client.stop_instances(InstanceIds=[instance_id])

        # Print the response
        print(f"EC2 instance {instance_id} is stopping. Response: {response}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your-instance-id' with the actual ID of your EC2 instance
instance_id_to_stop = 'i-0d7ae384c37af610a'

stop_ec2_instance(instance_id_to_stop)