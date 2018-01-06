def distance(source,target):
    delta = {True:0,False:1}
    table = [[0 for col in range(len(target)+1)] for row in range(len(source)+1)]

    table[0][0] = 0
    for i in range(1,len(source)+1):
        table[i][0] = table[i-1][0] + 1
    for j in range(1,len(target)+1):
        table[0][j] = table[0][j-1] + 1

    for i in range(len(source)):
        for j in range(len(target)):
            table[i+1][j+1] = min(table[i][j]+delta[source[i]==target[j]],table[i+1][j]+1,table[i][j+1]+1)
    print (table)
    return table[-1][-1]

print(distance('algor','logar'))
