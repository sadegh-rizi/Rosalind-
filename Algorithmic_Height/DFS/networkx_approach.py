import networkx as nx
with open("rosalind_cc.txt", "r+") as f:
    edges = []
    for edge in f.readlines():
        edges.append(list(map(int, edge.replace('\n', '').split(' '))))

graph = nx.Graph()
graph.add_nodes_from(range(1, edges[0][0] + 1))
graph.add_edges_from(edges[1:])
print(nx.number_connected_components(graph))