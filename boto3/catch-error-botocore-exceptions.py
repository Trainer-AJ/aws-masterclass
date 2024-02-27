import boto3
import botocore.exceptions # boto3 lib to catch aws errors

# INPUTS
print('*' * 50, 'Bucket name should be [GLOBALLY UNIQUE] and [WITHOUT CAPS]', '*' * 50, sep='\n')
NAME = input("Enter Bucket name please: ")
REGION = input("Enter Bucket Region Please: ")

def create_bucket(NAME, REGION):
    s3 = boto3.client('s3', region_name=REGION)

    # set region
    location_constraint = {'LocationConstraint': REGION} 
    try:
        response = s3.create_bucket(
            Bucket=NAME,
            CreateBucketConfiguration=location_constraint
        )
        if response["ResponseMetadata"]['HTTPStatusCode'] == 200:
            print("Bucket created successfully:", response['Location'])

            # Capturing common errors: 
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'InvalidBucketName':
            print("🚫🚫🚫🚫")
            print("Invalid bucket name provided:", NAME)
        else:
            raise error

    except botocore.exceptions.InvalidRegionError:
        print("🚫🚫🚫🚫")
        print("Use Valid Region!!")

    except (botocore.exceptions.EndpointConnectionError) as region_error:
        raise region_error
        print("🚫🚫🚫🚫")
        print("Please provide a Valid Region Name !!!", REGION, 'is not VALID')
        print(region_error)

create_bucket(NAME, REGION)
