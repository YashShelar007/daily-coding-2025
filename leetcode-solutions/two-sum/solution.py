def twoSum(nums, target):
    """
    Given an array of integers 'nums' and an integer 'target',
    returns the indices of the two numbers such that they add up to target.
    If no solution exists, returns an empty list.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
        
    return []  # No solution found
