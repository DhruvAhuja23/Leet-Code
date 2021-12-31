def rotate(mat):
    R=len(mat)
    C=len(mat[0])
    #Taking mid column ans swapping the element accross it 
    #for example [[1,2,3],[4,5,6],[7,8,9]] is coverted to [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    for i in range(R):
        for j in range(C//2):
            mat[i][j],mat[i][R-j-1]=mat[i][R-j-1],mat[i][j]
    
    #taking transpose across right diagonal
    for i in range(R):
        for j in range(C-i):
            mat[i][j],mat[R-j-1][R-i-1]=mat[R-j-1][R-i-1],mat[i][j] 

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))