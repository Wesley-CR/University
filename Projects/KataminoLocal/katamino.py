#Dominio: Lista de piezas y una matriz
def katamino(pieces, board):
    if is_solution(board):
        if pieces != []:
            return None
        return board
    if not pieces:
        return None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                emptyCell = (row, col)
                break
        else:
            continue    # Continuar al siguiente row si no se encuentra una celda vacía en este row
        break       # Salir del bucle externo si se encontró una celda vacía
    for piece in pieces:
        flag = False
        for rotation in get_children(piece):
            # Los offsets son para que la pieza no se salga del tablero
            # Funcionan de manera que mientras mas cerca esta la pieza de la derecha o abajo del tablero
            # mas grande es el offset que se le da a la pieza
            offset_right = 0
            offset_bottom = 0
            distanceRight = len(board[0]) - emptyCell[1]
            distanceBottom = len(board) - emptyCell[0]
            crCols = len(rotation[0])
            crRows = len(rotation)
            while crCols > distanceRight:
                offset_right += 1
                distanceRight += 1
            while crRows > distanceBottom:
                offset_bottom += 1
                distanceBottom += 1
            # I actually dont know how this works, but it does
            if not flag:
                if rotation[0][0] == '.': 
                    flag = True
                    offset_right += 1
                    processedCoords = (emptyCell[0] - offset_bottom, emptyCell[1] - offset_right)
                    if placeable(rotation, board, processedCoords):
                        put_a_piece(rotation, board, processedCoords)
                        pieces_copy = [p for p in pieces if p != piece]
                        result = katamino(pieces_copy, board)
                        if result is not None:
                            return result
                        remove_piece(processedCoords,rotation, board)
                    offset_right -= 1
                else:
                    flag = False
            processedCoords = (emptyCell[0] - offset_bottom, emptyCell[1] - offset_right)
            '''
            print("====================DEBUG====================")
            print("Empty Cell: ", emptyCell)
            print("Rotation: ")
            print_matrix(rotation)
            print("Offsets: ", offset_bottom, offset_right)
            print("Board: ")
            print_matrix(board)
            '''
            # Si la pieza se puede colocar en la posición actual, se pone y llama a la función recursivamente

            if placeable(rotation, board, processedCoords):
                put_a_piece(rotation, board, processedCoords)
                
                pieces_copy = [p for p in pieces if p != piece]
                result = katamino(pieces_copy, board)
                if result is not None:
                    return result
                remove_piece(processedCoords,rotation, board)
    # Si no se puede poner ninguna pieza en la posición actual, devuelve None para retroceder y probar otra pieza
    return None
#Codominio: La matriz con la solución del problema / None si no hay solución

#Dominio: Tres enteros
def pieceinput(L, A, P):
    piezas = []
    piezastemp = []
    for x in range(P*4):
        if x % 4==0 and x>3:
            piezas.append(piezastemp)
            piezastemp = []
        val = input() 
        val = [x for x in val]
        piezastemp.append(val)
    piezas.append(piezastemp)
    solution = katamino(piezas,[['.' for _ in range(A)]for _ in range(L)])
    if solution == None:
        return -1
    else:
        return solution
#Codominio: Una matriz con la solución del problema / -1 si no hay solución

#Dominio: Una copia de la pieza
def get_children(piece):
    pieceCopy = copy_matrix(piece)
    children = []
    tempFlipped = []
    # Agrega la pieza original a la lista de hijos
    children.append(pieceCopy)
    newRotation = copy_matrix(pieceCopy)
    # Rota la pieza tres veces y agrega cada rotación a la lista de hijos
    for i in range(3):
        newRotation = rotate_matrix(newRotation)
        children.append(copy_matrix(newRotation))
    # Voltea cada pieza en la lista de hijos y la agrega a la lista tempFlipped 
    for i in range(len(children)):
        flippedPiece = matrixflip(copy_matrix(children[i]))
        tempFlipped.append(flippedPiece)
    # Corta cada pieza en las listas de hijos y tempFlipped
    # Si la pieza cortada no es igual a la pieza correspondiente en tempFlipped, agréguela a la lista de hijos
    for x in range(len(children)):
        children[x] = cut_matrices(children[x])
        tempFlipped[x] = cut_matrices(tempFlipped[x])
        if children[x] != tempFlipped[x]:
            children.append(tempFlipped[x])
    return children
