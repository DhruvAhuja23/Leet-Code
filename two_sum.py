def two_sum(nums,target):
    ans=[]
    pair={}
    for i in range(len(nums)):
        search=target-nums[i]
        if(nums[i] in pair.keys()):
            ans.append(pair[nums[i]][0])
            ans.append(i)
            break
        else:
            pair[search]=[i,nums[i]]
    return ans

print(two_sum([2,7,11,15],9))