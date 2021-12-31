def merge_sorted_array(arr1,arr2,m,n):
    i=m-1
    j=n-1
    k=len(arr1)-1
    while(i>=0 and j>=0):
        if(arr1[i]>arr2[j]):
            arr1[k],arr1[i]=arr1[i],arr1[k]
            i-=1
            k-=1
        else:
            arr1[k],arr2[j]=arr2[j],arr1[k]
            j-=1
            k-=1
    if(i<0):
        while(k>=0):
            arr1[k]=arr2[j]
            k-=1
            j-=1
    return arr1
print(merge_sorted_array([1,2,3,0,0,0],[2,5,6],3,3))


