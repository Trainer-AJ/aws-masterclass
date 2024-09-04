[Retrieving Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-retrieve.html)

```py
import os
  region = os.environ['AWS_REGION']
```

- there are few by deafult vars - 
- AWS_DEFAULT_REGION – The default AWS Region where the Lambda function is executed.

- AWS_REGION – The AWS Region where the Lambda function is executed. If defined, this value overrides the AWS_DEFAULT_REGION.

## Env Vars: 
- the env you specify in lambda console auto reachable to function :) 
![image](https://github.com/user-attachments/assets/a8cd2c62-d21a-4111-b85b-8d2cfc2a5b01)

## Success msg after update: 
![image](https://github.com/user-attachments/assets/da3e5c26-0067-4fb0-a2f8-b789a7d0305e)


