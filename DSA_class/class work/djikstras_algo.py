import matplotlib.pyplot as plt
import networkx as nx


class priority_queue:
    def __init__(self,inp={}):
        self._array = inp
    def __len__(self):
        return len(self._array)
    def push(self,item,weight):
        self._array[item] = weight
    def pop(self):
        key = list(self._array.keys())[0]
        val = self._array[key]
        for keys in self._array:
            if self._array[key] > self._array[keys]:
                key = keys
                val = self._array[keys]
        temp = key
        del self._array[key]
        return temp
    # def top(self):
    #     if self.is_empty():
    #         raise IndexError("The queue is empty")
    #     else:
    #         return self._array[-1]
    def is_empty(self):
        return (len(self._array)==0)
    def show(self):
        return self._array
    def __repr__(self):
        return str(self._array)


G = nx.Graph()
Q = priority_queue()
def make_graph():
    G.add_weighted_edges_from([(1,2,1),(1,3,2),(1,4,5),(2,3,3),(3,4,1),(4,5,1),(3,5,1)])
make_graph()
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G,with_labels=True,edge_labels=labels)
# print(labels)
# plt.show()

def djikstras(start):
    nodes = G.nodes()
    values = {}
    visited = [start]
    values[start] = 0
    for i in nodes:
        if i != start:
            values[i] = 2000
    print(list(G.neighbors(start)))
    for j in list(G.neighbors(start)):
        values[j] = G.get_edge_data(start,j)['weight']
        Q.push(j,values[j])

    while (Q.is_empty() == False):
        print('running')
        next_node = Q.pop()
        for j in list(G.neighbors(next_node)):
            if (G.get_edge_data(j,next_node)['weight']+values[next_node] < values[j]):
                values[j] = values[next_node] + G.get_edge_data(j,next_node)['weight']
                if j not in visited:
                    Q.push(j,values[j])
        visited.append(next_node)
    print(values)





djikstras(1)
new_labels = nx.get_edge_attributes(G,'weight')
print(new_labels)
