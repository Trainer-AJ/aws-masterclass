import boto3 

REGION = 'ap-south-1'

# THIS SCRIPT RETURNS ID of RUNNING Ec2 Instances 
def running_ec2(REGION):
    # connect to ec2 service of that region
    ec2 = boto3.client('ec2', region_name=REGION)

    # All Running instances 
    response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ]
    )

    # print(response)
    """
    Response format:
    {'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-0e670eb768a5fc3d4', 'InstanceId': 'i-0471871927c317b1a', 'InstanceType': 't2.micro', 'KeyName': '1-feb-24',
    """

# Extract ID of Instnaces
# beacuse the response is in the Dict Reservations so,
    ID = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ID.append(instance['InstanceId'])
    return ID


running_ec2(REGION)
print(running_ec2(REGION))

EC2_2_Stop = running_ec2(REGION)

def ec2_stop(EC2_2_Stop):
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.stop_instances(
    InstanceIds=EC2_2_Stop)
    print('*'*50)
    print(f'STopped Your Ec2 with ID: {EC2_2_Stop}')
    print('*'*50)

ec2_stop(EC2_2_Stop)
