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

testList = [3,7,3,6,9,5,7,2,9]
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
    hypotenuse = sqrtW(expo_log(vector1[0],2) + expo_log(vector1[1],2))
    angleInRadians = math.acos(vector1[0]/hypotenuse)
    # newAngle = 20+((angleInRadians* 180) / math.pi)
    # newAngle = math.radians(20) + angleInRadians
    ratio = vector1[1] / vector1[0]
    newY = ratio*math.degrees(math.cos(math.radians(25)))
    return [vector1[0],newY]

print(vector_x_degrees_from_vector([3,9]))
# print(synthetic_division([2,1,-11,11,-3],1))
# print(synthetic_division([2,1,-11,11,-3],3))

#MATRICES

#1. Gauss-Jordan

# Python3 Implementation for Gauss-Jordan
# Elimination Method
M = 10

# Function to print the matrix
def PrintMatrix(a, n):
    for i in range(n):
        print(*a[i])

# function to reduce matrix to reduced
# row echelon form.
def PerformOperation(a, n):
    i = 0
    j = 0
    k = 0
    c = 0
    flag = 0
    m = 0
    pro = 0

    # Performing elementary operations
    for i in range(n):
        #Busca algun cero en la indentidad
        if (a[i][i] == 0):
            #Si encuentra un 0 busca un valor no 0 debajo de la fila actual
            c = 1
            while ((i + c) < n and a[i + c][i] == 0):
                #Este loop hace que si no encuentra un 0 en la de abajo
                #busque en la otra de mas abajo
                c += 1
            if ((i + c) == n):
                #Si no encuentra un 0 rompe el loop con flag 1
                #lo que quiere decir que puede tener soluciones infinitas
                flag = 1
                break
            #En caso de encontrar el 0 intercambia
            #la fila con el 0 con la que no tiene 0
            j = i
            for k in range(1 + n):

                temp = a[j][k]
                a[j][k] = a[j+c][k]
                a[j+c][k] = temp

        for j in range(n):
            # Excluding all i == j (diagonales)
            if (i != j):
                # Converting Matrix to reduced row
                # echelon form(diagonal matrix)
                p = a[j][i] / a[i][i]
                # busca un factor p para los numeros fuera de la identidad
                k = 0
                for k in range(n + 1):
                    a[j][k] = a[j][k] - (a[i][k]) * p

    return flag

# Function to print the desired result
# if unique solutions exists, otherwise
# prints no solution or infinite solutions
# depending upon the input given.
def PrintResult(a, n, flag):

    print("Result is : ")

    if (flag == 2):
        print("Infinite Solutions Exists<br>")
    elif (flag == 3):
        print("No Solution Exists<br>")

    # Printing the solution by dividing constants by
    # their respective diagonal elements
    else:
        for i in range(n):
            print(a[i][n] / a[i][i], end=" ")

# To check whether infinite solutions
# exists or no solution exists
def CheckConsistency(a, n, flag):

    # flag == 2 for infinite solution
    # flag == 3 for No solution
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + a[i][j]
        if (sum == a[i][j]):
            flag = 2

    return flag

# Driver code
a = [[0, 2, 1, 4],  [1, 1, 2, 6],   [2, 1, 1, 7]]

# Order of Matrix(n)
n = 3
flag = 0

# Performing Matrix transformation
flag = PerformOperation(a, n)

if (flag == 1):
    flag = CheckConsistency(a, n, flag)

# Printing Final Matrix
print("Final Augmented Matrix is : ")
PrintMatrix(a, n)
print()

# Printing Solutions(if exist)
PrintResult(a, n, flag)

# This code is contributed by phasing17


