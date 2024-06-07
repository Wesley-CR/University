bnTree = [5, [6, [3, [], []], [10, [], []]], [3, [], [7, [9, [], []], []]]]
      #     5
      #    / \
      #   6   3
      #  / \   \
      # 3  10   7
      #    /
      #   9 
testTree = [6,[[3,[]],[4,[[8,[]],[9,[]]]],[2,[[10,[]]]]]]
    #     6
    #    /| \
    #   / |  \
    #  3  4   2
    #    / \   \
    #   /   \   \
    #  8     9   10

def bnHeight(T):
    if T == []:
        return -1
    _, L, R = T
    return max(bnHeight(L),bnHeight(R))+1

# print(bnHeight(bnTree))

def anchuraMax(T):
    if T == []:
        return 0
    height = bnHeight(T)+1
    levels = [[] for i in range(height)]
    stack = [(T,0)]
    while stack != []:
        tree, level = stack.pop()
        levels[level].append(tree[0])
        if tree[1]:
            stack.append((tree[1],level+1))
        if tree[2]:
            stack.append((tree[2],level+1))
    max = -1
    width = -1
    for i in range(len(levels)):
        if width < len(levels[i]):
            max = i
            width = len(levels[i])
    return max,width,levels[i-1]

# print(anchuraMax(bnTree))

def ciclosG(G,N,K):
    paths = []
    ciclosG_aux(G,N,N,0,K,[N],paths)
    return paths

def ciclosG_aux(G, current, N, length, K, path, paths):
    if length == K:
        if current == N:
            paths.append(path)
    for neighbor, connected in enumerate(G[current]):
        if connected and (neighbor not in path or (neighbor == N and length == K-1)):
            ciclosG_aux(G,neighbor, N, length + 1, K, path + [neighbor], paths)

G = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]
# print(ciclosG(G,2,3))

def treeHeight(T):
    if T == []:
        return -1
    V, children = T
    height = -1
    for child in children:
        height = max(height,treeHeight(child))+1
    return height

# print(treeHeight(testTree))

def pathsAtoB(G,A,B,E):
    paths = []
    pathsAtoB_aux(G,A,A,0,E,[A],paths,B)
    return paths

def pathsAtoB_aux(G, current, N, length, K, path, paths,B):
    if length == K:
        if current == B:
            paths.append(path)
    for neighbor, connected in enumerate(G[current]):
        if connected and neighbor not in path:
            pathsAtoB_aux(G,neighbor, N, length + 1, K, path + [neighbor], paths,B)

# print(pathsAtoB(G,1,4,3))

# ==================== EXAMEN ========================
def sumEsp(T):
    return sumEsp_aux(T, 0, 0)

def sumEsp_aux(T,res,level):
    if not T:
        return res
    res += T[0] * level
    for child in T[1]:
        res=sumEsp_aux(child,res,level+1)
    return res

def sumaNodos(T):
    return sumaNodos_aux(T,0)

def sumaNodos_aux(T,res):
    if not T:
        return res
    res += T[0]
    for child in T[1]:
        res = sumaNodos_aux(child,res)
    return res

# print(sumaNodos([1000,[[2,[]],[3,[[10,[]]]]]]))
# print(sumEsp([1000,[[2,[]],[3,[[10,[]]]]]]))
def sumaNB(T):
    if T == []:
        return 0
    V,L,R = T
    V = sumaNB(L)+sumaNB(R)+V
    return V

def arb7(T):
    paths = []
    arb7_aux(T,[],paths)
    return paths

def arb7_aux(T,path,paths):
    if T == []:
        return
    V, L, R = T
    if (abs(sumaNB(T))%10) == 7:
        paths.append(path)
    if L != []:
        arb7_aux(L,path + [0], paths)
    if R != []:
        arb7_aux(R,path + [1], paths)

# print(arb7([1,[7,[],[]],[]]))
# print(arb7([28,[],[]]))
print(arb7([1,[9,[],[-2,[],[]]],[-17,[],[]]]))
def find_root(dic):
    parent_nodes = set(dic.keys())
    child_nodes = set()
    for child in dic.values():
        child_nodes.update(child)
    root = list(parent_nodes - child_nodes)
    return root[0] if root else None

def create_tree(node,dic):
    return [node,[create_tree(child,dic) for child in dic[node]]]

