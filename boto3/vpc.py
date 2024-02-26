import boto3

# below creates vpc in aws configure commands default region
# without print gives NO OUTPUT
# not like terraform, you change CIDR creates new vpc


def list_vpc():
    mumbai_vpc_client = boto3.client('ec2', region_name='ap-south-1')
    response = mumbai_vpc_client.describe_vpcs()
    vpcs = response['Vpcs']

    # Print VPC details
    for vpc in vpcs:
        print("VPC ID:", vpc['VpcId'])

def create_vpc():
    vpc = boto3.client('ec2')
    response = vpc.create_vpc(
        CidrBlock='10.16.0.0/16',
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Python-VPC-2'
                    },
                ]
            },
        ]
    )
# a = {'vpc': {'name': 'value', 'id': 97966}, 'owner': 'AJ'}
# a['vpc']['id']
    print(response['Vpc']['VpcId'])

# create_vpc()
list_vpc()