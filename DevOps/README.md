# demo-actions-project

**Tested it works -**

```sh
s3_value="mybucket"
sed -i "s|arn:aws:s3:::.*|arn:aws:s3:::$s3_value/*\"|" policy.json

```
