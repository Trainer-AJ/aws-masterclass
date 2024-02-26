# boto3 is  uild on top of botocore 
# https://botocore.amazonaws.com/v1/documentation/api/latest/tutorial/index.html

import boto3
# credentials and Auth type = https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
# aws cli supplied username and password via access key 

# boto3 session = 
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#module-boto3.session

# --------------------- visit aws management console -----------------------------
aws_console = boto3.session.Session(profile_name="default")

aws_management_console = boto3.session.Session(profile_name="default")
# ----------------- high level api ----------------------------
iam_console_resource = aws_management_console.resource('iam') 

for each_user in iam_console_resource.users.all():
    print(each_user.name)

# dir(aws_management_console)
# print(aws_management_console.get_available_resources())

# ---------------------------- Open IAM Console (low level) ------------------------------------------
# gives out dict and more control
iam_console = aws_console.client(service_name="iam")

# open window
result = iam_console.list_users()

print("Original Response: ", type(result))
print(result)

for each_user in result['Users']:
    print(each_user['UserName'])

# check this - https://docs.google.com/document/u/0/d/1-34IR_hz1ngwLWET9t5XSwOWEPULcDByQTp0buqJvqk/mobilebasic?pli=1