def reconstruirLA(aristas):
    adjList = {}
    for node, connection in aristas:
        if node in adjList:
            # adjList[node] += [[connection,[],[]]]
            adjList[node] += [connection]
            if connection not in adjList:
                adjList[connection] = []
        else:
            # adjList[node] = [[connection,[],[]]]
            adjList[node] = [connection]
            if connection not in adjList:
                adjList[connection] = []
    root = find_root(adjList)
    return create_tree(root,adjList)

# print(reconstruirLA([[4,6],[2,3],[2,4],[2,5],[1,2]]))

def dfs(G,node,visited):
    stack = [node]
    while stack != []:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for i in range(len(G)):
                if G[current][i] == 1 and not visited[i]:
                    stack.append(i)

def clasificaGrafo(G):
    n = len(G)
    visited = [False] * n
    print(visited)
    componentsCount = 0

    #Verificar si es arbol
    for i in range(n):
        tmp = sum(G[i])
        if tmp > 1:
            return "grafo general"

    #Verificar si es mas de uno
    for i in range(n):
        if not visited[i]:
            dfs(G,i,visited)
            componentsCount += 1

    #retornar arbol o bosque
    return "arbol" if componentsCount == 1 else "bosque"

test = [[0,0],
        [0,0]]
# print(clasificaGrafo(G))
# print(clasificaGrafo(test))

def rutaHojas(T):
    if not T:
        return []
    paths = []
    stack = [(T,[1])]
    while stack != []:
        tree, path = stack.pop()
        V, L, R = tree
        if L == [] and R == []:
            paths.append(path)
        if L != []:
            stack.append((L,path + [0]))
        if R != []:
            stack.append((R,path + [1]))
    return paths

# print(rutaHojas([1,[2,[],[]], [3,[],[]]]))

#================= EXAMEN 2 =================

def esAncestro(heap,A,B):
    indx = heap.index(B)
    while indx > 0:
        print(indx, " ", heap[indx])
        if heap[indx] == A:
            return True
        indx = (indx)//2
    return False

# print(esAncestro([0,100,19,36,17,3,25,1,2,7],19,7))
# print(esAncestro([0,100,19,36,17,3,25,1,2,7],7,1))

def rutasHojas(T):
    paths = []
    stack = [(T,[T[0]])]
    while stack != []:
        tree, path = stack.pop()
        V,L,R = tree
        if L == [] and R ==[]:
            paths.append(path)
        if L != []:
            stack.append((L,path+[L[0]]))
        if R != []:
            stack.append((R,path+[R[0]]))
    return paths

# print(rutasHojas([1,[2,[],[]],[3,[],[]]]))
# print(rutasHojas([1,[2,[3,[],[]],[]],[]]))

def LCA(T,A,B):
    if T == []:
        return 0
    V, L, R = T
    if V == A: return V
    if V == B: return V
    lValue = LCA(L,A,B)
    rValue = LCA(R,A,B)
    if (lValue == A or lValue == B) and (rValue == A or rValue == B):
        return V
    if lValue > 0:
        return lValue
    if rValue > 0:
        return rValue
    return 0

# print(LCA([1,
# [2,
# [3,[],[]],
# [4,[],[]] ],
# [5,
# [6,[],[]],
# [7,
# [8,[],[]],
# []] ]],
# 6,8))

# nose como hacer lo de gato lol lmao en plan holy shit lol xd
def genBST(pre):
    if not pre:
        return []
    tree, _ = generarBST(pre)
    return tree

def generarBST(pre,lower = -99999999,upper = 9999999):
    if not pre or pre[0] > upper or pre[0] < lower:
        return [], pre

    root_val = pre.pop(0)
    root = [root_val,[],[]]

    root[1], preorder = generarBST(pre,lower,root_val)
    root[2], preorder = generarBST(pre,root_val,upper)

    return root,pre

# print(genBST([3,1,5]))

def arbol(node,dic):
    return [node, [arbol(child, dic) for child in dic[node]]]

def BSTdeImpares(alt):
    totalNodes = 2**(alt+1)-1
    odds = [(2 * i) + 1 for i in range(totalNodes)]
    return BSTdeI_aux(odds,0,totalNodes-1)

def BSTdeI_aux(odds,start,end):
    if start>end:
        return []
    mid = (start + end) // 2
    root_val = odds[mid]
    left_subtree = BSTdeI_aux(odds,start,mid-1)
    right_subtree = BSTdeI_aux(odds,mid+1,end)
    return [root_val,left_subtree,right_subtree]
    
print(BSTdeImpares(2))
















