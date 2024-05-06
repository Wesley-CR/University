def permutations(list,n):
    perms = []
    for k in range(len(list)):
        temp = []
        for _ in range(n):
            temp.append(list[k])
        perms.append(temp)
    return perms

tstLst = [1,2]
print(permutations(tstLst,3))
