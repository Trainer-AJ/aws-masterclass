#!/bin/bash

read -p "Enter Number of buckets to create : " num
if [$num == ""]; then
    echo -e " ************** This Creates $(($num+1)) s3 buckets *************************"
else
    echo "Type 'del' to delete newly created buckets"

if [ "$1" = "del" ]; then
    buckets=$(aws s3 ls | awk '{print $3}' | grep -i "this-cli-demo")

    # Iterate through each bucket and delete it
    for bucket in $buckets; do
        aws s3 rb "s3://$bucket" --force
    done
else
    for ((i=0; i<=$num; i++)); do
        aws s3 mb s3://this-cli-demo-$i
    done

    # List all buckets
    aws s3 ls | awk '{print $3}'
fi

