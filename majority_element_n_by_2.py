def majority_element_n_by_2(arr):
    count=0
    candidate=1
    for i in range(len(arr)):
        if(count==0):
            candidate=arr[i]
            count=1
        else:
            if(candidate==arr[i]):
                count+=1
            else:
                count-=1
    canCount=0
    for i in range(len(arr)):
        if(arr[i]== candidate):
            canCount+=1
    return candidate if(canCount>len(arr)//2) else -1

print(majority_element_n_by_2([3,3,4]))