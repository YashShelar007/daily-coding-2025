# daily-coding-2025

# Daily Coding & Cloud Integration Challenge
This monorepo showcases daily projects that combine algorithm challenges (from LeetCode) with cloud, front-end, AI, and DevOps integrations.

## Project Structure
- **leetcode-solutions/**: Contains pure algorithm implementations (e.g., Two Sum, Valid Parentheses).
- **cloud-integrations/**: Contains cloud projects (AWS Lambda, Terraform, CloudFormation, etc.).
- **scripts/**: Utility scripts (e.g., packaging Lambda functions).
- **.github/workflows/**: CI/CD workflows for testing and deployment.

## Day 1 – Two Sum & Cloud Integration
- **LeetCode Problem:** Two Sum
- **Algorithm Implementation:** Located at `leetcode-solutions/two-sum/`
  - Run tests using: `python leetcode-solutions/two-sum/test_runner.py`
- **Cloud Integration:** AWS Lambda function deployed via Terraform, located at `cloud-integrations/two-sum/`
  - Package the Lambda with: `./scripts/package_lambda.sh`
  - Deploy using Terraform in `cloud-integrations/two-sum/terraform/`
  
## Day 2 – Valid Parentheses & Front-End Webapp
- **LeetCode Problem**: Valid Parentheses 
- **Algorithm Implementation**: Located at `leetcode-solutions/valid-parentheses`
  - Run tests using: `python leetcode-solutions/valid-parentheses/test_runner.py`
- **Front-End Component**: `frontend-components/bracket-matcher` (React).
  - Live checks bracket strings for validity.

## How to Contribute
Follow our commit guidelines using tags:
- `#leetcode` for algorithm changes
- `#aws` for cloud integrations
- `#ci` for workflow updates
Happy coding!