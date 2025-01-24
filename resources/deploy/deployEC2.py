import boto3
import time
import paramiko

# AWS configuration - Windows
REGION = 'us-east-1'  # Your region
KEY_NAME = 'key'  # Your EC2 key pair name
AMI_ID = 'ami-0001e312b82212f65'  # Example Windows AMI ID for us-east-1
INSTANCE_TYPE = 't2.micro'  # Your instance type
SECURITY_GROUP = 'sg-xxxxxxxxxxxxxxxxx'  # Your EC2 security group ID
SUBNET_ID = 'subnet-xxxxxxxxxxxxxxxxx'  # Your EC2 subnet ID

ec2 = boto3.client('ec2', region_name=REGION)

# Launch EC2 instance
response = ec2.run_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    MinCount=1,
    MaxCount=1,
    KeyName=KEY_NAME,
    SecurityGroupIds=[SECURITY_GROUP],
    SubnetId=SUBNET_ID,
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'LibraryAPIInstance'}]
    }]
)

instance_id = response['Instances'][0]['InstanceId']
print(f'Launching EC2 instance with ID: {instance_id}')

# Wait for the instance to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Get the public IP address of the instance
instance = ec2.describe_instances(InstanceIds=[instance_id])
public_ip = instance['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(f'Instance is running. Public IP: {public_ip}')

# Wait for a few seconds to allow instance to initialize
print(f'Wait 60 seconds before connecting')
time.sleep(60)  # Wait 60 seconds before connecting

# Set up SSH connection using Paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Update the key file path to Windows style
key_file_path = r'C:\Develop\backend-coding-challenge-library-api\resources\deploy\key.ppk'
print(f"Connecting to {public_ip}...")
ssh.connect(public_ip, username='ec2-user', key_filename=key_file_path)
print("SSH connection successful.")

# Use SFTP to transfer files
sftp = ssh.open_sftp()
print("SFTP connection established.")

# Define local and remote file paths
local_file = r'C:\Develop\backend-coding-challenge-library-api\resources\deploy\library.zip'
remote_file = '/home/ec2-user/library_api.zip'  # Linux path

# Upload the file
sftp.put(local_file, remote_file)
print(f"File uploaded to {remote_file}")

# Close the SFTP connection
sftp.close()

# Commands to extract and run the application on Linux
commands = [
    # Install necessary packages for Amazon Linux
    'sudo yum update -y',
    'sudo yum install -y python3 python3-pip unzip',

    # Unzip the library.zip file
    'unzip /home/ec2-user/library_api.zip -d /home/ec2-user/library_api',

    # Install required Python dependencies with error handling
    'cd /home/ec2-user/library_api && pip3 install -r requirements.txt || { echo "pip install failed"; exit 1; }',

    # Run the application in the background
    'cd /home/ec2-user/library_api && python3 main.py &'
]

# Execute the commands
for cmd in commands:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

print('Deployment complete! The API is now running on the Windows EC2 instance.')

# Close the SSH connection
ssh.close()