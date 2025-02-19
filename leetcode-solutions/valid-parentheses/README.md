# Valid Parentheses (LeetCode #20)

## Problem Statement

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid. A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example:
- `()[]{} -> True`
- `(] -> False`

## Approach

A common solution uses a **Stack**:
1. Traverse the string character by character.
2. If you see an opening bracket, push it onto the stack.
3. If you see a closing bracket, check the top of the stack:
   - If it matches the corresponding opening bracket, pop it.
   - Otherwise, the string is invalid.
4. At the end, if the stack is empty, the string is valid.

### Time Complexity
O(n), where n is the length of the string (single pass).

### Space Complexity
O(n) in the worst case (all opening brackets).

## File Structure

```
valid-parentheses/
├── solution.py        # The Python solution for Valid Parentheses
├── testcases.jsonl    # JSON-lines file with test cases
├── test_runner.py     # Script to run all test cases
└── README.md          # This file
```

## How to Run Locally

1. **Navigate to the directory**:
   ```bash
   cd leetcode-solutions/valid-parentheses
   ```
2. **Run the test runner**:
   ```bash
   python test_runner.py
   ```
3. **Observe the results** in the console.
