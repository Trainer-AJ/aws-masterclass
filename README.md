### [AWS CCP Practice Questions GitHub Repo](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-1.md)

# utlilty Folder 
- Tested sscript to empty and dlete all buckets 
- other one that check If any such resource running that caused bill in past 
aws s3 ls | awk '{print $3}'

# AWS Prod
- AWS Org setup : 1 aws account for security team : IAM identity center + Security hub /// 2nd for sandbox /// 3rd for Prod /// 4th Dev (lower) env etc
- **real world use case**: Need to send billing for Amazon Q use to Managers. List of 65k total users in azure 183 total in azure all of them have Q license, we just need to send bills to those users manager
  1. scan those users from AWS Identity center
  2. fetch their manager name from entra ID // email is forgein key (Vertical Delivery heads -- like Bhatt >> Goyal >> Arshi => send bill to Arshi )
  3. once csv done store in s3
  4. lambda in another aws account // Identity center in another

## git
To maintain **code traceability** for every release you do — i.e., mapping every **build ID** to the exact **commit ID** it was built from — you **do not need to cherry-pick or rebase**. Instead, you can **create a release branch directly from that commit ID**.

### ✅ Best Practice: Create a Release Branch from a Commit

Let’s say you have the **commit ID**:

```bash
abc1234
```

You can simply create a release branch from it like this:

```bash
git checkout -b release/1.0.0 abc1234
git push origin release/1.0.0
```

This gives you a new branch `release/1.0.0` that points **exactly to the commit that triggered the build**.

---

### 🚫 Why You Shouldn't Use Rebase or Cherry-Pick Here

* **Cherry-pick** creates a **new commit** with a different hash, breaking traceability.
* **Rebase** rewrites history, which also changes commit hashes.
* Both can confuse traceability unless you're doing hotfixes, which is a different workflow.

---

### 🧩 Optional: Tag for Immutable Releases

If you want a read-only marker (safer than branches), use a tag:

```bash
git tag release-1.0.0 abc1234
git push origin release-1.0.0
```

Tags are great for immutable releases (e.g., production deployments), while branches are better for ongoing patching (e.g., `release/1.0.x`).

---

### 🔄 Summary

| Goal                     | Recommended Git Action                   |
| ------------------------ | ---------------------------------------- |
| Code traceability        | `git checkout -b release/x.y.z <commit>` |
| Immutable release marker | `git tag release-x.y.z <commit>`         |
| Hotfix on older release  | Branch from tag or old release branch    |
| Avoid these              | Rebase, cherry-pick (for traceability)   |

Let me know if you're using GitHub/GitLab/Bitbucket CI pipelines, and I can tailor this more.
Great question. `git restore` is a relatively new Git command (introduced in Git 2.23) that simplifies some common tasks around undoing changes. It’s useful in **working directory management**, especially when you want to discard changes or revert to a previous state *without affecting commit history*.

---

## 🛠️ `git restore` – Real-World Use Cases

---

### ✅ **Scenario 1: Discard Local File Changes**

**You edited a file but realize you don’t want the changes anymore.**

**Example:**
You accidentally made changes to `config.json` that shouldn't be committed.

```bash
git restore config.json
```

🔄 This resets `config.json` back to the version in the latest commit (HEAD).

---

### ✅ **Scenario 2: Restore Deleted Files**

**You deleted a tracked file but haven't committed yet, and you want it back.**

```bash
rm app.js
git status
# app.js is shown as deleted

git restore app.js
```

✅ It brings `app.js` back from the last committed version.

---

### ✅ **Scenario 3: Unstage a File**

**You ran `git add somefile.js` by mistake. You want to unstage it without losing your changes.**

```bash
git restore --staged somefile.js
```

This removes the file from the staging area but keeps the local changes.

---

### ✅ **Scenario 4: Reset All Local Changes in Working Directory**

**You want to throw away all uncommitted local changes in the working directory (dangerous).**

```bash
git restore .
```

It will restore **all tracked files** to the last committed version.

Add `--staged` if you also want to unstage files.

```bash
git restore --staged .  # Unstage all files
git restore .           # Discard all local changes
```

---

## 🔒 Important Notes

