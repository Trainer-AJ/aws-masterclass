# Sign in to aws

1. configure aws 

```powershell
aws configure 
```

2. test connection :

```powershell
aws s3 mb s3://your-unique-bucket-name
```
3. Get help 
1. 
 ```azurepowershell
aws service name help

aws iam help
```

```powershell
aws iam list users

aws iam list-users --query 'Users[*].[UserName]'

```

sample output:
```powershell
[
    [
        "admin"
    ],
    [
        "aws_cli"
    ],
    [
        "mgn-install"
    ],
    [
        "migration-discovery"
    ]
]
```