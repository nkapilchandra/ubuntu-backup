#BT3051 Assignment 4
#Roll Number: MM14B022
#Collaborators: None
#Time: 0:35

import networkx as nx
import matplotlib.pyplot as plt
import random

def barabasi_albert_graph(G, nNodes, mLinks):
    # G is an initial graph, which should be an nx.Graph type of object
    # nNodes is the number of nodes to add to G
    # mLinks is the number of links that get added from a new node to existing nodes in each iteration
    G_new = G.copy()

    # CODE FOR graph creation

    G_new.add_edge(1,2)
    count = 0 # Variable to check how many nodes have been added
    nx.draw(G_new,with_labels=True)
    # plt.show()
    while (count <= nNodes):
        added = 0 # Variable to check how many links have been added
        while (added<mLinks):
            num = G_new.number_of_nodes()
            r = random.randint(1,num) # Randomly select a node
            deg = G_new.degree(r)
            total_deg = sum(list(dict(G_new.degree(list(range(1,num+1)))).values()))
            prob = deg/total_deg # Probability at each node based on its degree
            threshold = random.random() # Random generated threshold to decide if the link must be made
            if (prob>threshold):
                G_new.add_edge(r,count+3)
                added += 1
            if (added >= mLinks):
                break

        count += 1
        if (count >= nNodes):
            nx.draw(G_new,with_labels=True)
            plt.show()
            print(G_new.number_of_nodes())
            break



if __name__ == '__main__':
    G = nx.Graph()
    G.add_edge(1,2)
    G_new = barabasi_albert_graph(G,98,1)
