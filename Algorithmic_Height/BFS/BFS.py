def create_adjacency_list(directed=False):
    with open("rosalind_bfs.txt") as f:
        n,m=[int(x) for x in f.readline().split(" ")]
        adjacency_list= [[] for _ in range(n)]
        for i in range(m):
            u,v= [int(x) for x in f.readline().split(" ")]
            adjacency_list[u-1].append(v)
            if not directed:
                adjacency_list[v-1].append(u)

    return(adjacency_list)

adj= create_adjacency_list(directed=True)
#print(create_adjacency_list(directed=True))
#print(adj)
#While addressing Nodes in arrays
#We do -1 because of Indexing
#Hash tables(dict) could also be used as adj lists

def BFS(adj: 'adjacency list',s:'source node'):
    n= len(adj)
    parent = [None]*n
    distance=[-1]*n
    distance[s-1]=0
    parent[s-1]=s
    levels = [[s]]
    while len(levels[-1])>0:
        levels.append([])
        for u in levels[-2]:
            for v in adj[u-1]:
                if parent[v-1] is None:
                    parent[v-1]=u
                    levels[-1].append(v)
                    distance[v-1]=len(levels)-1
            
    return distance      

with open("output.txt",'w') as f:
    f.write(" ".join([str(x) for x in BFS(adj,1)]))