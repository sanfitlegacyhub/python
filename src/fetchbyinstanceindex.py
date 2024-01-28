import boto3

def get_instance_id_by_index(index):
    try:
        # Create an EC2 client
        ec2 = boto3.client('ec2')

        # Describe EC2 instances
        response = ec2.describe_instances()

        # Access the EC2 instance by index
        instance_count = 0
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_count += 1

                # Check if the current instance is the one you want
                if instance_count == index:
                    instance_id = instance['InstanceId']
                    return instance_id

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None  # Return None in case of an error

# Specify the index of the instance you want to retrieve
#index_to_retrieve = 2

# Get the instance ID by index
instance_id = get_instance_id_by_index(2)

# Print the result
if instance_id:
    print(f"Instance ID at index {2}: {instance_id}")
else:
    print("Failed to retrieve instance ID.")
