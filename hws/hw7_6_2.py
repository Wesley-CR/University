testTree = [6,[[3,[]],[4,[[8,[]],[9,[]]]],[2,[[10,[]]]]]]
    #     6
    #    /| \
    #   / |  \
    #  3  4   2
    #    / \   \
    #   /   \   \
    #  8     9   10
#1
# Height
def tree_height(T):
    if T == []:
        return 0
    v, hjs = T
    if hjs == []: return 0
    mx = -1
    for h in hjs:
        mx = max(mx,tree_height(h)+1)
    return mx

def bn_tree_height(T):
    if T == []:
        return 0
    v, L, R = T
    return max(bn_tree_height(L),bn_tree_height(R)) + 1

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
def most_value_node_path_aux(tree):
    return most_value_node_path(tree,most_value_node(tree))

def most_value_node_path(tree,mvNode):
    if tree == []: return -1
    v, children = tree
    path = [v]
    if v == mvNode:
        return [v]
    for child in children:
        tmp = most_value_node_path(child,mvNode)
        if tmp != -1:
            path = path + tmp
            return path
    return -1


print(most_value_node_path_aux(testTree))

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
def least_value_node_path_aux(tree):
    return most_value_node_path(tree,least_value_node(tree))

def least_value_node_path(tree,lvNode):
    if tree == []: return -1
    v, children = tree
    path = [v]
    if v == lvNode:
        return [v]
    for child in children:
        tmp = least_value_node_path(child,lvNode)
        if tmp != -1:
            path = path + tmp
            return path
    return -1

print(least_value_node_path_aux(testTree))
#3 Order
print("============================================")
# Pre-order
print("Pre-order")
def pre_order(T):
    if T == []: return
    v, chldrn = T
    order = []
    order.append(v)
    for chld in chldrn:
        order = order + pre_order(chld)
    return order

print(pre_order(testTree))
print("============================================")
# From now on im going to assume the trees are binary trees :D
bnTree = [5, [6, [3, [], []], []], [3, [], [7, [9, [], []], []]]]
print("Order")
def in_order(T):
    if T == []:
        return []
    v, L, R = T
    order = []
    if L: order = order + in_order(L)
    order.append(v)
    if R: order = order + in_order(R)
    return order

print(in_order(bnTree))

print("============================================")
#Post order
print("Post order")
def post_order(T):
    if T == []: return []
    v, L, R = T
    order = []
    if L: order = order + post_order(L)
    if R: order = order + post_order(R)
    order = order + [v]
    return order

print(post_order(bnTree))
print("============================================")
#TODO Inverse orders
# Pre-order
print("Inverse Pre-order")
def inverse_pre_order(T):
    if T == []: return
    v, chldrn = T
    order = []
    order.append(v)
    for chld in reversed(chldrn):
        order = order + pre_order(chld)
    return order

print(inverse_pre_order(testTree))
print("============================================")
# From now on im going to assume the trees are binary trees :D
bnTree = [5, [6, [3, [], []], []], [3, [], [7, [9, [], []], []]]]
print("Inverse Order")
def inverse_in_order(T):
    if T == []:
        return []
    v, L, R = T
    order = []
    if R: order = order + in_order(R)
    order.append(v)
    if L: order = order + in_order(L)
    return order

print(inverse_in_order(bnTree))

print("============================================")
#Post order
print("Inverse Post order")
def inverse_post_order(T):
    if T == []: return []
    v, L, R = T
    order = []
    order = order + [v]
    if R: order = order + post_order(R)
    if L: order = order + post_order(L)
    return order

print(inverse_post_order(bnTree))

print("============================================")
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
        
print("levels where n is")
print(levels_of_n(bnTree,3))
 
print("============================================")
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

print("all nodes in a level")
print(nodes_in_a_level(bnTree,2))

bigger_tree = [10,
               [5,
                [2, [90, [],[]], [4, [], []]],
                [8, [7, [], []], []]],
               [15,
                [12, [], []],
                [20, [18, [], []], [25, [], []]]]]
# Widest level of a tree
def widest_tree_level(tree):
    nLevels = bn_tree_height(tree)
    levels = []
    for i in range(nLevels):
        levels.append([])
    stack = [(tree,0)]
    while stack:
        tree, level = stack.pop()
        v, L, R = tree
        levels[level].append(v)
        if L:
            stack.append((L,level+1))
        if R:
            stack.append((R,level+1))
    mx = -1
    for i in range(len(levels)):
        if len(levels[i]) > mx:
            mx = i
    return levels[mx]

print(widest_tree_level(bigger_tree))
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

# Path to every node in a level
def path_to_node(tree, node):
    if tree == []:
        return []
    v, L, R = tree
    if v == node:
        return [v]
    for subtree in [L, R]:
        if subtree:
            path = path_to_node(subtree, node)
            if path:
                return [v] + path
    return []

def path_every_node_in_a_level(tree,target):
    nodes = nodes_in_a_level(tree,target)
    paths = []
    for i in range(len(nodes)):
        paths.append(path_to_node(tree,nodes[i]))
    return paths

print(path_every_node_in_a_level(bigger_tree,2))

# All balanced trees of N nodes
def all_balanced_trees(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1, [], []]]
    trees = []
    for i in range(n):
        left = all_balanced_trees(i)
        right = all_balanced_trees(n - i - 1)
        for l in left:
            for r in right:
                trees.append([n, l, r])
    return trees

# create tree from pre-order and inorder
print("=-=-=-=-=-=-=-=-=-=-=-=")
def create_tree(preorden,inorden):
    if preorden == []: return []
    preorden.reverse()
    tree = []
    current = preorden.pop()
    tree.append(current)
    indexInInorder = inorden.index(current)
    leftTree = inorden[:indexInInorder]
    if leftTree:
        preordenTMP = [x for x in preorden if x in leftTree]
        preordenTMP.reverse()
        tree.append(create_tree(preordenTMP,leftTree))
    rightTree = inorden[indexInInorder+1:]
    if rightTree:
        preordenTMP = [x for x in preorden if x in rightTree]
        preordenTMP.reverse()
        tree.append(create_tree(preordenTMP,rightTree))
    return tree
#HOLY **** I DID IT
preorderTest = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
inorderTest = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
print(create_tree(preorderTest,inorderTest))
# IT WORKS!!!!!!!!!
