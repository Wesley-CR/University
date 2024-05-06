def encontrar_ruta(C):
    """
    recibe una matriz de rutas en la ciudad
    retorna una matriz con el camino marcado por 1's, o nula si no había camino
    """
    # se considera estado de aceptacion haber alcanzado la casilla X-1, Y-1
    if not C:   # si la matriz viene vacía
        return []
    pos_inicial = C[0][0]
    if pos_inicial:
        return []
    R = [[0] * len(C[0]) for _ in range(len(C))]      # la salida
    visitados = set()
    if ruta_aux(0, 0, C, R, visitados):
        return R
    return []


def ruta_aux(i, j, C, R, visitados):
    if (i, j) in visitados or not esValido(C, i, j):
        return False

    visitados.add((i, j))

    if C[i][j]:
        return False

    # falta revisar si ya llegamos a la última posición, que significa estado de aceptación
    if i == len(R) - 1 and j == len(R[0]) - 1:
        R[i][j] = 1
        return True
    
    direcciones = [[0, -1],
                   [-1, 0],
                   [0, 1],
                   [1, 0]]
    
    if esValido(C, i, j):
        R[i][j] = 1
        for dir in direcciones:
            dir_i, dir_j = i + dir[0], j + dir[1]
            if esValido(C, dir_i, dir_j):
                if ruta_aux(dir_i, dir_j, C, R, visitados):
                    return True
        R[i][j] = 0
        return False


def esValido(C, i, j):
    """
    Función para validar un índice a acceder en una matriz.
    Se invoca antes de acceder al índice para evitar errores de rango.
    Retorna True si los índices i y j están dentro de 0 y el tamaño de la matriz.
    """
    filas = len(C)
    columnas = len(C[0])
    if i < 0 or j < 0 or i >= filas or j >= columnas:
            return False
    if C[i][j] == 1:
        return False
    return True
