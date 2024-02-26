#!/bin/bash

# ------------------------------------------------
# TESTED 
# _-----------------------------------------------

# Prompt user for folder name
read -p "Enter the folder path (e.g., ~/demo): " folder_path

# Expand tilde in folder path
folder_path=$(eval echo "$folder_path")

# Check if the folder exists
if [ ! -d "$folder_path" ]; then
    echo "Error: The specified folder does not exist."
    exit 1
fi

# Prompt user for S3 bucket name
read -p "Enter the S3 bucket name: " s3_bucket

# Check if the AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it and configure your credentials."
    exit 1
fi

# Upload the entire folder to S3
aws s3 sync "$folder_path" "s3://$s3_bucket"

if [ $? -eq 0 ]; then
    echo "Folder successfully uploaded to S3 bucket: $s3_bucket"
else
    echo "Error: Failed to upload folder to S3 bucket."
    exit 1
fi
