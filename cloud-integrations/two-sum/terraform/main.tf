terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Create IAM Role for Lambda execution
resource "aws_iam_role" "lambda_exec" {
  name = "${var.lambda_function_name}-exec"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Attach AWSLambdaBasicExecutionRole to the IAM role
resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Define the Lambda function
resource "aws_lambda_function" "two_sum" {
  function_name = var.lambda_function_name
  handler       = "handler.lambda_handler"  # file: handler.py, function: lambda_handler
  runtime       = var.runtime
  role          = aws_iam_role.lambda_exec.arn
  memory_size   = var.memory_size
  timeout       = var.timeout
  filename      = var.lambda_zip_path

  # Ensure deployment updates when the zip file changes
  source_code_hash = filebase64sha256(var.lambda_zip_path)
}

# Create an HTTP API using API Gateway v2
resource "aws_apigatewayv2_api" "api" {
  name          = var.api_name
  protocol_type = "HTTP"
}

# Integrate the Lambda function with the API Gateway
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.two_sum.invoke_arn
  integration_method     = "POST"
  payload_format_version = "2.0"
}

# Define a route for the API (e.g., POST /twosum)
resource "aws_apigatewayv2_route" "default" {
  api_id    = aws_apigatewayv2_api.api.id
  route_key = "POST /twosum"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# Create a default stage to deploy the API automatically
resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.api.id
  name        = "$default"
  auto_deploy = true
}

# Allow API Gateway to invoke the Lambda function
resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.two_sum.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
}
