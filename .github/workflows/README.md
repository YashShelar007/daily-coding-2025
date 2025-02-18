# .github Directory

This folder contains configuration and workflows for **GitHub Actions**, along with any repository-wide community health files (e.g., issue templates, pull request templates).

## Overview

- **Workflows (`.github/workflows/`)**  
  This is where you define automated processes (CI/CD, daily tasks, etc.). Each YAML file describes a workflow triggered by specific GitHub events, such as pushes or pull requests.
  
- **Community Health Files**  
  *Issue templates*, *pull request templates*, and other files (like `CODEOWNERS`) can live here to standardize collaboration across the repository.

## Current Workflows

1. **`python-tests.yml`**  
   - **Purpose:** Runs Python tests for your LeetCode solutions whenever relevant files change or a pull request is opened.  
   - **Trigger:** Push/PR to the `leetcode-solutions/` folder.  
   - **Actions:** Checks out code, sets up Python, installs dependencies (if any), and executes `test_runner.py`.

2. **`lambda-deploy.yml`**  
   - **Purpose:** Automates packaging and deploying AWS Lambda functions and infrastructure via Terraform.  
   - **Trigger:** Push to `cloud-integrations/` folder or changes to `scripts/package_lambda.sh`.  
   - **Actions:** Packages the Lambda code, initializes Terraform, and applies the configuration.

3. **`daily-update.yml`**  
   - **Purpose:** Runs a job on every push to `main` (or any branch you specify).  
   - **Trigger:** Push to `main`.  
   - **Actions:** (Currently disabled from modifying the root README, but can be adapted for other daily tasks like notifications or log archiving.)

## Secrets & Permissions

- **Secrets** (like AWS credentials) are stored in **GitHub Repository Settings → Secrets**.  
- Each workflow references these secrets using `secrets.<SECRET_NAME>` (e.g., `${{ secrets.AWS_ACCESS_KEY_ID }}`).  
- For workflows that push changes or manage infrastructure, ensure your `GITHUB_TOKEN` or personal access token has the appropriate permissions set under `permissions:`.

## Contributing

- **Branching Strategy:** Use feature branches for new challenges or fixes, then open pull requests.  
- **Commit Messages:** Follow our tagging convention (e.g., `#leetcode`, `#aws`, `#ci`) to indicate the domain of the commit.  
- **Reviews & Approvals:** The repository might have rules requiring approvals before merging changes into `main`.

## Further Reading

- [GitHub Actions Documentation](https://docs.github.com/en/actions)  
- [Terraform Documentation](https://www.terraform.io/docs)  
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)  
