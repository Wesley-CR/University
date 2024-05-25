def find_node(tree,n):
    if tree == []: return False
    v, L,R = tree
    if v == n: return True
    return find_node(L,n) or find_node(R,n)

bnTree = [5, [6, [3, [], []], []], [3, [], [7, [9, [], []], []]]]
print(find_node(bnTree,12))

bigger_tree = [10,
               [5,
                [2, [90, [],[]], [4, [], []]],
                [8, [7, [], []], []]],
               [15,
                [12, [], []],
                [20, [18, [], []], [25, [], []]]]]

def list_leaves(tree):
    if tree == []: return
    v, L, R = tree
    leaves = []
    if L == [] and R == []:
        leaves.append(v)
    if L: leaves = leaves + list_leaves(L)
    if R: leaves = leaves + list_leaves(R)
    return leaves

'''
        10
       /  \
      /    \
     5      15
    / \    /  \
   /   \  /    \
  2     8 12    20
 / \   /     \    \
90  4 7       18   25
'''
print(list_leaves(bigger_tree))

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

print(is_balanced(bigger_tree))

def sum_of_nodes(tree):
    if tree == []: return 0
    v, L, R = tree
    return v + sum_of_nodes(L) + sum_of_nodes(R)

def is_triangular(n):
    tmp = 1
    while tmp < n:
        triangular = (tmp*(tmp+1))/2
        if triangular == n:
            return True
        tmp += 1
    return False

print(is_triangular(sum_of_nodes(bigger_tree)))

