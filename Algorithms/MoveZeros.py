def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    numslen = len(nums)
    for i in reversed(range(len(nums))):
        if nums[i] is 0:
            nums.pop(i)
    addlen = numslen - len(nums)
    nums += [0] * addlen