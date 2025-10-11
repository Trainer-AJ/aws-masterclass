The video you provided, **"Day 13 | Top 15 AWS Services that Every DevOps Engineers should learn | #aws #devops,"** is part of a 45-day DevOps course. The main objective is to identify the critical AWS services that a DevOps engineer must master to improve automation and efficiency.

Here are the key points, facts, and examples shared in the video:

---

### **Key Concepts & Foundation**
* **DevOps Focus on AWS [02:45]:** While AWS offers over 200 services, a DevOps engineer only needs to focus on those related to their core roles: Automation and Efficiency [03:33].
* **AWS as a Service Provider [00:54]:** AWS is a cloud provider offering Platform as a Service (PaaS) and Infrastructure as a Service (IaaS). It simplifies complex tasks by providing them as managed services.  
  * **Example:** Instead of manually installing and managing Kubernetes, AWS provides it as a service (EKS), handling the underlying maintenance [01:20].

---

### **Top 15 AWS Services for DevOps Engineers**
The video details the following 15 essential AWS services:

| No. | Service | Key Functionality & Facts | Example/Use Case | Timestamp |
|---|---|---|---|---|
| 1. | **EC2 (Elastic Compute Cloud)** | The fundamental compute service for deploying applications and live projects. | Deploying a web application or a dynamic application [04:33]. | [04:24] |
| 2. | **VPC (Virtual Private Cloud)** | Essential for securing EC2 instances and all your AWS resources. Involves components like security groups, subnet ranges (CIDR blocks), and traffic rules (inbound/outbound) [05:33]. | Ensuring your EC2 instances are secured within a private network. | [05:12] |
| 3. | **EBS (Elastic Block Store) / Volumes** | Provides block storage volumes to attach to EC2 instances, used for persistent data storage. Supports snapshots and backups. | Storing data for a database or an application that continuously creates files [07:28]. | [06:52] |
| 4. | **S3 (Simple Storage Service) Buckets** | A widely used, cheap, and extendable object storage service. It is now encrypted by default by AWS [09:26]. | Storing files, Excel sheets, or humongous data that an application needs to read or write [08:10]. | [08:01] |
| 5. | **IAM (Identity and Access Management)** | A critical component for security that manages permissions (roles and policies) for users (developers, QA) and AWS services. | Granting a QA engineer only read access to a GitHub repository, while developers have write access [11:11]. | [10:28] |
| 6. | **CloudWatch** | The primary monitoring and observability service that keeps track of every action and event taking place on your AWS environment. | Triggering a notification when an EC2 instance reaches a specific CPU threshold [16:42]. | [12:46] |
| 7. | **Lambda Functions** | A serverless compute service used for executing short-lived actions or functionalities. It automatically provisions, runs the code, and tears down the instance. | Correlated with CloudWatch: Sending a mail notification or automatically encrypting an EBS volume when CloudWatch detects an unencrypted volume [15:09]. | [15:35] |
| 8. | **AWS CodePipeline** | A CI/CD service similar to a Jenkins pipeline for modeling and automating the release process. | Defining the flow for continuous integration and delivery [21:18]. | [20:24] |
| 9. | **AWS CodeBuild** | A fully managed build service that compiles source code, runs tests, and produces software packages (artifacts). | Taking the code and compiling it into a usable artifact, like a JAR or WAR file [21:45]. | [20:35] |
| 10. | **AWS CodeDeploy** | Automates software deployments to various compute services like EC2, AWS Fargate, AWS Lambda, or on-premises servers. | Deploying a built WAR file artifact onto an EC2 instance [22:32]. | [21:51] |
| 11. | **AWS Config (Configuration Service)** | A guardrail service that monitors and records your AWS resource configurations to ensure compliance. | Monitoring for the creation of unencrypted EBS volumes or S3 buckets without versioning [24:43]. | [24:43] |
| 12. | **Billing and Costing** | Services that provide detailed information on organizational spending across various AWS resources. | Reviewing how much the organization has spent on S3 or EC2 instances in the last 30 or 90 days [25:50]. | [25:30] |
| 13. | **AWS KMS (Key Management Service)** | A managed service that makes it easy to create and control encryption keys used to encrypt your data. | Storing and managing keys, secrets, and certificates required for encrypting S3 buckets or EBS volumes [27:10]. | [26:24] |
| 14. | **CloudTrail** | Used for operational and risk auditing. It records and preserves logs of all API activities/actions that occur in your AWS account for a specific duration. | Auditing the activities of a developer or retrieving logs of an API action from six months ago [28:19]. | [28:12] |
| 15. | **EKS (Elastic Kubernetes Service)** | A fully managed Kubernetes service provided by AWS. Requires a good foundational knowledge of on-premises Kubernetes [30:24]. | Running containerized applications using a managed Kubernetes solution. | [30:05] |

---

### **Additional Container and Logging Services**
* **Fargate [31:16]:** A serverless compute engine for containers that can be used without Kubernetes.  
* **ECS (Elastic Container Service) [31:21]:** AWS's proprietary container orchestration solution.  
  * **EKS vs. ECS [31:44]:** EKS is a managed version of the open-source Kubernetes, while ECS is an AWS proprietary container orchestration solution.  
* **ELK Stack (Elasticsearch, Logstash, Kibana) [32:20]:** An efficient logging and search mechanism. Elasticsearch is key for collecting and querying logs from microservices to identify errors and common practices over a long period. | [32:20] |

---

**You can watch the video here:**  
🔗 [http://www.youtube.com/watch?v=leWJypzVyQ4](http://www.youtube.com/watch?v=leWJypzVyQ4)
