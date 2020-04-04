## Given an integer array nums, find the contiguous subarray (containing at least one number)
## which has the largest sum and return its sum.

# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[i], array[i])
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar

# O(n) time | O(1) space