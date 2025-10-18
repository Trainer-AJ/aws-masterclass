# demo-actions-project

**Tested it works -**

```sh
s3_value="mybucket"
sed -i "s|arn:aws:s3:::.*|arn:aws:s3:::$s3_value/*\"|" policy.json

```

## github actions OIDC
<img width="1634" height="676" alt="image" src="https://github.com/user-attachments/assets/3f4f2db0-0e4e-45a1-bb19-6fc40618ec58" />
