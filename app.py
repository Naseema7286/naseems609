import boto3

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace 'us-east-1' with your preferred region

# Specify parameters for the new EC2 instance
instance_params = {
    'ImageId': 'ami-0abcdef1234567890',  # Replace with the appropriate AMI ID for your region
    'InstanceType': 't2.micro',  # Instance type
    'MinCount': 1,  # Minimum number of instances to launch
    'MaxCount': 1,  # Maximum number of instances to launch
    'KeyName': 'your-key-pair-name',  # Replace with your key pair name
    'SecurityGroupIds': ['sg-0123456789abcdef0'],  # Replace with your security group ID
    'SubnetId': 'subnet-0123456789abcdef0',  # Replace with your subnet ID (optional)
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyEC2Instance'}
            ]
        }
    ]
}

# Launch the EC2 instance
try:
    response = ec2.run_instances(**instance_params)
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 Instance created with ID: {instance_id}")
except Exception as e:
    print(f"Failed to create EC2 instance: {e}")

