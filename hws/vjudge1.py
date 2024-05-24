#Problem A
friends, fenceHeight = map(int, input().split(' '))
friendsHeightsList = list(map(int, input().split(' ')))
roadWidth = 0
for i in range(len(friendsHeightsList)):
    if friendsHeightsList[i] > fenceHeight:
        roadWidth += 2
    else:
        roadWidth += 1
print(roadWidth)