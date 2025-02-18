#!/bin/bash
# Navigate to the lambda_function directory in the cloud-integrations folder
cd "$(dirname "$0")/../cloud-integrations/two-sum/lambda_function" || exit

# Clean up any previous package
rm -f lambda.zip

# (Optional) Install dependencies into a 'package' directory if needed
# For now, since there are no external dependencies, we just zip the handler file.
zip -j lambda.zip handler.py

echo "Packaged Lambda function into lambda.zip"
