### [AWS CCP Practice Questions GitHub Repo](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-1.md)

# utlilty Folder 
- Tested sscript to empty and dlete all buckets 
- other one that check If any such resource running that caused bill in past 
aws s3 ls | awk '{print $3}'

# AWS Production
- AWS Org setup : 1 aws account for security team : IAM identity center + Security hub /// 2nd for sandbox /// 3rd for Prod /// 4th Dev (lower) env etc
- **real world use case**: Need to send billing for Amazon Q use to Managers. List of 65k total users in azure 183 total in azure all of them have Q license, we just need to send bills to those users manager
  1. scan those users from AWS Identity center
  2. fetch their manager name from entra ID // email is forgein key (Vertical Delivery heads -- like Bhatt >> Goyal >> Arshi => send bill to Arshi )
  3. once csv done store in s3
  4. lambda in another aws account // Identity center in another 
