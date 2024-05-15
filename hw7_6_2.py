testTree = [6,[[3,[]],[4,[[8,[]],[9,[]]]],[2,[[10,[]]]]]]
#1
# Height
def tree_height(T):
    if T == []: return 0
    v, hjs = T
    mx = -1
    for h in hjs:
        mx = max(mx,tree_height(h)+1)
    return mx + 1

print(tree_height(testTree))
#2. Max and Min
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
    if T == []: return -1
    v, hjs = T
    minNode = v
    for h in hjs:
        result = least_value_node(h)
        if result < minNode:
            minNode = result
    return minNode

print(least_value_node(testTree))
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
#3 Order
print("============================================")
# Pre-order
def pre_order(T):
    if T == []: return
    v, chldrn = T
    print(v)
    for chld in chldrn:
        pre_order(chld)

pre_order(testTree)
print("============================================")
# From now on im going to assume the trees are binary trees :D
bnTree = [5, [6, [3, [], []], []], [3, [], [7, [9, [], []], []]]]

def in_order(T):
    if T == []:
        return
    v, L, R = T
    in_order(L)
    print(v)
    in_order(R)

in_order(bnTree)

in_order(bnTree)

print("============================================")
#Post order
def post_order(T):
    if T == []: return
    v, L, R = T
    post_order(L)
    post_order(R)
    print(v)

post_order(bnTree)

print("============================================")
#TODO Inverse orders

#Levels
# All levels in which a number n appears
def levels_of_n(T,n):
    if T == []: return []
    levels = []
    stack = [(T,0)]
    while stack:
        tree, level = stack.pop()
        v, L, R = tree
        if v == n:
            levels.append(level)
        if L:
            stack.append((L,level+1))
        if R:
            stack.append((R,level+1))
    return levels
        
print(levels_of_n(bnTree,3))

# All nodes in a level
def nodes_in_a_level(T,level):
    if T == []: return []
    nodes = []
    stack = [(T,0)]
    while stack:
        tree, l = stack.pop()
        v, L, R = tree
        if l == level:
            nodes.append(v)
        if L:
            stack.append((L,l+1))
        if R:
            stack.append((R,l+1))
    return nodes

print(nodes_in_a_level(bnTree,2))

# Advanced
# is balanced
def binary_tree_height(T):
    if T == []: return 0
    v, L, R = T
    return max(binary_tree_height(L),binary_tree_height(R)) + 1

def is_balanced(T):
    if T == []: return True
    v, L, R = T
    if abs(binary_tree_height(L)-binary_tree_height(R)) > 1:
        return False
    return is_balanced(L) and is_balanced(R)

print(is_balanced(bnTree))

