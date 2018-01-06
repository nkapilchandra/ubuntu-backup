def distance(source,target,i,j):
    if (i == None and j == None):
        i = len(source) - 1
        j = len(target) - 1
    if (i == 0 and j == 0):
        if (source[i] != target[j]):
            return 1
        return 0
    if (i == 0):
        return j
    if (j == 0):
        return i

    if (source[i] == target[j]):
        return min(distance(source,target,i-1,j)+1, distance(source,target,i,j-1)+1, distance(source,target,i-1,j-1))
    else:
        return min(distance(source,target,i-1,j)+1, distance(source,target,i,j-1)+1, distance(source,target,i-1,j-1)+1)

print(distance('algor','logar',None,None))
