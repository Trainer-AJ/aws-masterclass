import boto3

# Set the region
region = 'ap-south-1'

# Initialize the S3 client
s3_client = boto3.client('s3', region_name=region)

def list_buckets():
    response = s3_client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

def empty_bucket(bucket_name):
    # List objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    # Check if the bucket is empty
    if 'Contents' not in response:
        return
    
    # Delete all objects in the bucket
    objects = [{'Key': obj['Key']} for obj in response['Contents']]
    s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
    
    # If the bucket still has more objects (pagination), repeat the process
    while response.get('IsTruncated'):  # Check if there are more objects to delete
        response = s3_client.list_objects_v2(Bucket=bucket_name, ContinuationToken=response['NextContinuationToken'])
        objects = [{'Key': obj['Key']} for obj in response['Contents']]
        s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})

def delete_bucket(bucket_name):
    empty_bucket(bucket_name)
    s3_client.delete_bucket(Bucket=bucket_name)

def main():
    # List all buckets
    buckets = list_buckets()
    
    # Filter buckets based on the region if necessary
    for bucket in buckets:
        print(f"Processing bucket: {bucket}")
        delete_bucket(bucket)
        print(f"Deleted bucket: {bucket}")

if __name__ == "__main__":
    main()
