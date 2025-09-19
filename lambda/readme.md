## Pre-Req
1. Secrets manager
2. S3 bucket with reports folder in it
3. IAM roles to lambda
4. 15 sec timeout
5. env vars:
   
| **Key**           | **Value**                    |
|-------------------|------------------------------|
| S3_BUCKET_NAME     | just-ec2-transfer-777        |
| S3_OBJECT_KEY      | reports/manager.csv          |
| region_name        | ap-south-1                   |
| secret_name        | azure-app-credentials        |