#Codominio: Una lista de piezas

#Dominio: Una matriz y una lista de piezas
def is_solution(board):
    for i in range(len(board)):
        if '.' in board[i] : return False
    else: return True
#Codominio: Un booleano


#La unica razon por la que esta función existe es porque la memoria de Python es rara
#Dominio: Una matriz
def copy_matrix(matrix):
    newMatrix = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newMatrix[i][j] = matrix[i][j]
    return newMatrix
#Codominio: Una copia de la matriz

#Dominio: Una Pieza, una matriz y una posición
def placeable(piece, board, position):
    """Verifica si una pieza puede ser colocada en una posición dada en el tablero.
    Si la pieza se sale del tablero o si se superpone con otra pieza, devuelve False."""
    if position[0] + len(piece) > len(board) or position[1] + len(piece[0]) > len(board[0]):
        return False
    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] != '.' and board[row + position[0]][col + position[1]] != '.':
                return False
    return True
#Codominio: Un booleano

#Dominio: Posiciones, rotaciones de una pieza y una matriz
def remove_piece(position, rotation, board):
    for row in range(len(rotation)):
        for col in range(len(rotation[0])):
            if rotation[row][col] != '.':
                board[row + position[0]][col + position[1]] = '.'
#Codominio: La matriz con la pieza removida

#Dominio: Una copia de la pieza, una matriz y una lista de posiciones
def put_a_piece(pieceCopy,matrix,positions):
    x = 0
    y = 0
    posX,posY = positions
    for i in range(posX,posX+len(pieceCopy)):
        y = 0
        for j in range(posY,posY+len(pieceCopy[0])):
            if matrix[i][j] == '.':
                matrix[i][j] = pieceCopy[x][y]
            y += 1
        x += 1
    return matrix
#Codomino: La matriz con la pieza puesta en la posición dada

#Dominio: Una matriz
def rotate_matrix(m):
    rotada = []
    for _ in range(len(m)):
        rotada.append([])
    for i in range(len(m)):
        for j in range(len(m)): #len(m[0]) no
            rotada[i].append(m[j].pop())
    return rotada
#Codominio: La matriz rotada 90 grados a la izquierda

#Dominio: Una matriz
def matrixflip(m):
    tempm = m[::]
    for i in range(0,len(tempm)):
            tempm[i].reverse()
    return(tempm)
#Codomino: La matriz volteada

#Estas funciones de corte están separadas porque al principio solo cortamos partes de ella y
#luego nos dimos cuenta que ocupabamos cortar todo, woops

#Dominio: Una matriz
def cut_matrices(matrix):
    matrix = cut_matrix_top(matrix)
    matrix = cut_matrix_right(matrix)
    matrix = cut_matrix_bottom(matrix)
    matrix = cut_matrix_left(matrix)
    return matrix
#Codominio: La matriz cortada en todos los lados

#Dominio: Una matriz
def cut_matrix_top(M):
    while True:
        for i in range(len(M[0])):
            if M[0][i] != '.':
                return M
        M.pop(0)
    return M
#Codominio: La matriz cortada en la parte superior

#Dpminio: Una matriz
def cut_matrix_bottom(M):
    while True:
        for i in range(len(M[0])):
            if M[-1][i] != '.':
                return M
        M.pop()
    return M
#Codominio: La matriz cortada en la parte inferior

#Dominio: Una matriz
def cut_matrix_left(M):
    while True:
        for row in M:
            if row[0] != '.':
                break
        else:
            for row in M:
                row.pop(0)
            continue
        break
    return M
#Codominio: La matriz cortada en la parte izquierda

#Dominio: Una matriz
def cut_matrix_right(M):
    while True:
        for row in M:
            if row[-1] != '.':
                break
        else:
            for row in M:
                row.pop()
            continue
        break
    return M
#Codominio: La matriz cortada en la parte derecha

#Dominio: Una matriz
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='')
        print()
#Codominio: La matriz impresa en consola, con cada linea de la matriz en una linea diferente en consola - Fancy

#=======================Driver Code=======================
inputs = input()
L,A,P = inputs.split(' ')
L = int(L)
A = int(A)
P = int(P)
kataminofinal = pieceinput(L,A,P)
if kataminofinal == -1:
    print(kataminofinal)
else:
    print_matrix(kataminofinal)