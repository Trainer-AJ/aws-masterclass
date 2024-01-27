#!/bin/bash

# This will create s3 buckets in the supplied list of regions
regions=("ap-south-1" "us-east-1" "ap-northeast-1")

echo "Creating S3 buckets in the following regions: ${regions[@]}"

for location in "${regions[@]}"
do
    bucket_name="aws-cli-demo-$RANDOM"
    aws s3 mb s3://$bucket_name --region $location
    echo "Bucket created in $location region: $bucket_name"
done

echo -e "\nHere is the list of all buckets created: \n"
aws s3 ls

# sample output: 
# 2024-01-27 02:01:19 aws-cli-demo-14308
# 2024-01-27 02:01:21 aws-cli-demo-28340
# 2024-01-27 02:01:24 aws-cli-demo-9689