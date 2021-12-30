def findMedianSortedArrays(x,y):
    len_x=len(x)
    len_y=len(y)
    start=0 #dividing the two arrays in such a way we can find a point at which max(x_left) <= min(y_right) && max(y_left)<=min(x_right)
    if(len_x==0 and len_y>=1):
        return y[len_y//2] if(len_y&1) else (y[len_y//2-1]+y[len_y//2])/2 
    if(len_x>=1 and len_y==0):
        return x[len_x//2] if(len_x&1) else (x[len_x//2-1]+x[len_x//2])/2
    end=min(len_x,len_y)-1
    x_ans=0
    y_ans=0
    if(len(x)>len(y)):
        findMedianSortedArrays(y,x)
    while True: #[1,5,8,9,10] #[2,6,7,11,12,13] #[1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        position_x=(start+end)//2 #index 1 
        #y=3
        if((len_x+len_y)%2==1):
            position_y=(len_x+len_y)//2 - position_x
        else:
            position_y=(len_x+len_y)//2 - position_x -1
        x_left= x[position_x] if (position_x>=0) else -float('inf')
        x_right=x[position_x+1] if(position_x+1<len_x) else float('inf')
        y_left= y[position_y-1] if (position_y-1>=0) else -float('inf')
        y_right=y[position_y] if(position_y<len_y) else float('inf')
        # if((x[position_x] <= y[position_y]) and (y[position_y-1] <= x[position_x+1]) ):
        if(x_left<=y_right and y_left<=x_right ):
            x_ans=max(x_left,y_left)
            y_ans=min(x_right,y_right)
            break
        elif(x_left > y_right):
            end=position_x-1
        else:
            start=position_x+1
    if((len_x+len_y)%2==1):
        return x_ans
    else:
        return (x_ans+y_ans)/2
print(findMedianSortedArrays([3],[-1,-2]))