def reverse(arr,index):
    j=len(arr)-1
    while(index<j):
        arr[index],arr[j]=arr[j],arr[index]
        index+=1
        j-=1
    

def next_permutation(arr):
    i=len(arr)-2
    while(i>=0 and arr[i+1]<=arr[i]):
        i-=1
    
    if(i>=0):
        j=len(arr)-1
        while(j>0 and arr[j]<=arr[i]):
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        reverse(arr,i+1)
    return arr
print(next_permutation([1,5,1]))