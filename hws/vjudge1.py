#Problem A
# friends, fenceHeight = map(int, input().split(' '))
# friendsHeightsList = list(map(int, input().split(' ')))
# roadWidth = 0
# for i in range(len(friendsHeightsList)):
#     if friendsHeightsList[i] > fenceHeight:
#         roadWidth += 2
#     else:
#         roadWidth += 1
# print(roadWidth)

#Problem B
# bearA, bearB = map(int, input().split(' '))
# counter = 0
# while bearA <= bearB:
#     bearA=bearA*3
#     bearB=bearB*2
#     counter+=1
# print(counter)

#Problem C
# input()
# numbersList = list(map(int, input().split(' ')))
# sum = 0
# for i in range(len(numbersList)):
#     sum += numbersList[i]
# print(sum)

#Problem D
# magnets = int(input())
# tmp = int(input())
# groups = 1
# for i in range(magnets-1):
#     tmp2 = int(input())
#     if tmp2//10 == tmp%10:
#         groups += 1
#     tmp = tmp2
# print(groups)

# Problem E
# colors = int(input())
# colorsList = input()
# popQ = 0
# for i in range(len(colorsList)-1):
#     if colorsList[i] == colorsList[i+1]:
#         popQ += 1
# print(popQ)

#Problem K
# string = input()
# count = 0
# for x in string:
#     if x == '|':
#         count += 1
# if count%2 == 0:
#     if string[(len(string)-1)//2] == '(' and string[((len(string)-1)//2)+1] == ')':
#         print("correct")
#     else:
#         print("fix")
# else:
#     print("fix")

# Problem L

