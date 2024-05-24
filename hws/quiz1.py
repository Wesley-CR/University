#Suma de nodos a distancia 7
def make_tree(height, value=1):
    if height == 0:
        return []
    else:
        return [value, make_tree(height-1, value+1), make_tree(height-1, value+1)]

def print_tree(tree, level=0):
    if tree == []:
        return
    value, left, right = tree
    print_tree(right, level + 1)
    print('    ' * level + str(value))
    print_tree(left, level + 1)

def suma_de_nodos(tree, distance = 0):
    sum = 0
    if tree == []:
        return 0
    v, left, right = tree
    if distance%7 == 0:
        sum += v
    if left: sum += suma_de_nodos(left, distance+1)
    if right: sum += suma_de_nodos(right, distance+1)
    return sum

#Create an example tree for the above function
tree = [1, [2, [3, [], []], [4, [], []]], [5, [6, [], []], [7, [], []]]]
tree2 = make_tree(8)
print_tree(tree2)
print(suma_de_nodos(tree2)) # 1 + 4 + 7 = 12

     
