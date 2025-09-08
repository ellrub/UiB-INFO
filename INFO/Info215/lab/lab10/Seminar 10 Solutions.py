import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Task 1.1
G1 = nx.Graph()

G1.add_edge("0", "1")
G1.add_edge("0", "2")
G1.add_edge("0", "3")
G1.add_edge("0", "4")
G1.add_edge("1", "3")
G1.add_edge("2", "3")
G1.add_edge("2", "4")
G1.add_edge("2", "5")
G1.add_edge("3", "5")
#G1.add_edge("1", "0")
#G1.add_edge("2", "0")
#G1.add_edge("3", "0")
#G1.add_edge("3", "1")
#G1.add_edge("3", "1")
#G1.add_edge("3", "2")
#G1.add_edge("4", "0")
#G1.add_edge("4", "2")
#G1.add_edge("5", "2")
#G1.add_edge("5", "3")

# Half of these are redundant since the graph is by default undirected
# I have commented those out

pos = nx.spring_layout(G1, seed=6)
nx.draw(G1, pos, with_labels=True)
plt.show()


# Task 1.2

# Create/Draw an adjacency matrix based on the following graph:
#     A B C D E
#   A 0 1 1 0 1
#   B 1 0 0 0 0
#   C 1 0 0 1 1
#   D 0 0 1 0 1
#   E 1 0 1 1 0


# Task 2.1 - Graph Density: manually

# Graph 1.1
# density = 2*9/6(6-1) = 0.6

# Graph 1.2
# density = 2*6/5(5-1) = 0.6



# Task 2.2 - Graph Density - using code

n = len(G1.nodes())
m = len(G1.edges())

G1_density = 2*m/(n*(n-1))
print("\nDensity of graph 1.1: ", G1_density)

# Task 3.1
G_karate = nx.karate_club_graph()
nx.write_graphml(G_karate, 'karateclub.graphml')

k_density = nx.density(G_karate)
deg_centrality = nx.degree_centrality(G_karate)
close_centrality = nx.closeness_centrality(G_karate)
between_centrality = nx.betweenness_centrality(G_karate)

print("\nDensity of karate club: ", k_density)

print("\nDegree centrality of karate club: ", deg_centrality)
print("\nCloseness centrality of karate club: ", close_centrality)
print("\nBetweeness centrality of karate club: ", between_centrality)



# Task 3.2



degrees = G_karate.degree() #Dict with Node ID, Degree
nodes = G_karate.nodes()

n_color = np.asarray([degrees[n] for n in nodes])

degree_size = np.asarray([deg_centrality[n]*500 for n in nodes])
closeness_size = np.asarray([close_centrality[n]*300 for n in nodes])
between_size = np.asarray([between_centrality[n]*1000 for n in nodes])

degree_options = {
    "node_color": n_color,
    "node_size": degree_size,
    "cmap" : plt.cm.Reds,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.4,
    "with_labels" : True,
}

closeness_options = {
    "node_color": n_color,
    "node_size": closeness_size,
    "cmap" : plt.cm.Reds,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.4,
    "with_labels" : True,
}

between_options = {
    "node_color": n_color,
    "node_size": between_size,
    "cmap" : plt.cm.Reds,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.4,
    "with_labels" : True,
}

pos = nx.spring_layout(G_karate, seed=6)

nx.draw(G_karate, pos, **degree_options)
plt.show()

nx.draw(G_karate, pos, **closeness_options)
plt.show()

nx.draw(G_karate, pos, **between_options)
plt.show()



# Task 3.3


eigenvector = nx.eigenvector_centrality(G_karate, max_iter=100, tol=1e-06, nstart=None, weight=None)

#n_color = np.asarray([eigenvector[n] for n in nodes])

eigen_color = []
for n in nodes:
    color = ""
    if eigenvector[n] > 0.20:
        color = "blue"
    else:
        color = "red"
    eigen_color.append(color)

eigenvector_options = {
    "node_color": eigen_color,
    "node_size": between_size,
    "cmap" : plt.cm.Reds,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.4,
    "with_labels" : True,
}

nx.draw(G_karate, pos, **eigenvector_options)
plt.show()



# Task 4.1

GS = nx.Graph()

GS.add_edge("Bob", "Mike")
GS.add_edge("Bob", "John")
GS.add_edge("Bob", "Jill")
GS.add_edge("John", "Jill")
GS.add_edge("John", "Leah")
GS.add_edge("Leah", "Shane")
GS.add_edge("Leah", "Jill")
GS.add_edge("Leah", "Shane")
GS.add_edge("Shane", "Emma")
GS.add_edge("Shane", "Jill")
GS.add_edge("Shane", "Liz")
GS.add_edge("Mike", "Emma")
GS.add_edge("Mike", "Jill")
GS.add_edge("Jill", "Emma")
GS.add_edge("Emma", "Liz")
GS.add_edge("Liz", "Allen")
GS.add_edge("Allen", "Lisa")
GS.add_edge("Emma", "Bob")
GS.add_edge("John", "Shane")


pos = nx.spring_layout(GS, seed=6)
nx.draw(GS, pos, with_labels = True)
#plt.show()


k_density = nx.density(GS)

deg_centrality = nx.degree_centrality(GS)
close_centrality = nx.closeness_centrality(GS)
between_centrality = nx.betweenness_centrality(GS)
#
# print("\nDensity of Task 4: ", k_density)
# print("\nDegree centrality of Task 4: ", deg_centrality)
# print("\nCloseness centrality Task 4: ", close_centrality)
# print("\nBetweeness centrality Task 4: ", between_centrality)
