bnTree = [5, [6, [3, [], []], [10, [], []]], [3, [], [7, [9, [], []], []]]]
testTree = [6,[[3,[]],[4,[[8,[]],[9,[]]]],[2,[[10,[]]]]]]

def anchuraMax(T):
    if T == []:
        return []
    levels = [[] for i in range(bnTree_height(T))]
    stack = [(T,0)]
    while stack != []:
        tree, level = stack.pop()
        if tree == []: continue
        v, L, R = tree
        levels[level].append(v)
        stack.append((L,level+1))
        stack.append((R,level+1))
    max = 0
    index = -1
    for i in range(len(levels)):
        if max < len(levels[i]):
            max = len(levels[i])
            index = i
    return index

def bnTree_height(T):
    if T == []:
        return 0
    v, L, R = T
    return max(bnTree_height(L),bnTree_height(R))+1

def tree_height(T):
    if T == []:
        return 0
    stack = [(T,0)]
    maxlvl = 0
    while stack != []:
        tree, lvl = stack.pop()
        if lvl > maxlvl:
            maxlvl = lvl
        v, chldrn = tree 
        for child in chldrn:
            stack.append((child,lvl+1))
    return maxlvl

# print(bnTree_height(bnTree))
# print(anchuraMax(bnTree))
# print("======================================")
# print(tree_height(testTree))

# Matrices de prueba
G1 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

G2 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

G3 = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

G = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

def encuentraRutar(G, S, D):
    res = []
    v = [0 for _ in range(len(G))]
    St = [(S, v, [])]
    v[S] = 1
    while St:
        o, vst, path = St.pop()
        if o == D:
            res.append(path + [o])
        else:
            for ady in range(len(G)):
                if G[o][ady] and not vst[ady]:
                    cpust = vst[:]
                    cpust[ady] = 1
                    St.append((ady, cpust, path + [o]))
    return res

G3 = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]
#print(encuentraRutar(G3, 2, 4))

def dfs_paths(G, current, end, path, paths):
    if current == end:
        paths.append(path[:])
        return
    for neighbor, connected in enumerate(G[current]):
        if connected and neighbor not in path:
            dfs_paths(G, neighbor, end, path + [neighbor], paths)

def find_all_paths(G, start, end):
    paths = []
    dfs_paths(G, start, end, [start], paths)
    return paths

print(encuentraRutar(G3,2,4))
print("========")
print(find_all_paths(G,2,4))
def dfs_ciclos(G, current, N, length, K, path, paths):
    if length == K:
        if current == N:
            paths.append(path[:])
        return
    for neighbor, connected in enumerate(G[current]):
        if connected and (neighbor not in path or (length == K - 1 and neighbor == N)):
            dfs_ciclos(G, neighbor, N, length+1, K, path + [neighbor], paths)

def ciclos(G,N,K):
    paths = []
    dfs_ciclos(G, N, N, 0, K, [N], paths)
    return paths

print("=======================")
print(ciclos(G,2,3))

def rotar(L,k):
    tmp = 0
    for i in range(k):
        tmp = L.pop()
        L.insert(0,tmp)
    return L

print(rotar([1,2,3],3))


def grafoDirigoG(G, current, N, length, K, path, paths, B):
    if length == K:
        if current == B:
            paths.append(path[:])
    for neighbor, connected in enumerate(G[current]):
        if connected and neighbor not in path:
            grafoDirigoG(G, neighbor, N, length+1, K, path + [neighbor], paths, B)

def grafoDirigido(G,A,B,K):
    paths = []
    grafoDirigoG(G, A, A, 0, K, [A], paths, B)
    return paths

def duplicar(L):
    return [element for element in L]

print(duplicar([0,4,2,6]))

print("===========")
print(grafoDirigido(G,3,4,4))
