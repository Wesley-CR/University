def printM(M):
    for i in range(len(M)):
        print(M[i])
#1.I still have no idea how to do the first promblem

#2. Batman

#3. Funcion en forma matricial
def transposeM(M):
    r = [[0 for i in range(len(M))]for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
           r[j][i] = M[i][j]
    return r

# testMatrix = [[2,3,4,5],
#               [5,6,2,4]]
def dotPoint(v1,v2):
    r = 0
    for i in range(len(v1)):
        r += v1[i]*v2[i]
    return r

def matMult(A,B):
    return [[dotPoint(row,col) for col in transposeM(B)]for row in A]

def nulMat(m,n):
    return [[0 for i in range(n)]for j in range(m)]

def idenMat(m):
    r = nulMat(m,m)
    for i in range(m):
        r[i][i] = 1
    return r

def expMat(M,e):
    if e == 0: return idenMat(len(M))
    r = expMat(M,e//2)
    r = matMult(r,r)
    if e%2:
        r = matMult(M,r)
    return r

def function(n):
    A = [[0,1, 0],
         [0,0, 1],
         [4,0,-1]]
    B = [[0],
         [1],
         [2],]
    return matMult(expMat(A,n),B)[0][0]

# print(function(10))

#4. matrix acum
def acumMat(M):
    r = nulMat(len(M)+1,len(M[0])+1)
    for i in range(len(M)):
        for j in range(len(M[0])):
            r[i+1][j+1] = M[i][j]+r[i][j+1]+r[i+1][j]-r[i][j]
    return r

def cantidadArboles(M,Q):
    res = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == ".": M[i][j] = 0
            if M[i][j] == "*": M[i][j] = 1
    M = acumMat(M) 
    for dir in Q:
        i,j,x,y = dir[0],dir[1],dir[2],dir[3]
        res.append(M[x][y]-M[x][j-1]-M[i-1][j]+M[i-1][j-1])
    return res

# print(cantidadArboles([
# [".","*",".","."],
# ["*",".","*","*"],
# ["*","*",".","."],
# ["*","*","*","*"]],
#                 [(2,2,3,4),
#                  (3,1,3,1),
#                  (1,1,2,2)]))

def reps(L):
    if len(L)==0:
        return []
    if len(L)==1:
        return [L]
    l = []
    for i in range(len(L)):
        m = L[i]
        restL = L[:i] + L[i+1:]
        for p in reps(restL):
            l.append([m]+p)
    return l

# X = [1,2,3,4]
# print(reps(X))

def permGen(L,K,combActual,index,combinations):
    if len(combActual) == K:
        combinations.append(combActual)
        return
    for i in range(len(L)):
        permGen(L,K,combActual+[L[i]],index+1,combinations)

def anotherPerm(L,K):
    combinations = []
    permGen(L,K,[],0,combinations)
    return combinations

# L = [1, 2]
# K = 3
# result = anotherPerm(L, K)
# print(result)

def rep_perm_gen(L,K,current,index,combinations):
    if len(current) == 3:
        combinations.append(current)
        return
    for i in range(L):
        rep_perm_gen(L,K,current+[L[i]],index+1,combinations)

def rep_perm(L,K):
    combinations = []
    rep_perm_gen(L,K,[],0,combinations)
    return combinations

def perms(list):
    if len(list)==0: return []
    if len(list)==1: return [list]
    l = []
    for i in range(len(list)):
        m = list[i]
        rest = list[:i] + list[i+1:]
        for item in perms(rest):
            l.append([m]+item)
    return l

# print(perms([2,5]))

def quickSort(list):
    if (list == []): return list
    menor = []
    mayor = []
    for i in list[1:]:
        if i < list[0]:
            menor.append(i)
        else: 
            mayor.append(i)
    return quickSort(menor)+[list[0]]+quickSort(mayor)

def difSim(A,B):
    A = quickSort(A)
    B = quickSort(B)
    C = []
    while(A and B):
        if A[0] < B[0]:
            C.append(A[0])
            A = A[1:]
        elif (A[0]==B[0]):
            A = A[1:]
            B = B[1:]
        else:
            C.append(B[0])
            B = B[1:]
    if B:
        for i in range(len(B)):
            C.append(B[i])

    if A:
        for i in range(len(A)):
            C.append(A[i])
    return C

print(difSim([1,2,3],[3,4,5]))
print(difSim([1,2,3],[2,3,1]))

