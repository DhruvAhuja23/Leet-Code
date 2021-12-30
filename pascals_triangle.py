def pascals(num):
    arr=[]
    for i in range(num):
        newArr=[0]*(i+1)
        newArr[0]=1
        newArr[i]=1
        arr.append(newArr)
        for j in range(1,i):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    return arr
print(pascals(5))       
