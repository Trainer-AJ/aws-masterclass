# 🎥 Day-14 | Configuration Management With Ansible | Puppet vs Ansible | Live Projects  
**Speaker:** Abhishek Veeramalla  
**Video URL:** [http://www.youtube.com/watch?v=I5_NF8nvACg](http://www.youtube.com/watch?v=I5_NF8nvACg)  

This session focuses on **Configuration Management (CM)** in DevOps — explaining the evolution from manual scripting to automation through CM tools — and provides a detailed **comparison between Ansible and other tools like Puppet and Chef**.  

---

## 🧩 1. Configuration Management (CM) Overview

| Concept | Description | Timestamp |
|---|---|---|
| **Definition** | Configuration Management is the way a DevOps engineer manages the configuration of servers or infrastructure. | [02:05] |
| **The Problem (Pre-CM Era)** | Before CM tools, SysAdmins had to manually log into each server to perform updates, patches, or software installations, which was time-consuming and error-prone. | [04:54] |
| **Traditional Solution** | Administrators relied on **Shell scripts (Linux)** or **PowerShell scripts (Windows)** to automate repetitive tasks. | [06:04] |
| **Drawback** | Scripts required frequent updates for different OS distributions (CentOS, Ubuntu, Alpine) and command changes, reducing maintainability. | [08:33] |
| **Impact of Cloud & Microservices** | Cloud adoption increased the number of servers by **10x**, making manual/scripting-based methods unsustainable. | [07:04], [08:12] |
| **Popular CM Tools** | Puppet, Chef, Ansible, and Salt are widely used tools in the CM ecosystem. | [10:25] |
| **Recommendation** | Ansible is the preferred tool — estimated to be used by **90% of organizations**, and recommended for DevOps beginners. | [12:40] |

---

## ⚖️ 2. Comparison: Ansible vs. Puppet/Chef

The video highlights **four major reasons** why Ansible became the most popular CM tool.

| Feature | **Ansible** | **Puppet / Chef (Other CM Tools)** |
|---|---|---|
| **Mechanism** | **Push Model** – Configuration is pushed directly from the Ansible control node to target machines. | **Pull Model** – Agents periodically pull configuration updates from a master node. | 
| **Architecture** | **Agentless:** No installation of agents on target servers; uses SSH/WinRM directly. | **Master-Slave (Agent-Based):** Requires agent setup on each managed node. | 
| **Language** | Uses **YAML Manifests (Playbooks)** — human-readable and simple. | Requires learning a dedicated **domain-specific language (e.g., Puppet DSL)**. | 
| **OS Support** | Excellent cross-platform support — **Linux via SSH**, **Windows via WinRM**. | Managing Windows servers can be more complex and limited. | 

---

### 💡 Key Advantages & Concepts of Ansible

- **Simplicity:** Playbooks use YAML syntax, making automation easier to understand and write. [23:14]  
- **Agentless Connectivity:** Requires only IP/DNS of the target servers and SSH key-based authentication. [17:05]  
- **Dynamic Inventory:** Automatically detects and manages new cloud instances (e.g., new AWS EC2 servers). [19:59]  
- **Customization:** Written in **Python**; engineers can develop and share custom modules through **Ansible Galaxy**. [27:16], [28:27]  

---

## ⚠️ 3. Disadvantages of Ansible

| Limitation | Description | Timestamp |
|---|---|---|
| **Windows Support** | Managing Windows servers is slightly more complex than Linux systems. | [25:05] |
| **Debugging Complexity** | Debug logs from Playbook runs can be difficult to interpret, making troubleshooting harder. | [25:38] |
| **Performance Bottlenecks** | May experience slowdowns when running tasks on **very large infrastructures** (e.g., 10,000+ servers). | [26:18], [26:51] |

---

## 🎯 4. Common Ansible Interview Questions (and Answers)

| **Question** | **Answer** | **Timestamp** |
|---|---|---|
| **What programming language does Ansible use, and can you write custom modules?** | Ansible is written in **Python**, and supports writing custom modules in Python (shared via **Ansible Galaxy**). | [31:08] |
| **Does Ansible support both Linux and Windows? What protocols does it use?** | Yes. Uses **SSH** for Linux and **WinRM** for Windows. | [31:38], [31:56] |
| **What is the difference between Puppet and Ansible, and why choose Ansible?** | Ansible uses a **Push Model** and is **Agentless**, while Puppet uses a **Pull Model** with a **Master-Slave setup**. | [32:55] |
| **Is Ansible a push or pull mechanism?** | **Push mechanism.** | [33:42] |
| **What language are Ansible Playbooks written in?** | **YAML (YAML Manifests).** | [34:08] |
| **Does Ansible support all cloud providers (AWS, Azure, GCP)?** | Yes, it’s **cloud-agnostic** — only requires SSH/WinRM connectivity. | [34:36] |

---

## 🧠 Summary

- **Ansible** revolutionized configuration management by eliminating the need for agents and simplifying automation with YAML.  
- It integrates seamlessly across **cloud environments** and **hybrid infrastructures**, making it the tool of choice for modern DevOps teams.  
- While **debugging** and **large-scale performance** remain challenges, its simplicity, extensibility, and community support make it the dominant CM tool in the industry.  

---

**🔗 Video Reference:** [Day-14 | Configuration Management With Ansible | Puppet vs Ansible | #ansible #devops](http://www.youtube.com/watch?v=I5_NF8nvACg)

# 🎥 Day-15 | Getting Started with Ansible — Installation, Authentication, Ad Hoc Commands, Playbooks & Roles  
**Speaker:** Abhishek Veeramalla  
**Video Title:** *“Day-15 | Getting Started with Ansible | Ad Hoc Commands | Playbooks | Roles | Live Projects”*  
**Video URL:** *(not provided but part of the same DevOps 45-day series)*  

This video provides a **practical, step-by-step guide** to starting with **Ansible**, focusing on installation, authentication, ad hoc commands, playbooks, and roles. It’s an essential session for DevOps engineers looking to automate configuration management and infrastructure provisioning.

---

## ⚙️ 1. Initial Setup and Prerequisites

| **Key Point / Fact** | **Details** | **Timestamp** |
|---|---|---|
| **Recommended Environment** | Begin learning Ansible on a **Linux system** (e.g., an Ubuntu AWS EC2 instance). It’s simpler to install and manage than on Windows or macOS. | [00:39] |
| **Installation (Ubuntu)** | Use the `apt` package manager after updating repositories to install Ansible easily:  
  ```bash
  sudo apt update && sudo apt install ansible -y
  ```
| [02:07] |
| **Minimum Setup Requirement** | Requires **two servers** — one Ansible control node (where Ansible is installed) and at least one **target server** (the managed node). | [04:30] |
| **Verification Command** | To verify installation:  
  ```bash
  ansible --version
  ```
| [04:08] |

---

## 🔐 2. Setting Up Passwordless Authentication

Passwordless SSH is **a prerequisite for Ansible** to communicate with managed servers.

| **Step** | **Description** | **Command / Fact** | **Timestamp** |
|---|---|---|---|
| **1️⃣ Generate SSH Keys** | Run the key generation command on the Ansible control node. | `ssh-keygen` | [07:22] |
| **2️⃣ Share the Public Key** | Copy the generated public key (`id_rsa.pub`) to the target server and append it to its `~/.ssh/authorized_keys` file. |  | [09:28] |
| **3️⃣ Test Passwordless Access** | Ensure SSH connection works without password prompts:  
  ```bash
  ssh <username>@<target_IP>
  ```
| Once this works, Ansible can execute commands automatically.
| [11:01] |

---

## ⚡ 3. Ansible Ad Hoc Commands

Ad Hoc commands allow for **quick, one-line automation** without writing full Playbooks — perfect for small, one-time tasks.

| **Key Concept / Fact** | **Details** | **Timestamp** |
|---|---|---|
| **Inventory File** | Stores IPs or hostnames of all target servers. Default location: `/etc/ansible/hosts`. You can also define your own file locally. | [15:50] |
| **Grouping Servers** | You can create groups inside the inventory file like `[web_servers]` or `[DB_servers]` to run tasks selectively. 
| [24:41] |

**Example Command:**
```bash
ansible -i inventory all -m shell -a "touch devops_class"
```

ansible → Main command

-i inventory → Path to inventory file

all → Targets all listed servers (or specific groups like web_servers)

-m shell → Uses the “shell” module to run shell commands

-a → Specifies the actual command to execute

| [17:28] |



---

📘 4. Ansible Playbooks

Playbooks are YAML files that define multi-step automation tasks — the true power of Ansible.

Key Fact / Concept	Explanation	Timestamp

File Format	Written in YAML (.yaml or .yml) and start with ---.	[27:06], [27:24]
Basic Syntax Elements		


hosts: all
become: true   # Run tasks with root privileges
tasks:
  - name: <task name>
    module_name:
      parameter: value
```
 | [29:01] |
| **Execution Command** |
  
```bash
ansible-playbook -i inventory first-playbook.yaml
```
| |
| **Fact Gathering** | First step in any Playbook — collects detailed facts about each target machine. | [37:01] |
| **Debugging** | Add verbosity flags (`-v`, `-vv`, or `-vvv`) for detailed logs. | [38:39] |

**Example: Install and Start Nginx**
```yaml
---
- hosts: all
become: true
tasks:
  - name: Install nginx
    apt:
      name: nginx
      state: present

  - name: Start nginx
    service:
      name: nginx
      state: started


---

🧩 5. Ansible Roles

Roles help organize complex Playbooks into reusable, modular components. They’re crucial for real-world production automation.

Concept / Command	Explanation	Timestamp

Need for Roles	A Playbook with 50–60 tasks (like for a Kubernetes cluster) becomes unreadable; Roles divide it logically.	[43:58]
Create a Role	Automatically generate a role structure using Ansible Galaxy:	


ansible-galaxy role init kubernetes
``` | [45:25] |
| **Role Directory Structure** |  
- `tasks/` → Defines main tasks (`main.yaml`) [50:17]  
- `handlers/` → Triggered only when notified (e.g., restart service) [52:26]  
- `templates/` → Contains **Jinja2 templates** for dynamic config files [53:44]  
- `files/` → Static files like `index.html` or certificates [53:15]  
- `vars/` and `defaults/` → Store variables [51:52]  
- `meta/` → Metadata like author, license, dependencies [51:04] |

---

## 🌍 6. Real-Time Scenario (Infrastructure + Configuration)

| **Tool** | **Purpose** | **Example** | **Timestamp** |
|---|---|---|---|
| **Terraform** | Used to create the infrastructure (e.g., spin up 3 EC2 instances). | Provision cloud infrastructure. | [42:55] |
| **Ansible** | Configures the infrastructure post-creation (e.g., install Kubernetes or software on those servers). | One EC2 as a **master node**, two as **worker nodes**. | [43:24] |

---

## 🧠 Summary

- **Ansible Installation:** Simple and quick setup on Ubuntu.  
- **Passwordless SSH:** A key prerequisite for communication.  
- **Ad Hoc Commands:** Perfect for fast, one-time automation tasks.  
- **Playbooks:** YAML-based, structured automation for multiple tasks.  
- **Roles:** Enable large-scale, organized, reusable configurations.  
- **Integration:** Works seamlessly with **Terraform** or other IaC tools for end-to-end automation.  

---

**✅ Key Takeaway:**  
> Ansible enables **agentless**, **idempotent**, and **repeatable automation** across hybrid environments — a must-have skill for DevOps engineers.

