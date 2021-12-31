def repeat_and_missing_number(arr):
    #to check the duplicate and missing number in given array
    #here i have use xor operation to cancel out the repeating numbers in the range of 1 to N
    #ans then i have checked the right most set bit number to evaluate among which number from the is responsible for setting that particular bit
    #After that i have again traverse through the array and taking the xor again first with elements of array and then with range to 
    #cancel out repeating element the element remained was x if its count is more than 1
    #else the element is y   
    n=len(arr)
    xor1=0
    x=0
    y=0
    count=0
    for i in arr:
        xor1^=i
    for j in range(1,n+1):
        xor1^=j
    
    set_bit_no=xor1 & ~(xor1-1)

    for i in range(len(arr)):
        if(arr[i] & set_bit_no):
            x^=arr[i]
        else:
            y^=arr[i]
    for i in range(1,n+1):
        if(i & set_bit_no):
            x^=i
        else:
            y^=i

    for i in arr:
        if(i==x):
            count+=1
    if(count==0):
        return [y,x]
    return [x,y]

print(repeat_and_missing_number([3, 1, 2, 5, 3]))