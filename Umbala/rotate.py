def rotate(matrix, n):
    """
    Matrix of size n*n
    """
    for i in range(0, (n+1)//2):
        for j in range(0+i, n-i-1):
            t1 = matrix[i][j]
            t2 = matrix[j][n-i-1]
            t3 = matrix[n-i-1][n-j-1]
            t4 = matrix[n-j-1][i]
            matrix[j][n-i-1] = t1
            matrix[n-i-1][n-j-1] = t2
            matrix[n-j-1][i] = t3
            matrix[i][j] = t4

    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = 4

for i in range(0, n):
    print(matrix[i])

rotated_matrix = rotate(matrix, n)

for i in range(0, n):
    print(rotated_matrix[i])
