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
    return katamino(piezas,[['.' for _ in range(A)]for _ in range(L)],0,(0,0),[],0)

def katamino(pieces,board,row,lastPutCoords,lasPutPiece,usedPieces=0):
    # we can use pieces like a queue and pila like a stack
    if row > len(board): return board
    n = len(pieces)
    if usedPieces >= n: 
        remove_piece(lasPutPiece,board,lastPutCoords[0],lastPutCoords[1])
        return False
    for _ in range(len(pieces)): #revisar
        #check if pieces is empty and the board is filled
        if pieces == []: 
            if is_solution(board):
                print("no puedo parar de llorar")
                return board
            else:
                print("No solution")
                return -1
        current = pieces.pop()
        pila = get_children(current)
        valid_rotation = False
        print_matrix(board)
        i = 0
        while i < len(board[0]) and pila != []:
        #for i in range(len(board[0])):
            if board[row][i] == '.':
                offset_right = 0
                offset_bottom = 0
                current_rotation = pila.pop()
                distanceRight = len(board[0]) - i
                distanceBottom = len(board) - row
                crCols = len(current_rotation[0])
                crRows = len(current_rotation)
                while crCols > distanceRight:
                    offset_right += 1
                    distanceRight += 1
                while crRows > distanceBottom:
                    offset_bottom += 1
                    distanceBottom += 1
                if is_valid(current_rotation,board,(row-offset_bottom,i-offset_right)):
                    put_a_piece(current_rotation,board,row-offset_bottom,i-offset_right)
                    lasPutPiece = current_rotation
                    valid_rotation = True
                    print_matrix(board)
                    if pila == []:
                        break
                    if '.' in board[row]:
                        if katamino(pieces, board, row, (row-offset_bottom,i-offset_bottom),lasPutPiece, usedPieces):
                            return True
                        remove_piece(current_rotation,board,row-offset_bottom,i-offset_right)
                    if katamino(pieces,board,row+1, (row-offset_bottom,i-offset_bottom),current_rotation,usedPieces):
                        return True
                    remove_piece(current_rotation,board,row-offset_bottom,i-offset_right)
                else:

                    i -= 1
                    continue
            i+=1 
        if not valid_rotation:
            pieces.insert(0,current)
            usedPieces += 1
            katamino(pieces,board,row, (row-offset_bottom,i-offset_bottom),current_rotation,usedPieces)

                                                                                                                        #junior mewing tercero

# The only reason for this function is because we dont know how to use python memory right!!
def copy_matrix(matrix):
    newMatrix = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newMatrix[i][j] = matrix[i][j]
    return newMatrix

def get_children(pieceCopy):
    pieceCopy = copy_matrix(pieceCopy)
    children = []
    tempFlipped = []
    # Add the original pieceCopy to the children list
    children.append(pieceCopy)
    newRotation = copy_matrix(pieceCopy)
    # Rotate the pieceCopy three times and add each rotation to the children list
    for i in range(3):
        newRotation = rotate_matrix(newRotation)
        children.append(copy_matrix(newRotation))
    # Flip each pieceCopy in the children list and add it to the tempFlipped list
    for i in range(len(children)):
        flippedPiece = matrixflip(copy_matrix(children[i]))
        tempFlipped.append(flippedPiece)
    # Cut each pieceCopy in the children and tempFlipped lists
    # If the cut pieceCopy is not equal to the corresponding pieceCopy in tempFlipped, add it to the children list
    for x in range(len(children)):
        children[x] = cut_matrices(children[x])
        tempFlipped[x] = cut_matrices(tempFlipped[x])
        if children[x] != tempFlipped[x]:
            children.append(tempFlipped[x])
    return children
#LETS ******* GOOOOOOOOOOOOOOOOOOOOO!1!1111111111!!!!111!!!!111!!!!111!!!1111!!!111!!!!1

def is_valid(pieceCopy,board,coords):
    x = 0
    if coords[0] > len(board) + len(pieceCopy): return False
    if coords[1] > len(board[0])+ len(pieceCopy[0]): return False
    for i in range(coords[0],coords[0]+(len(pieceCopy))):
        y = 0
        for j in range(coords[1],coords[1]+(len(pieceCopy[0]))):
            if j > len(board[0]) or i>len(board): return False
            if board[i][j] != '.' and pieceCopy[x][y] != '.':
                return False
            y +=1
        x+=1
    return True

