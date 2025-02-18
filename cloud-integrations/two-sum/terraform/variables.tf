variable "aws_region" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "The name for the Lambda function"
  type        = string
  default     = "two-sum-function"
}

variable "runtime" {
  description = "Runtime environment for Lambda"
  type        = string
  default     = "python3.8"
}

variable "memory_size" {
  description = "Memory (in MB) allocated to the Lambda function"
  type        = number
  default     = 128
}

variable "timeout" {
  description = "Lambda function execution timeout (in seconds)"
  type        = number
  default     = 10
}

variable "lambda_zip_path" {
  description = "Relative path to the zipped Lambda deployment package"
  type        = string
  default     = "../lambda_function/lambda.zip"
}

variable "api_name" {
  description = "Name of the API Gateway"
  type        = string
  default     = "two-sum-api"
}
