import boto3 

def lambda_handler(event, context):
    REGION = 'ap-south-1'

    # connect to ec2 service of that region
    ec2 = boto3.client('ec2', region_name=REGION)

    # All Running instances 
    ID = []
    paginator = ec2.get_paginator('describe_instances')
    for response in paginator.paginate(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                ID.append(instance['InstanceId'])

    if ID:
        ec2.stop_instances(InstanceIds=ID)
        print('*' * 50)
        print(f'Stopped Your Ec2 with IDs: {", ".join(ID)}')
        print('*' * 50)
    else:
        print("No running instances found.")
