"""
install dotenv then load else shows nothing
loads everything that you specify in .env file
"""
# pip install python-dotenv

import os 
import boto3 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def test_env():
    print(f"All Env detected => {os.getenv("region")}, {os.getenv("min")}")

def s3(): 
    region = os.getenv("region")
    s3 = boto3.client('s3', region_name=region)

    response = s3.list_buckets()
    print(response)

# def lambda_handler(event, context):
test_env()
s3()
