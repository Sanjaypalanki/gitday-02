import boto3

# Create EC2 client
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Change region if needed

# Launch instance
instances = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (us-east-1)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair-name',  # Replace with your actual key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyFirstEC2'}]
        }
    ]
)

print("Launched instance with ID:", instances[0].id)

