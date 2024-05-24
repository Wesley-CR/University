# Prereqs
def expo_log(number,exp):
    if exp <= 0: return 1
    res = expo_log(number,exp//2)
    res *= res
    if exp%2 == 0:
        return res
    return res*number

def sqrtA(n,min,max,p=1e-6):
    m = (min+max)/2
    if (m**2)-p < n and (m**2)+p> n:
        return m
    if (m**2)>n:
        return sqrtA(n,min,m)
    return sqrtA(n,m,max)

def sqrtW(n):
    return sqrtA(n,1,n)

#1. Maximo
def max_in_vector(vector):
    max = vector [0]
    index = 0
    for i in range(len(vector)):
        if vector[i] > max:
            max = vector[i]
            index = i
    return max,index

testList = [3,-1,5.2,7,3,6,9,5,7,2,9]
#print(max_in_vector(testList))

#2. Minimo
def min_in_vector(vector):
    min = vector[0]
    index = 0
    for i in range(len(vector)):
        if vector[i] < min:
            min = vector[i]
            index = i
    return min,index
#print(min_in_vector(testList))

#3. Multiply scalar by vector
def scale_vector(vector,scale):
    for i in range(len(vector)):
        vector[i]=vector[i]*scale
    return vector
#print(scale_vector(testList,2))

#4. Sum of vectors
def sum_of_vectors(vector1,vector2):
    res = []
    for i in range(len(vector1)):
        res.append(vector1[i]+vector2[i])
    return res
#print(sum_of_vectors(testList,testList))

#5. Recursive dot product
def dot_product(vector1,vector2,res=0):
    if vector1 == []:
        return res
    return dot_product(vector1[1:],vector2[1:],res + vector1[0] * vector2[0])
#print(dot_product(testList,testList))

#6. Solution of a polynomial
def find_factors(number,firstCoeficient):
    factors = []
    number = abs(number)
    for i in range(1,(number//2)+1):
        if number % i == 0:
            factors.append(i/firstCoeficient)
            factors.append((-1*i)/firstCoeficient)
    factors.append(number/firstCoeficient)
    factors.append((-1*number)/firstCoeficient)
    return factors

def synthetic_division(coeficients,div):
    res = []
    res.append(coeficients[0])
    for i in range(1,len(coeficients)):
        if (coeficients[i]+(res[i-1]*div)) == 0:
            continue
        res.append(coeficients[i]+(res[i-1]*div))
    return res

import math
def bhaskara(coeficients):
    discriminant = (coeficients[1]**2) - (4*(coeficients[0]*coeficients[2]))
    #I literally dont understand why my sqrt doesn't work
    x1 = (-coeficients[1]+math.sqrt(discriminant))/(2*coeficients[0])
    x2 = (-coeficients[1]-math.sqrt(discriminant))/(2*coeficients[0])
    return x1,x2

def sol_polynomial(coeficients):
    coefLen = len(coeficients)
    res = []
    factors = find_factors(coeficients[coefLen-1],coeficients[0])
    for factor in factors:
        tmp = 0
        for i in range(coefLen,1,-1):
            #print(i, " Exponente:", i-1, " Coeficiente:", coeficients[coefLen-i], " Factor:", factor)
            tmp += coeficients[coefLen-i]*(factor**(i-1))
            #print(tmp)
        tmp+=coeficients[coefLen-1]
        #print("final temp:", tmp, " factor: ", factor)
        if int(tmp) == 0:
            res.append(factor)
            #print(synthetic_division(coeficients,factor))
            res.append(bhaskara(synthetic_division(coeficients,factor))[0])
            res.append(bhaskara(synthetic_division(coeficients,factor))[1])
            break
    return res

# print(sol_polynomial([1,8,11,-20]))
# print(sol_polynomial([1,2,-5,-6]))
# print(sol_polynomial([1,0,-11,6]))

#7. Distance between vectors
def distance_vectors(vector1,vector2):
    sum = 0
    for i in range(len(vector1)):
        sum += expo_log(vector1[i]-vector2[i],2)
    return sqrtW(sum)

# testVector1 = [1,2,3,4,5]
# testVector2 = [6,7,8,9,10]
# print(distance_vectors(testVector1,testVector2))

#8. Vector X degrees from another vector
#comically large function name btw
def vector_x_degrees_from_vector(vector1):
    ratio = vector1[1] / vector1[0]
    newY = ratio*math.degrees(math.cos(math.radians(25)))
    return [vector1[0],newY]
#Idk why this doesnt work and how can this be done without math library lol
# print(vector_x_degrees_from_vector([3,9]))
# print(synthetic_division([2,1,-11,11,-3],1))
# print(synthetic_division([2,1,-11,11,-3],3))

#MATRICES

#1. Gauss-Jordan
# I coulnt do this by myself so
# This solution is from https://www.geeksforgeeks.org/program-for-gauss-jordan-elimination-method/
# (I made the time to understand it)
def print_M(M):
    for i in range(len(M)):
        print(M[i])

def gauss_jordan_aux(M):
    flag = 0
    n = len(M)
    for i in range(n):
        if M[i][i] == 0:
            c=1
            while (i+c) < n and M[i+c][i]==0:
                c+=1
            if i+c == n:
                flag = 1
                break
            j = i
            for k in range(1+n):
                tmp = M[j][k]
                M[j][k] = M[j+c][k]
                M[j+c][k] = tmp

        for j in range(n):
            if i!=j:
                p = M[j][i] / M[i][i]
                k = 0
                for k in range(n+1):
                    M[j][k] = M[j][k] - (M[i][k] * p)
    return flag

def results(M,flag):
    n = len(M)
    if flag == 2:
        print("existen soluciones infinitas")
    elif flag == 3:
        print("No tiene soluciones")
    else:
        for i in range(n):
            print(M[i][n] / M[i][i])

def check_consistency(M,flag):
    n = len(M)
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += M[i][j]
        if sum == M[i][j]:
            flag = 2
    return flag

def gauss_jordan(M):
    flag = gauss_jordan_aux(M)
    if flag == 1:
        flag = check_consistency(M,flag)
    print("Matriz en forma Echelon:")
    print_M(M)
    results(M,flag)

# gauss_jordan([[0, 2, 1, 4],[1, 1, 2, 6],[2, 1, 1, 7]])

#2. Matrix exponentiation
def nul_mat(m,n):
    return [[0 for i in range(n)] for i in range(m)]

def indentity_matrix(m):
    res = nul_mat(m,m)
    for i in range(m):
        res[i][i] = 1
    return res

def dotPoint(v1,v2):
    r = 0
    for i in range(len(v1)):
        r += v1[i]*v2[i]
    return r

def transpose_M(M):
    r = [[0 for i in range(len(M))]for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
           r[j][i] = M[i][j]
    return r

def mat_Mult(A,B):
    return [[dotPoint(row,col) for col in transpose_M(B)]for row in A]

def mat_exp(M,n):
    if n == 0: return indentity_matrix(len(M))
    r = mat_exp(M,n//2)
    r = mat_Mult(r,r)
    if n%2: r = mat_Mult(r,M)
    return r

def tribonacci(n):
    A = [[0,1,0],
         [0,0,1],
         [1,1,1]]

    B = [[1],
         [1],
         [1]]
    return mat_Mult(mat_exp(A,n),B)
# LISTS

#1. Last n's in list
def last_n_in_list(M,n):
    res = []
    for _ in range(n):
        res.append(M.pop())
    return res

# print(last_n_in_list(testList,3))

#2. Sort a list
def quickSort(List):
    if List == []: return List
    men = []
    may = []
    for element in List[1:]:
        if element < List[0]:
            men.append(element)
        else:
            may.append(element)
    return quickSort(men)+[List[0]]+quickSort(may)

# print(quickSort(testList))

#3. Does it have sublists?!
#I was thinking of trying to access an index and
#catching the error if it didnt worked but idk
def sublists_question_mark(List):
    for i in range(len(List)):
        if isinstance(List[i],list):
            return True
    return False

test2List = [2,[3,4]]
# print(sublists_question_mark(test2List))

#4. Find if there is a sublist between i and j
def sublist_between_i_and_j_question_mark(L,i,j):
    for x in range(i,j):
        if isinstance(L[i],list):
            return x,True
    return False

# print(sublist_between_i_and_j_question_mark(testList,3,5))
# print(sublist_between_i_and_j_question_mark(test2List,1,2))

#5. Multiples of K in a list
def multiples_in_list(L,k):
    counter = 0
    for i in range(len(L)):
        if L[i] % k == 0:
            counter += 1
    return counter

# print(multiples_in_list(testList,3))

#6. First n positive integers
def first_n_positive_integers(L):
    res = []
    for i in range(len(L)):
        if L[i] == int(L[i]) and L[i] > 0:
            res.append(L[i])
    return res

# print(first_n_positive_integers(testList))

#7. First n primes
def is_prime(n):
    if n != int(n):return False
    if n <= 1: return False
    if n%2 == 0: return False
    for i in range(2,int((n/2)+1)):
        if n%i == 0:
            return False
    return True

def first_n_primes(L,n):
    primes = []
    for i in range(len(L)):
        if n == 0: return primes
        if is_prime(L[i]):
            primes.append(L[i])
            n -= 1
    return primes

# print(first_n_primes(testList,5))

#8. Swap elements in a list
def swap_elements(L,i,j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
    return L

# print(testList)
# print(swap_elements(testList,2,4))

#9. replace elements A with B
def replace_elements(L,a,b):
    for i in range(len(L)):
        if L[i] == a: L[i] = b
    return L

# print(testList)
# print(replace_elements(testList,3,100))

#10. Multiply elements of a list
def scalar_product_of_elements(L):
    if L == []: return L
    res = 1
    for i in range(len(L)):
        res *= L[i]
    return res

# print(scalar_product_of_elements(testList))

#11. Eliminate duplicates
def eliminate_duplicates(L):
    L = quickSort(L)
    for i in range(len(L)):
        if i+1 < len(L) and L[i] == L[i+1]:
            L.pop(i)
    return L

# print(eliminate_duplicates(testList))

#12. Invert list
def invert_list(L):
    newList = L.copy()
    res = []
    for i in range(len(newList)):
        res.append(newList.pop())
    return res

# print(invert_list(testList))

#13. is palindrome
def is_palindrome(L):
    if L == invert_list(L):
        return True
    else:
        return False

palindrom_list = [3,1,2]
# print(is_palindrome(palindrom_list))

#14 combinations
def combinations(L):
    combs = []
    for i in range(len(L)):
        for j in range(i,len(L)):
            if L[i] != L[j]:
                combs.append([L[i]]+[L[j]])
    return combs

# print(combinations([6,7,8]))

#15. permutations
def permutations(L):
    if len(L) == 0: return []
    if len(L) == 1: return [L]
    l = []
    for i in range(len(L)):
        m = L[i]
        rest = L[:i]+L[i+1:]
        for item in permutations(rest):
            l.append([m] + item)
    return l

# print(permutations(['A','B','C']))
aa = [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'A', 
'B'], ['C', 'B', 'A']]
a = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
for i in range(len(aa)):
    print(permutations(aa[i]))

#16. set exponentiation
def set_exponentiation(L,exp):
    if exp == 0: return [()]
    if exp == 1: return L
    expSet = set_exponentiation(L,exp-1)
    cartesianProduct = []
    for element in L:
        for element2 in expSet:
            cartesianProduct.append((element,element2))
    return cartesianProduct

# testSet = [0,1]
# exp = 2
# print(set_exponentiation(testSet,exp))



















