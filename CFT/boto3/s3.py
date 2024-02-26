import logging
import boto3
from botocore.exceptions import ClientError
# Let's use Amazon S3
s3 = boto3.resource('s3')

bucket_name = input("Please Enter Bucket Name: ")

region = input("Please Enter Region Name: ")

def create_bucket(bucket_name, region):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f' Found Bucket ==> {bucket["Name"]}')

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

# # Upload a new file
# with open('test.jpg', 'rb') as data:
#     s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)