| Command                                | What it does                       |
| -------------------------------------- | ---------------------------------- |
| `git restore <file>`                   | Discards local changes in the file |
| `git restore --staged <file>`          | Removes the file from staging area |
| `git restore --source=<commit> <file>` | Restores file from specific commit |

---

## 👩‍💻 When to Use vs. Alternatives

| Task                    | Use `git restore`        | Older equivalent         |
| ----------------------- | ------------------------ | ------------------------ |
| Discard file changes    | ✅ `git restore <file>`   | `git checkout -- <file>` |
| Unstage a file          | ✅ `git restore --staged` | `git reset HEAD <file>`  |
| Reset working directory | ✅ `git restore .`        | `git checkout .`         |

---

## ⚠️ Not for Undoing Commits

`git restore` only works on the **working directory and index** — not commit history. For undoing commits, use:

* `git reset` (soft, mixed, hard)
* `git revert`

---

Let me know if you want a visual flowchart for when to use `restore`, `reset`, `checkout`, etc.
Sure! Let’s walk through **real-world use cases** for `git cherry-pick`, `git rebase`, and `git revert` — three powerful but often misunderstood Git tools.

---

## 🍒 `git cherry-pick`

### 🔧 Use Case: **Apply a single commit (or a few) from one branch to another**

---

### 🧑‍💻 **Real-World Example**:

You fixed a critical bug on the `develop` branch, but you also need that fix in `release/1.0.0` without merging all of `develop`.

```bash
# You're on release/1.0.0
git checkout release/1.0.0

# Cherry-pick the commit from develop
git cherry-pick abc1234
```

🎯 This applies **just that one commit** (`abc1234`) to the `release/1.0.0` branch.

---

✅ **Use cherry-pick when:**

* You want specific commits from another branch.
* You’re doing hotfixes or backporting fixes.
* You want to avoid merging the full history of another branch.

---

## 🔀 `git rebase`

### 🔧 Use Case: **Make your commit history linear and clean**

---

### 🧑‍💻 **Real-World Example**:

You’re working on a feature branch `feature/login`. Meanwhile, `main` has had a few updates. You want to integrate those updates into your feature branch **without a merge commit**.

```bash
# You're on your feature branch
git checkout feature/login

# Rebase onto main to replay your commits on top of the updated main
git rebase main
```

🎯 This reapplies your changes on top of the latest `main` branch — like rewriting history.

---

✅ **Use rebase when:**

* You want a **clean, linear commit history**.
* You're preparing a feature branch for a PR/merge.
* You're working on a private branch and want to sync with updated base branch.

---

⚠️ **Avoid rebasing public/shared branches**, as it rewrites history and can break collaborators’ work.

---

## ↩️ `git revert`

### 🔧 Use Case: **Undo a commit by creating a new commit that reverses its changes**

---

### 🧑‍💻 **Real-World Example**:

You merged a feature that introduced a bug into `main`. You want to undo it, but **keep the history and don’t mess with other commits**.

```bash
# On the main branch
git revert abc1234
```

🎯 This creates a new commit that undoes the changes introduced by `abc1234`.

---

✅ **Use revert when:**

* You need to **undo commits on a shared branch** (e.g., main or release).
* You want to preserve history and **don’t want to rewrite commit history**.
* You're fixing a bad commit without changing Git history.

---

## 🔄 Summary Comparison

| Command       | Best For                             | Rewrites History? | Safe on Shared Branches? | Example Use Case                         |
| ------------- | ------------------------------------ | ----------------- | ------------------------ | ---------------------------------------- |
| `cherry-pick` | Applying specific commits            | No                | Yes                      | Backporting a bugfix to a release branch |
| `rebase`      | Making history clean and linear      | ✅ Yes             | 🚫 No (only on private)  | Rebasing feature branch before merge     |
| `revert`      | Undoing a commit by making a new one | No                | ✅ Yes                    | Reverting a bad commit on `main`         |

---

Let me know if you want visuals or Git history examples (before/after diagrams) for any of these.
In GitHub Actions, **environment variables (env vars)** are used to pass dynamic values to workflows, jobs, and steps. GitHub provides **built-in environment variables**, and you can also define **custom ones** at different levels.

---

## 🧰 1. **Built-In Environment Variables**

