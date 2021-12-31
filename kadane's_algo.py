def max_subarray_sum(arr):
    summ=-float('inf')
    maxSum=-float('inf')
    for i in range(len(arr)):
        summ=max(summ+arr[i],arr[i]) # To check if valuw at current index is maximum then value until this index 
        maxSum=max(summ,maxSum) # To store maximum sum of a contiguyouus sub array
    return maxSum
    
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))