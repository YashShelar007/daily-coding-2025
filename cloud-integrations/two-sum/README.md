# Two Sum Cloud Integration

This project integrates the classic **Two Sum** algorithm into a cloud-based service. The goal is to deploy the solution as a serverless function using AWS Lambda, and expose it via an API Gateway endpoint—all managed through Terraform.

## Project Overview

- **Algorithm:**  
  The Two Sum solution is implemented in Python and can be found in the corresponding algorithm repository.

- **Cloud Component:**  
  - **AWS Lambda Function:**  
    Wraps the Two Sum solution to process incoming HTTP requests.
  - **API Gateway:**  
    Provides a RESTful endpoint that triggers the Lambda function.
  - **Terraform:**  
    Automates the provisioning of the AWS Lambda function, API Gateway, and required IAM roles.

## Directory Structure

```
two-sum/
├── lambda_function/
│   ├── handler.py          # AWS Lambda handler that invokes the Two Sum solution.
│   └── requirements.txt    # Dependencies for the Lambda function.
├── terraform/
│   ├── main.tf             # Terraform configuration for Lambda, API Gateway, and IAM.
│   └── variables.tf        # Configurable variables for Terraform deployment.
└── README.md               # This file.
```

## How to Deploy

1. **Package the Lambda Function:**
   - Run the packaging script from the root of the repository:
     ```bash
     ./scripts/package_lambda.sh
     ```
   - This script packages the Lambda code from `lambda_function/` into a `lambda.zip` file.

2. **Deploy with Terraform:**
   - Navigate to the `terraform` directory:
     ```bash
     cd cloud-integrations/two-sum/terraform
     ```
   - Initialize Terraform:
     ```bash
     terraform init
     ```
   - Preview the changes:
     ```bash
     terraform plan
     ```
   - Deploy the resources:
     ```bash
     terraform apply -auto-approve
     ```

3. **Test the Service:**
   - After deployment, find the API endpoint from your Terraform output or the AWS Console.
   - Use `curl` or Postman to send a POST request:
     ```bash
     curl -X POST https://<your-api-endpoint>/twosum \
          -H "Content-Type: application/json" \
          -d '{"nums": [2, 7, 11, 15], "target": 9}'
     ```

## Future Enhancements

As you expand your cloud integrations:
- **Additional Services:**  
  Consider adding support for more complex services, such as integrating AWS S3 for storage or using CloudWatch for monitoring.
- **Multi-Region Deployments:**  
  Experiment with deploying in multiple regions or even across different cloud providers.
- **CI/CD Pipelines:**  
  Enhance your automation by integrating these deployments with your CI/CD workflows.

This project is a stepping stone towards a comprehensive cloud-based portfolio—enjoy building and exploring new cloud integrations!