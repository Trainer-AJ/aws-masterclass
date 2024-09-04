# pip install python-dotenv

import os 
import boto3 
# from dotenv import load_dotenv, dotenv_values

# load_dotenv()

def test_env():
    print(f"All Env detected => {os.getenv("region")}, {os.getenv("min")}")

def s3(): 
    region = os.getenv("region")
    s3 = boto3.client('s3', region_name=region)

    response = s3.list_buckets()

# Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f' Found Bucket ==> {bucket["Name"]}')

def asg():
    region = os.getenv("region")
    asg = boto3.client('autoscaling', region_name=region)
    response = asg.update_auto_scaling_group(
        AutoScalingGroupName=os.getenv('asg_name'),
        MinSize=int(os.getenv('min')),
        DesiredCapacity=int(os.getenv('desired')),
        MaxSize=int(os.getenv('max'))
    )
    print(response)


def lambda_handler(event, context):
    test_env()
    # s3()
    asg()
