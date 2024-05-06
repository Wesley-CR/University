guards = ['<','>','^','v']
guardsDir = [[0,-1],[0,1],[-1,0],[1,0]]

def esValido(M,i,j):
    if i < 0 or i>= len(M): return False
    if j < 0 or j>= len(M[0]): return False
    return True

def limpiar(M,i,j,dir):
    k = 1
    while esValido(M,i+k*dir[0],j+k*dir[1]) and M[i+k*dir[0]][j+k*dir[1]] != 'X':
        M[i+k*dir[0]][j+k*dir[1]] = M[i][j]
        k+=1

def buscarHijos(M,i,j):
    hijos = []
    dirs = [[-1, 0], #Up
            [0 ,-1], #Left
            [-1,-1], #Top left
            [0 , 1], #Right
            [-1, 1], #Top Right
            [1 ,-1], #Bottom left
            [1 , 0], #Bottom
            [1 , 1]] #Bottom Right
    for dir in dirs:
        nI = i + dir[0]
        nJ = j + dir[1]
        if esValido(M,nI,nJ):
            if M[nI][nJ] == '.':
                hijos.append([nI,nJ])
    return hijos

def batman(M):
    initPos = [-1,-1]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'B': initPos = [i,j]
            if M[i][j] in guards: limpiar(M,i,j,guardsDir[guards.index(M[i][j])])
    
    visitados = [[0 for i in range(len(M[0]))]for j in range(len(M))]

    pila = buscarHijos(M,initPos[0],initPos[1])
    while pila != []:
        newPos = pila.pop()
        i,j = newPos
        visitados[i][j] = 1
        if visitados[0][0] == 1: return True
        hijos = buscarHijos(M,i,j)
        for hijo in hijos:
            x,y = hijo
            if visitados[x][y] == 0:
                pila.append(hijo)
    return False

mat = [[".", ".", "X", ".", "v", ".", "<"],
       [".", ".", ".", ".", "X", "B", "X"],
       [">", ".", "X", ".", ".", ".", "^"]]

print(batman(mat))

print(batman(
[[".",".",".",".",".",".","<"],
[".",".",".",".",".","B","X"],
[".","<",".",".",".",".","."]])
)


