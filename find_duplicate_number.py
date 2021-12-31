def findDuplicate(nums):
    while(nums[0]!=nums[nums[0]]):
        temp=nums[nums[0]]
        nums[nums[0]]=nums[0]
        nums[0]=temp
    return nums[0]
print(findDuplicate([1,3,4,2,2]))