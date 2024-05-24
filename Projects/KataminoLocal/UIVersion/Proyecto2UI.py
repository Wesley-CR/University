import customtkinter
from tkinter import *
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.iconbitmap("kataicon.ico")
app.title('Katamino Visualizer by Wesley and Felipe')
customtkinter.set_appearance_mode("dark")
app.resizable(False, False)

piece_textures = { #Diccionario bonito, https://www.w3schools.com/python/python_dictionaries.asp
#A LA MEDIDA DE LO POSIBLE USAR CASOS CON ESTOS SIMBOLOS PORFAVOR  
    "+": "imgs/t1.png",
    "%": "imgs/t2.png",
    "=": "imgs/t3.png",
    "#": "imgs/t4.png",
    "*": "imgs/t5.png",
    "&": "imgs/t6.png",
    "^": "imgs/t7.png",
    "@": "imgs/t8.png",
    "%": "imgs/t9.png",
    "$": "imgs/t10.png",
    ".": "imgs/t11.png",
}

texturascargadas = {}

def cargarimgs():
    for simbolo, img in piece_textures.items(): 
        texturascargadas[simbolo] = ImageTk.PhotoImage(Image.open(img))

def dibujartablero(n, m, tablero):
    c = 70 #Tamaño de cada cuadro (70 funciona bien no cambiar porfis)
    cuadros = [] 
#Gracias pagina francesa https://math.univ-lyon1.fr/irem/Formation_ISN/formation_interfaces_graphiques/module_tkinter/exo_canevas.html
    dibujo = Canvas(app, width=m * c, height=n * c, bg='black')
    dibujo.grid(row=0, column=0, columnspan=2, padx=3, pady=3)
    for fila in range(n):
        transito = []
        for columna in range(m):
            x1 = columna * c
            y1 = fila * c
            x2 = (columna + 1) * c
            y2 = (fila + 1) * c
            simbolo = tablero[fila][columna]
            imgte = texturascargadas.get(simbolo) #https://www.w3schools.com/python/ref_dictionary_get.asp

            if imgte:  # checkea si el simbolo tiene textura
                cuadrito = dibujo.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=imgte, anchor=CENTER) #https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
                #https://stackoverflow.com/questions/29132608/how-to-center-a-image-in-a-canvas-python-tkinter
            else:
                # Pone piezas negras en los espacios donde no hay simbolo valido (los que no están en el diccionario)
                notexture = texturascargadas["."]
                cuadrito = dibujo.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=notexture, anchor=CENTER)

            transito.append(cuadrito)
        cuadros.append(transito)
def katamino(pieces, board):
    if is_solution(board):
        if pieces != []:
            return None
        dibujartablero(len(board), len(board[0]), board)
        return board
    if not pieces:
        return None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                empty_cell = (row, col)
                break
        else:
            continue
        break
    for piece in pieces:
        for rotation in get_children(piece):
            offset_right = 0
            offset_bottom = 0
            distanceRight = len(board[0]) - empty_cell[1]
            distanceBottom = len(board) - empty_cell[0]
            crCols = len(rotation[0])
            crRows = len(rotation)
            while crCols > distanceRight:
                offset_right += 1
                distanceRight += 1
            while crRows > distanceBottom:
                offset_bottom += 1
                distanceBottom += 1
            processedCoords = (empty_cell[0] - offset_bottom, empty_cell[1] - offset_right)
            if can_place(rotation, board, processedCoords):
                put_a_piece(rotation, board, processedCoords)
                pieces_copy = [p for p in pieces if p != piece]
                result = katamino(pieces_copy, board)
                if result is not None:
                    return result
                remove_piece(processedCoords,rotation, board)
    return None
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
def get_children(pieceCopy):
    pieceCopy = copy_matrix(pieceCopy)
    children = []
    tempFlipped = []
    children.append(pieceCopy)
    newRotation = copy_matrix(pieceCopy)
    for i in range(3):
        newRotation = rotate_matrix(newRotation)
        children.append(copy_matrix(newRotation))
    for i in range(len(children)):
        flippedPiece = matrixflip(copy_matrix(children[i]))
        tempFlipped.append(flippedPiece)
    for x in range(len(children)):
        children[x] = cut_matrices(children[x])
        tempFlipped[x] = cut_matrices(tempFlipped[x])
        if children[x] != tempFlipped[x]:
            children.append(tempFlipped[x])
    return children
def is_solution(board):
    for i in range(len(board)):
        if '.' in board[i] : return False
    else: return True
def remove_piece(position, rotation, board):
    for row in range(len(rotation)):
        for col in range(len(rotation[0])):
            if rotation[row][col] != '.':
                board[row + position[0]][col + position[1]] = '.'
def copy_matrix(matrix):
    newMatrix = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newMatrix[i][j] = matrix[i][j]
    return newMatrix
def can_place(piece, board, position):
    if position[0] + len(piece) > len(board) or position[1] + len(piece[0]) > len(board[0]):
        return False
    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] != '.' and board[row + position[0]][col + position[1]] != '.':
                return False
    return True
def get_positions(board):
    positions = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                positions.append((row, col))
    return positions
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
def rotate_matrix(m):
    rotada = []
    for _ in range(len(m)):
        rotada.append([])
    for i in range(len(m)):
        for j in range(len(m)): #len(m[0]) no
            rotada[i].append(m[j].pop())
    return rotada
def matrixflip(m):
    tempm = m[::]
    for i in range(0,len(tempm)):
            tempm[i].reverse()
    return(tempm)
def cut_matrices(matrix):
    matrix = cut_matrix_top(matrix)
    matrix = cut_matrix_right(matrix)
    matrix = cut_matrix_bottom(matrix)
    matrix = cut_matrix_left(matrix)
    return matrix
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
def print_matrix(matrix):
    max_len = max(len(str(element)) for row in matrix for element in row)
    for row in matrix:
        for element in row:
            print(str(element).rjust(max_len), end="")
        print()

cargarimgs() #Carga las imagenes, asi no muere nada

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

app.mainloop()
