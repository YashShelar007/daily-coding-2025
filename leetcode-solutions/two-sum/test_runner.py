import json
import os
from solution import twoSum

def run_test_case(test_case):
    nums = test_case["nums"]
    target = test_case["target"]
    expected = test_case["expected"]
    
    result = twoSum(nums, target)
    
    # If expected is "No solution", then result should be an empty list.
    if expected == "No solution":
        passed = (result == [] or result is None)
    else:
        passed = (result == expected)
    
    return result, expected, passed

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(current_dir, 'testcases.jsonl')
    
    try:
        with open(test_file, 'r') as f:
            # Read each non-empty line and load it as a JSON object.
            test_cases = [json.loads(line) for line in f if line.strip()]
    except Exception as e:
        print("Error reading test cases:", e)
        return
    
    all_passed = True
    for idx, test_case in enumerate(test_cases, start=1):
        result, expected, passed = run_test_case(test_case)
        if passed:
            print(f"Test case {idx}: PASSED")
        else:
            print(f"Test case {idx}: FAILED")
            print(f"  Input: nums = {test_case['nums']}, target = {test_case['target']}")
            print(f"  Expected: {expected}, Got: {result}")
            all_passed = False
    
    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

if __name__ == '__main__':
    main()
