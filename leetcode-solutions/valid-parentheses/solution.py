def isValid(s):
    """
    Determines if a string of brackets is valid.
    
    A string is valid if:
      1. Every opening bracket has a corresponding closing bracket of the same type.
      2. Brackets close in the correct order.

    :param s: A string consisting of characters '()[]{}'
    :return: True if 's' is a valid parentheses string, False otherwise.
    """

    # Map each closing bracket to its corresponding opening bracket
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        if char in mapping:
            # char is a closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # char is an opening bracket
            stack.append(char)

    return len(stack) == 0
