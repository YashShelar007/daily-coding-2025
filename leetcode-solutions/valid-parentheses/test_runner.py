import json
import os
from solution import isValid

def run_test_case(test_case):
    input_str = test_case["input"]
    expected = test_case["expected"]
    result = isValid(input_str)
    passed = (result == expected)
    return result, expected, passed

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(current_dir, 'testcases.jsonl')

    try:
        with open(test_file, 'r') as f:
            test_cases = [json.loads(line.strip()) for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading testcases.jsonl: {e}")
        return

    all_passed = True
    for idx, test_case in enumerate(test_cases, start=1):
        result, expected, passed = run_test_case(test_case)
        if passed:
            print(f"Test case {idx}: PASSED")
        else:
            print(f"Test case {idx}: FAILED")
            print(f"  Input: {test_case['input']}")
            print(f"  Expected: {expected}, Got: {result}")
            all_passed = False

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

if __name__ == '__main__':
    main()
