import networkx as nx
import matplotlib.pyplot as plt
def to_bin(n,k):
    ans = ''
    while (n>0):
        rem = n%2
        ans = str(rem) + ans
        n = n//2
    while (len(ans) != k):
        ans = '0' + ans
    return ans

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

class my_stack:
    def __init__(self,inp = []):
        self._array = inp
    def __len__(self):
        return len(self._array)
    def push(self,item):
        self._array.append(item)
    def pop(self):
        return self._array.pop()
    def top(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        else:
            return self._array[-1]
    def is_empty(self):
        return (len(self._array)==0)
    def show(self):
        return self._array
    def __repr__(self):
        return str(self._array)


G = nx.Graph()
# def make_graph():
#     G.add_edges_from([(1,2),(1,3),(1,4),(2,5),(2,6),(3,6),(4,7),(4,8)])
#
# make_graph()
# nx.draw(G,with_labels=True)
# plt.show()

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

    # for i in range(count):
    #     print(G.degree(i))
hcube(5)

def DFS(G,start_node):
    i = list(nx.nodes(G))[start_node]
    undiscovered = nx.nodes(G)
    process = my_stack()
    discovered = []
    final = []
    process.push(i)
    discovered.append(i)
    while(process.is_empty() == False):
        neighbors = list(nx.all_neighbors(G,i))
        for _ in neighbors:
            if _ not in discovered:
                discovered.append(_)
                process.push(_)
        i = process.pop()
        final.append(i)
    final = final[:-2]
    print('final = ',final)
# DFS(G,0)


def BFS(G,start_node):
    i = list(nx.nodes(G))[start_node]
    undiscovered = nx.nodes(G)
    process = []
    discovered = []
    final = []
    process.append(i)
    while(len(process) != 0):
        neighbors = list(nx.all_neighbors(G,i))
        for _ in neighbors:
            if _ not in discovered:
                discovered.append(_)
                process.append(_)
        i = process.pop(0)
        final.append(i)
    print('final = ',final)
BFS(G,0)
