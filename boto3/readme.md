# Python basics - 
- [logging python](https://docs.python.org/3/howto/logging.html)
- [use cryptography to store passwords in db](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_modules_of_cryptography.htm)

### [Other Real World Boto3 that checks billing](../utility/readme.md)
# boto3 docs - 
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#passing-credentials-as-parameters
```py
import boto3

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
)
```
