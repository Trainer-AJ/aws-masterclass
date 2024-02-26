#!/bin/bash
# -----------------------------------------------------
                             # TESTED
# --------------------------------------------------
# List to have Record for Future 
aws s3 ls > bucket_list.txt

# Assuming the list is stored in a file named bucket_list.txt
bucket_list_file="bucket_list.txt"

# Check if the file exists
if [ ! -f "$bucket_list_file" ]; then
    echo "Error: File $bucket_list_file not found."
    exit 1
fi

# Extract bucket names from the third column and use them in a for loop
while read -r line; do
    # Extract bucket name from the third column (assuming space as a delimiter)
    bucket_name=$(echo "$line" | awk '{print $3}')
    
    # Use the bucket name in a for loop
    echo "Processing bucket: $bucket_name"
    aws s3 rm "s3://$bucket_name" --recursive
    aws s3api delete-bucket --bucket "$bucket_name"
    if [ $? -eq 0 ]; then
        echo "Bucket $bucket_name successfully emptied and deleted."
    else
        echo "Error: Failed to delete bucket $bucket_name."
    fi
    
done < "$bucket_list_file"