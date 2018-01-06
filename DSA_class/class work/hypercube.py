import networkx as nx
import matplotlib.pyplot as plt
from edit_distance2 import distance

G = nx.Graph()

# Function to convert Decimal number to Binary number
def to_bin(n,k):
    ans = ''
    while (n>0):
        rem = n%2
        ans = str(rem) + ans
        n = n//2
    while (len(ans) != k):
        ans = '0' + ans
    return ans


def hcube(n):
    count = 2**(n)
    nodes = {}
    dimen = [0,]*n
    cur_node = dimen
    for i in range(count):
        nodes[to_bin(i,n)] = i
    for i in nodes:
        for j in nodes:
            if (distance(i,j)== 1):
                G.add_edges_from([(nodes[i],nodes[j])])

    for i in range(count):
        print(G.degree(i))
hcube(3)
nx.draw(G,with_labels=True)
plt.show()
