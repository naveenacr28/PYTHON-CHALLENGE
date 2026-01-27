"""Given an array nums and a target sum, find the indices of two numbers that add up to the target.
Input : nums = [2,7,11,15], target = 9
Output : [0,1] (because 2 + 7 = 9)"""

target = 9
nums = [2,3,7,6]
for i in range (0,len(nums)-1):
    for j in range (0,len(nums)-1):
        sum = nums[i]+nums[j+1]
        if sum==target:
            print(f"{i},{j+1}")