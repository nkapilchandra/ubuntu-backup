import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

# G.add_edge(1,2,weight=2.0)
def to_bin(n,k):
    ans = ''
    while (n>0):
        rem = n%2
        ans = str(rem) + ans
        n = n//2
    while (len(ans) != k):
        ans = '0' + ans
    return ans

# print(to_bin(4,4))

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

# print(distance('algor','logar',None,None))

def hcube(n):
    count = 2**(n)
    nodes = {}
    dimen = [0,]*n
    cur_node = dimen
    for i in range(count):
        nodes[to_bin(i,n)] = i
    for i in nodes:
        for j in nodes:
            if (distance(i,j,None,None)== 1):
                # print(i,j)
                G.add_edges_from([(nodes[i],nodes[j])])

    for i in range(count):
        print(G.degree(i))
hcube(2)
nx.draw(G,with_labels=True)
plt.show()
