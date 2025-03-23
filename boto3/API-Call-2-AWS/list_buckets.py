import os
import requests
from signing import create_headers
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

# Load environment variables from the .env file
load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# AWS S3 service endpoint
service = 's3'
host = 's3.amazonaws.com'
region = 'us-east-1'
endpoint = '/'
method = 'GET'

# Load AWS credentials from environment variables
# access_key = os.environ['AWS_ACCESS_KEY_ID']
# secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
# #session_token = os.environ['AWS_SESSION_TOKEN']

# Create headers and signature for the request
#headers, amzdate = create_headers(method, endpoint, service, host, region, access_key, secret_key, session_token)
headers, amzdate = create_headers(method, endpoint, service, host, region, access_key, secret_key)

# Make the request to list S3 buckets
request_url = 'https://' + host + endpoint
response = requests.get(request_url, headers=headers, timeout=5)

print(f"Response Status Code: {response.status_code}")
print(f"Response Body: {response.text}")

# If there's an error, it will raise the HTTPError, which you can catch
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Response Body: {response.text}")

# Check for successful response
response.raise_for_status()

# Parse and print the list of S3 buckets (response text contains XML)
print("List of S3 Buckets:")
print(f"{response.text}\n")

# ===================== Extra ============================
xml_data = response.text
# Parse the XML
root = ET.fromstring(xml_data)

# Define the namespace
namespace = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}

# Get Owner details
owner = root.find('s3:Owner', namespace)
owner_id = owner.find('s3:ID', namespace).text
owner_display_name = owner.find('s3:DisplayName', namespace).text

# Print Owner info
print(f"Owner ID: {owner_id}")
print(f"Owner Display Name: {owner_display_name}")

# Get Bucket details
buckets = root.findall('s3:Buckets/s3:Bucket', namespace)

# Print Bucket info
print("\nList of S3 Buckets:")
for bucket in buckets:
    bucket_name = bucket.find('s3:Name', namespace).text
    creation_date = bucket.find('s3:CreationDate', namespace).text
    print(f"- {bucket_name} \n (Created on: {creation_date})")