def searchin_2D_matrix(arr,element):
    R=len(arr)
    C=len(arr[0])
    low=0
    high=R-1
    row=-1
    col=-1
    while(low<=high):
        mid=(low+high)//2
        if ((mid==len(arr)-1) or (arr[mid][0]<=element and arr[mid+1][0]>element)):
            row=mid
            break
        elif(arr[mid][0]>element):
            high=mid-1
        else:
            low=mid+1
    low=0
    high=C-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[row][mid]==element):
            col=mid
            return True
        elif(arr[mid][0]>element):
            high=mid-1
        else:
            low=mid+1
    return  False 

print(searchin_2D_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

