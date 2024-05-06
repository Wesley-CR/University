def esValido(M,i,j):
    rows = len(M)
    cols = len(M[0])
    if i >= rows or i < 0: return False
    if j >= cols or j < 0: return False
    return True

def esPunto(M,i,j):
    return M[i][j] == '.'

guards = ['<','>','^','v']
guardsDir = [[0,-1],[0,+1],[1,0],[-1,0]]

def limpiar(M,i,j,dir):
    k = 1
    while(esValido(M,i+k*dir[0],j+k*dir[1]) and M[i+k*dir[0]][j+k*dir[1]] != 'X'):
        M[i+k*dir[0]][j+k*dir[1]] = M[i][j]
        k += 1

def buscarHijos(M,i,j):
    dirs = [[-1, 0], #Up
            [0 ,-1], #Left
            [-1,-1], #Top left
            [0 , 1], #Right
            [-1, 1], #Top Right
            [1 ,-1], #Bottom left
            [1 , 0], #Bottom
            [1 , 1]] #Bottom Right
    hijos = []
    for dir in dirs:
        nX = i + dir[0]
        nY = j + dir[1]
        if esValido(M,nX,nY):
            if esPunto(M,nX,nY):
                hijos.append([nX,nY])
    return hijos

def batman(M):
    visitados = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    initPoint = (-1,-1)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'B': initPoint = (i,j)
            if M[i][j] in guards:
                limpiar(M,i,j,guardsDir[guards.index(M[i][j])])

    if M[0][0] != '.': return False

    pila = buscarHijos(M,initPoint[0],initPoint[1])
    while pila != []:
        current = pila.pop()
        visitados[current[0]][current[1]] = 1
        if visitados[0][0] == 1: return True
        hijos = buscarHijos(M,current[0],current[1])
        for casilla in hijos:
            if visitados[casilla[0]][casilla[1]] == 0:
                pila.append(casilla)
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









