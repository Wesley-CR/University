testTree = [2,[[3,[]],[4,[]],[5,[[10,[]]]]]]
# Height
def tree_height(T):
    if T == []: return 0
    v, hjs = T
    mx = -1
    for h in hjs:
        mx = max(mx,tree_height(h)+1)
    return mx + 1

print(tree_height(testTree))
# Most value node
def most_value_node(T):
    if T == []: return -1
    v, hjs = T
    maxNode = v
    for h in hjs:
        result = most_value_node(h)
        if result > maxNode:
            maxNode = result
    return maxNode

print(most_value_node(testTree))
# Path to most value node
def most_value_node_path(T):
    if T == []: return T
    mvNode = most_value_node(T)
    v, children = T
    path = [v]
    if v == mvNode:
        return 0
    for child in children:
        if most_value_node_path(child) != -1:
            path.append(child[0])
    return path

print(most_value_node_path(testTree))

# Least value node
def least_value_node(T):
    if T == []: return 100000
    v, hjs = T
    minNode = v
    for h in hjs:
        result = least_value_node(h)
        if result < minNode:
            minNode = result
    return minNode

print(most_value_node(testTree))
# Path to least value node
def least_value_node_path(T):
    if T == []: return T
    mvNode = least_value_node(T)
    v, children = T
    path = [v]
    if v == mvNode:
        return 0
    for child in children:
        if least_value_node_path(child) != -1:
            path.append(child[0])
    return path

print(least_value_node_path(testTree))