def is_solution(board):
    for i in range(len(board)):
        if '.' in board[i]: return False
    else: return True

def get_positions(board):
    positions = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                positions.append((row, col))
    return positions

def put_a_piece(pieceCopy,matrix,posX,posY):
    x = 0
    y = 0
    for i in range(posX,posX+len(pieceCopy)):
        y = 0
        for j in range(posY,posY+len(pieceCopy[0])):
            if matrix[i][j] == '.':
                matrix[i][j] = pieceCopy[x][y]
            y += 1
        x += 1
    return matrix

def remove_piece(pieceCopy,matrix,posX,posY):
    x = 0
    y = 0
    for i in range(posX,posX+len(pieceCopy)):
        y = 0
        for j in range(posY,posY+len(pieceCopy[0])):
            if matrix[i][j] == pieceCopy[x][y]:
                matrix[i][j] = '.'
            y += 1
        x += 1
    return matrix

def rotate_matrix(mat):
    N = len(mat)
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp
    while mat[0][0] == "." and mat[1][0] == "." and mat[2][0] == "." and mat[3][0] == ".":
        for i in range(len(mat)):
            mat[i] = mat[i][1:] + [mat[i][0]]
    return mat

def matrixflip(m): #flip
    tempm = m[::]
    for i in range(0,len(tempm)):
            tempm[i].reverse()
    return(tempm)

def cut_matrix_top(M):
    while True:
        for i in range(len(M[0])):
            if M[0][i] != '.':
                return M
        M.pop(0)
    return M

def cut_matrix_bottom(M):
    while True:
        for i in range(len(M[0])):
            if M[-1][i] != '.':
                return M
        M.pop()
    return M

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

def cut_matrices(matrix):
    matrix = cut_matrix_top(matrix)
    matrix = cut_matrix_right(matrix)
    matrix = cut_matrix_bottom(matrix)
    matrix = cut_matrix_left(matrix)
    return matrix

#=======================EVERYTHING BELOW THIS IS JUST TESTING LOL====================================

matrix = [[0 for i in range(10)]for j in range(10)]
#pieceCopy = [[0,'%',0,0],
#         ['%','%','%',0],
#         [0,'%',0,0],
#         [0,0,0,0]]

piece2 = [[0,0,0,0],
          [0,0,0,0],
          [0,0,'■','■'],
          ['■','■','■',0]]
piece4=[['.', '.', '.', '.'], 
        ['.', '.', '.', '.'],
        ['o', '.', '.', '.'], 
        ['o', 'o', 'o', '.']]
#fancy matrix printing
def print_matrix(matrix):
    max_len = max(len(str(element)) for row in matrix for element in row)
    print()
    for row in matrix:
        for element in row:
            print(str(element).rjust(max_len), end=" ")
        print()
    print()

L,A,P = split(" ",input())
L = int(L)
A = int(A)
P = int(P)
pieceinput(L,A,P)

# tempStack = get_children(piece4)
# for i in range(len(tempStack)):
#     print_matrix(tempStack[i])
# piece4 =cut_matrix_top(piece4)
# piece4 =cut_matrix_right(piece4)
# print_matrix(piece4)

# testMatrix = [['.' for i in range(15)] for j in range(15)]
# testMatrix = put_a_piece(piece4,testMatrix,10,5)
# testMatrix = put_a_piece(piece4,testMatrix,9,6)
# print_matrix(testMatrix)
# # print_matrix(put_a_piece(pieceCopy,matrix,1,1))
# print_matrix(piece2)
# r2 = rotateMatrix(piece2) 
# print_matrix(r2)
# r3 = rotateMatrix(r2) 
# print_matrix(r3)
# r4 = rotateMatrix(r3) 
# print_matrix(r4)


#print(*piezas, sep='\n')
#print()
#print(*piezas[0], sep='\n')
#print(*piezas, sep='\n')









