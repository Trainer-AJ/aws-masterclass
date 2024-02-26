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
# Query Results
`listname.attribute` = Formula

1.
```json
   aws ec2 describe-volumes --query 'Volumes[*].VolumeId'

[
    {
        "Attachments": [],
        "AvailabilityZone": "ap-south-1a",
        "CreateTime": "2024-02-25T14:46:37.236000+00:00",
        "Encrypted": false,
        "Size": 100,
        "SnapshotId": "",
        "State": "available",
        "VolumeId": "vol-0a366725c631d6275",
        "Iops": 3000,
        "VolumeType": "gp3",
        "MultiAttachEnabled": false,
        "Throughput": 125
    }
]

aws ec2 describe-volumes --query 'Volumes[*].VolumeId' --output text
```
2. for a Particular value `listname[number]`
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
# Linux with CLI
The `xargs` command in Linux is used to build and execute command lines from standard input. It reads data from standard input (stdin) or pipes, and executes the command (default is `/bin/echo`) one or more times based on the input read. Here's what the options `-otl` mean:

- `-o, --open-tty`: This option opens a new terminal (TTY) for each command execution. This is particularly useful if you're running commands that might require interaction or if you want to separate the output of each command into different terminals.
- `-t, --verbose`: This option prints the command line on the standard error output before executing it. It's useful for debugging purposes or if you want to see the commands that `xargs` is going to execute.
- `-l, --max-lines[=max-lines]`: This option limits the number of arguments taken from standard input for each command line to execute. If `max-lines` is not specified, it defaults to 1. It ensures that each command executed by `xargs` contains a certain number of arguments at most, which can be helpful when dealing with commands that have argument count limitations.

Here's a simple example of how `xargs -otl` might be used:

```bash
# Suppose you have a list of files and you want to print them with ls in a separate terminal for each file
echo "file1 file2 file3" | xargs -otl ls
```

This would open a new terminal for each file (`-o`), print the command to be executed (`ls`), and list (`ls`) the contents of each file in separate terminals.
