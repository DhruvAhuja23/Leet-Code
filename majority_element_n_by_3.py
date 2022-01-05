def majority_element_n_by_3(arr):
    if(len(arr)==1):
            return arr
    num1=-float('inf')
    num2=-float('inf')
    count1=0
    count2=0
    for i in range(len(arr)):
        if(num1==arr[i]):
            count1+=1
        elif(num2==arr[i]):
            count2+=1
        elif(count1==0):
            num1=arr[i]
            count1=1
        elif(count2==0):
            num2=arr[i]
            count2=1
        else:
            count1-=1
            count2-=1
    canCan1=0
    canCan2=0
    for i in range(len(arr)):
        if(num1==arr[i]):
            canCan1+=1
        if(num2==arr[i]):
            canCan2+=1
    arr1=[]
    if(canCan1>len(arr)//3):
        arr1.append(num1)
    if(canCan2>len(arr)//3):
        arr1.append(num2)
    return arr1

print(majority_element_n_by_3([1,1,2,2,3,2,1]))

