def set_matrix(mat):
    is_col=False
    for i in range(len(mat)):
        
        if(mat[i][0]==0):
            is_col=True
        for j in range(1,len(mat[0])):
            if(mat[i][j]==0):
                mat[i][0]=0
                mat[0][j]=0

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if((not mat[i][0]) or (not mat[0][j])):
                mat[i][j]=0

    if(mat[0][0]==0):
        for j in range(len(mat[0])):
            mat[0][j]=0
    
        # if first column value i value is 0 i have to set whole column as 0
    if is_col:
        for i in range(len(mat)):
            mat[i][0]=0
    return mat
print(set_matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))