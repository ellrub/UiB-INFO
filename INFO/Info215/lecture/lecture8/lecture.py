import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph([("A", "eggs")])
G.add_node("spinach") # Add a single node
G.add_node("Hg") # Add a single node by mistake
G.add_nodes_from(["folates", "asparagus", "liver"]) # Add a list of nodes
G.add_edge("spinach", "folates") # Add one edge, both ends exist
G.add_edge("spinach", "heating oil") # Add one edge by mistake
G.add_edge("liver", "Se") # Add one edge, one end does not exist
G.add_edges_from([("folates", "liver"), ("folates", "asparagus")])

print(repr(G.nodes))

# Undirected graphs consist only of undirected edges. To create an empty undirected 
# graph with no nodes and no edges, we can use the following code:
# G = nx.Graph()

# Directed graphs, also known as digraphs, have at least one directed edge. Create 
# an empty directed graph with the constructor:
# G = nx.DiGraph()

# Multigraphs are like undirected graphs, but they can have parallel edges —multiple 
# edges between the samenodes. Create an empty multigraph with the constructor 
# G = nx.MultiGraph()

# Finally, directed multigraphs are what they say they are: directed graphs with parallel 
# edges. Create an empty directed multigraph with the constructor:
# G = nx.MultiDiGraph()

# Adding nodes one by one.
# G.add_node("spinach") # Add a single node
# G.add_edge("spinach", "folates")

# Adding nodes from a list:
# G.add_nodes_from(["folates", "asparagus", "liver"]) # Add a list of nodes
# G.add_edges_from([("folates", "liver"), ("folates", "asparagus")])
# Adding a duplicate node or edge is silently ignored unless the graph is a multigraph; 
# in the latter case, anadditional parallel edge is created.

# Removing an edge does not remove its end nodes.
# Removing a node removes all incident edges.
# Example:
# G.remove_edge("spinach", "heating oil")
# G.remove_edges_from([("spinach", "heating oil"), ]) # safe to remove missing edge using a list
# G.remove_node("spinach")
# G.remove_nodes_from(["Hg",]) # Safe to remove a missing node using a list

# Node labels are the keys of G.nodes. Node attributes, in the form of nested dictionaries, 
# are the values.
# print(G.nodes)
# > {'Se': {}, 'eggs': {}, 'asparagus': {}, 'A': {}, 'liver': {}, 'spinach': {}, 'folates': {}}

# If called with the optional parameter data=True, the methods return the lists with the additional 
# attribute dictionaries.
# print(G.nodes(data=True))
# ❮ [('Se', {}), ('eggs', {}), ('asparagus', {}), ('A', {}), ('liver', {}), ('spinach', {}), ('folates', {})]
# print(G.edges(data=True))
# ❮ [('Se', 'liver', {}), ('eggs', 'A', {}), ('asparagus', 'folates', {}), ('liver', 'folates', {}), ('spinach', 'folates', {})]