def isValid(board,i,j):
    if i < 0 or i >= len(board): return False
    if j < 0 or j >= len(board[0]): return False
    return True

def genChildren(board,i,j):
    children = []
    dirs = [[ 2,-1],#Top left
            [ 2, 1],#Top Rigth
            [-1,-2],#Left Top
            [ 1,-2],#Left Bottom
            [-1, 2],#Right Top
            [ 1, 2],#Rigth Bottom
            [-2,-1],#Bottom left
            [-2, 1]]#Bottom Right
    for dir in dirs:
        nI = i + dir[0]
        nJ = j + dir[1]
        if isValid(board,nI,nJ):
            children.append([nI,nJ])
    return children

def isSolved(visited):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] != 1: return False
    return True

def knightsTour(N):
    board = [[0 for _ in range(N)]for __ in range(N)]
    visited = [[0 for _ in range(N)]for __ in range(N)]
    visited[0][0] = 1
    counter = 1
    pila = [[0,0]]
    while pila != []:
        newPos = pila.pop()
        board[newPos[0]][newPos[1]] = counter
        counter += 1
        visited[newPos[0]][newPos[1]] = 1
        if isSolved(visited): 
            printM(visited)
            return board
        children = genChildren(board,newPos[0],newPos[1])
        for child in children:
            if visited[child[0]][child[1]] == 0:
                pila.append(child)
        board[newPos[0]][newPos[1]] = 0
        counter -= 1
        visited[newPos[0]][newPos[1]] = 0
    printM(visited)
    printM(board)
    return False

def printM(M):
    for i in range(len(M)):
        print(M[i])

printM(knightsTour(5))
