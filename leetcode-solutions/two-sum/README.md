# Two Sum Challenge

## Problem Statement

Given an array of integers `nums` and an integer `target`, the **Two Sum** problem asks you to return the indices of the two numbers that add up to `target`. If no solution exists, the function should return an empty list.

## Approach

The solution leverages a hash map (dictionary) to store the numbers encountered while iterating over the array. For each element, the complement (i.e., `target - current_number`) is checked in the hash map:
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

This approach ensures that the solution runs efficiently even for large input sizes.

## Files in This Directory

- **solution.py:** Contains the Python implementation of the Two Sum algorithm.
- **testcases.jsonl:** A JSON-lines file with multiple test cases. Each line represents a test case with `nums`, `target`, and the expected output.
- **test_runner.py:** A script to run the test cases against the solution and validate the results.
- **README.md:** This file, which documents the problem, approach, and instructions for running the tests.

## How to Run the Tests

1. **Ensure you are in the `two-sum` directory.**
2. **Execute the test runner:**
   ```bash
   python test_runner.py
   ```
   This script will read the test cases from `testcases.jsonl`, run the solution in `solution.py`, and output the test results.

## Additional Notes

- This solution is part of a larger project combining algorithm practice with cloud integrations and other technology domains.
- Stay tuned for additional challenges and integrations in upcoming days!

Happy coding and testing!