def printM(M):
    for i in range(len(M)):
        print(M[i])

def nullM(m,n):
    return [[0 for i in range(m)]for i in range(n)]

def identityM(n):
    I = nullM(n,n)
    for i in range(n):
        I[i][i] = 1
    return I

def mat_mult(A,B):
    rowsA = len(A)
    collsB = len(B[0])
    collsA = len(A[0])
    C = [[0 for i in range(collsB)] for j in range(rowsA)]
    for i in range(rowsA):
        for j in range(collsB):
            for k in range(collsA):
                C[i][j] += A[i][k] * B[k][j]
    return C

# This version for some reason is too big??
# def expo_log_mat(M,e):
#     n = len(M)
#     if e == 0:
#         return [[1 if i == j else 0 for i in range(n)]for j in range(n)]
#     if e == 1:
#         return M
#     half_exp = e//2
#     half_mat = expo_log_mat(M,half_exp)
#     if not e%2:
#         return mat_mult(M,e)
#     return mat_mult(M,mat_mult(M,e))

def mat_exp(M,e):
    if not e: return identityM(len(M))
    r = mat_exp(M,e//2)
    r = mat_mult(r,r)
    if e%2:
        r = mat_mult(M,r)
    return r

def transpuesta(M):
    res = [[0 for i in range(len(M))]for j in range(len(M[0]))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = M[j][i]
    return res

def prod_pto(A,B):
    res = 0
    for i in range(len(A)):
        res+= A[i]*B[i]
    return res

def mult_mat(A,B):
    return [[prod_pto(row,col) for col in transpuesta(B)] for row in A]

A = [[2,2,3,-7],
     [3,4,-3,4]]

B = [[2,2,4],
     [3,1,1],
     [2,0,5],
     [4,3,0]]

# printM(mult_mat(A,B))
# printM(mat_mult(A,B))

def quickSort(M):
    if M == []: return M
    Lower = []
    Higher = []
    for i in M[1:]:
        if i<M[0]:
            Lower.append(i)
        else:
            Higher.append(i)
    return quickSort(Lower)+[M[0]]+quickSort(Higher)

# testList = [2,45,34,55,6,56,65,12,5,3,8]
# print(quickSort(testList))

def mAcum(M):
    lenght = len(M)
    width = len(M[0])
    acum = [[0 for i in range(width+1)]for i in range(lenght+1)]
    for i in range(lenght+1):
        for j in range(width+1):
            acum[i+1][j+1] = M[i][j]+acum[i+1][j]+acum[i][j+1]-res[i][j]
    return acum

def difSim(A,B):
    C = quickSort(A)
    D = quickSort(B)
    ds = []
    while C and D:
        if C[0]<D[0]:
            ds.append(C[0])
            C = C[1:]
        else if C[0] == D[0]:
            C = C[1:]
            D = D[1:]
        else:
            ds.append(D[0])
            D = D[1:]
    return ds













