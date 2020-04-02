## Given a non-empty array of integers, every element appears twice except for one.
## Find that single one.

# Example 1:
#Input: [2,2,1]
#Output: 1

# Example 2:
#Input: [4,1,2,1,2]
#Output: 4

# Method 1
def singleNumber(self, nums: List[int]) -> int:
    my_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

    val_once = [key for (key, value) in my_dict.items() if value is 1]
    return(val_once[0])

# Method 2
def singleNumber(self, nums: List[int]) -> int:
    my_dict = {}
    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1
    for k, v in my_dict.items():
        if v == 1:
            return k
    return []