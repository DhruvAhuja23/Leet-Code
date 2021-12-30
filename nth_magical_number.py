def magic(a,b,n):
    A=a
    B=b
    left=min(a,b)
    right=min(a,b)*n
    while(b>0):
        temp=a
        a=b
        b=temp%b
    lcm=A*B//a
    while(left < right):
        m=left+(right-left)//2
        c=(m/A) + (m/B) - (m/lcm)
        if((m//A) + (m//B) - (m//lcm) < n):
            left=m+1
        else:
            right=m
    return left % (pow(10,9)+7)

print(magic(6,4,3))