GitHub automatically provides these in every Actions run.

| Variable            | Description                                       |
| ------------------- | ------------------------------------------------- |
| `GITHUB_REPOSITORY` | `owner/repo` name                                 |
| `GITHUB_REF`        | The branch or tag ref that triggered the workflow |
| `GITHUB_SHA`        | The commit SHA that triggered the workflow        |
| `GITHUB_WORKFLOW`   | The name of the workflow                          |
| `GITHUB_RUN_NUMBER` | A unique number for each run of a workflow        |
| `GITHUB_ACTOR`      | The user who triggered the workflow               |
| `GITHUB_TOKEN`      | A token used to authenticate in the workflow      |
| `GITHUB_ENV`        | File path to export env vars across steps         |

🧪 **Example** (using a built-in var in a step):

```yaml
- name: Show commit SHA
  run: echo "The commit SHA is $GITHUB_SHA"
```

---

## 🛠️ 2. **Custom Environment Variables**

You can define your own environment variables at the **workflow**, **job**, or **step** level.

### 🔹 Workflow Level

```yaml
env:
  NODE_ENV: production

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Environment is $NODE_ENV"
```

### 🔹 Job Level

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      TEST_ENV: staging
    steps:
      - run: echo "Running tests in $TEST_ENV"
```

### 🔹 Step Level

```yaml
steps:
  - name: Step with env
    run: echo "Hello $MY_NAME"
    env:
      MY_NAME: Alice
```

---

## 📦 3. **Environment Files for Sharing Variables**

To set a variable that **persists across steps**, use the `GITHUB_ENV` file.

### Example:

```yaml
- name: Set env var across steps
  run: echo "VERSION=1.2.3" >> $GITHUB_ENV

- name: Use env var
  run: echo "Version is $VERSION"
```

---

## 🔐 4. **Secrets as Env Vars**

Secrets (like tokens, passwords) are stored securely and injected into workflows as env vars.

### Example:

```yaml
env:
  MY_SECRET: ${{ secrets.MY_SECRET }}
```

Then use it like:

```yaml
- name: Use secret
  run: echo "The secret is $MY_SECRET"
```

⚠️ Avoid printing secrets directly — GitHub will mask them, but it’s better to be safe.

---

## 🌱 5. **Environments (with secrets & protection rules)**

GitHub Environments (defined in repository settings) can hold secrets and protection rules for specific deployment stages like `staging`, `prod`.

### Example:

```yaml
jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to prod
        run: echo "Deploying to ${{ vars.ENV_NAME }}"
```

You can define variables at the **environment level** using GitHub’s UI.

---

## 🧭 Summary

| Scope         | Supports Secrets? | Example                      |
| ------------- | ----------------- | ---------------------------- |
| Built-in vars | N/A               | `$GITHUB_SHA`, `$GITHUB_REF` |
| Custom vars   | No                | `env: VAR=value`             |
| Secrets       | ✅ Yes             | `${{ secrets.MY_SECRET }}`   |
| GitHub Env    | ✅ Yes             | `environment: production`    |
| Cross-step    | N/A               | `echo "X=1" >> $GITHUB_ENV`  |

---

Let me know if you want a template GitHub Actions file that uses these in practice (e.g., CI/CD or deployment).

```git
-     -------- -----------
   1        0.028 cd .\Downloads\
   2        0.093 mkdir gitDemo
   3        0.020 cd .\gitDemo\
   4        0.221 git init
   5        1.800 code -r .
   6        0.103 git add .\1-file.txt
   7        0.101 git status
   8        0.161 git commit -m "commit 1 "
   9        0.295 git log
  10        0.090 git status
  11        0.111 git restore .\1-file.txt
  12        0.064 git status
  13        0.067 git add .\1-file.txt
  14        0.139 git commit -m "commit 2 "
  15        0.172 git log
  16        0.053 git add .\1-file.txt
  17        0.122 git commit -m "release 1.0"
  18       17.398 git log
  19        0.077 git tag v1.0 0b1c2c24
  20        6.934 git log
  21        0.053 git add .\1-file.txt
  22        0.120 git commit -m "commit 3"
  23        4.315 git log
  24        0.127 git checkout -b release/v1.0 0b1c2…
```
