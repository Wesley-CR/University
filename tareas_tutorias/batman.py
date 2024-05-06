#Profe asi como nota, este codigo esta increiblemente
#inspirado en el suyo porsiacaso y lo de las direcciones no se
#si es como se hace normalmente pero me parece genio
def batman(M):
    visitados = set()
    # Buscar a batman
    initialPos=(0,0)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'B':
                initialPos = (i,j)
    return bodega(initialPos[0],initialPos[1],M,visitados)

def bodega(i,j,M,visitados):
    if (i,j) in visitados or not esValido(i,j,M):
        return False

    visitados.add((i,j))

    if i == 0 and j == 0:
        return True

    direcciones = [
            [ 0,-1],#Izquierda
            [-1, 0],#Arriba
            [ 1, 0],#Abajo
            [ 0, 1],#Derecha
            [ 1,-1],#Arriba,izquierda
            [-1,-1],#Abajo,izquierda
            [ 1, 1],#Arriba,derecha
            [-1, 1],#Abajo,derecha
            ]

    if esValido(i,j,M):
        for dir in direcciones:
            dir_i,dir_j = i + dir[0], j + dir[1]
            if esValido(dir_i,dir_j,M):
                if bodega(dir_i,dir_j,M,visitados):
                    return True
        return False

def esValido(i,j,M):
    filas, columnas = len(M), len(M[0])
    if i < 0 or j < 0 or i >= filas or j >= columnas:
        return False
    # Verificar si hay un obstaculo
    if M[i][j] == 'X' or M[i][j] == '<' or M[i][j] == '>' or M[i][j] == '^' or M[i][j] == 'v':
        return False
    # Verificar si hay un guarda a la derecha
    for x in range(j,columnas):
        if M[i][x] == 'X': break
        if M[i][x] == '<':
            return False
    # Verificar si hay un guarda a la izquierda
    for x in range(j,0,-1):
        if M[i][x] == 'X': break
        if M[i][x] == '>':
            return False
    # Verificar si hay un guarda a la arriba
    for x in range(i,0,-1):
        if M[x][j] == 'X': break
        if M[x][j] == 'v':
            return False
    # Verificar si hay un guarda a la abajo
    for x in range(i,filas):
        if M[x][j] == 'X': break
        if M[x][j] == '^':
            return False
    return True

print(batman(
[[".",".","X",".","v",".","<"],
[".",".",".",".","X","B","X"],
[">",".","X",".",".",".","^"]])
)

print(batman(
[[".",".",".",".",".",".","<"],
[".",".",".",".",".","B","X"],
[".","<",".",".",".",".","."]])
)
