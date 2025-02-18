import json

def twoSum(nums, target):
    """
    Given a list of integers `nums` and an integer `target`,
    returns the indices of the two numbers such that they add up to target.
    If no solution is found, returns an empty list.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    
    Expects the incoming event to be in one of two forms:
      - Direct payload: a JSON with "nums" and "target".
      - API Gateway Proxy: where the payload is inside event["body"] as a JSON string.
    
    Returns a JSON response with the result.
    """
    print("Received event:", event)
    try:
        # Handle payload from API Gateway proxy integration
        if "body" in event:
            payload = json.loads(event["body"])
        else:
            payload = event

        # Extract inputs
        nums = payload.get("nums")
        target = payload.get("target")
        if nums is None or target is None:
            raise ValueError("Missing 'nums' or 'target' in payload")

        # Compute the result using the twoSum function
        result = twoSum(nums, target)

        response = {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }
    except Exception as e:
        print("Error:", str(e))
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response
