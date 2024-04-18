def create_adjacency_list(directed=False):
    with open("rosalind_ts.txt") as f:
        n,m=[int(x) for x in f.readline().split(" ")]
        adjacency_list= [[] for _ in range(n)]
        for i in range(m):
            u,v= [int(x) for x in f.readline().split(" ")]
            u-=1
            v-=1
            adjacency_list[u].append(v)
            if not directed:
                adjacency_list[v].append(u)

    return(adjacency_list)

adj= create_adjacency_list(directed=True)
#print(adj)
#print(create_adjacency_list(directed=True))
#print(adj)
#While addressing Nodes in arrays
#We do -1 because of Indexing
#Hash tables(dict) could also be used as adj lists
def dfs(adjacency_list,s,parent=None,order=None):
    if parent is None:
        parent = [None for v in adjacency_list]
        parent[s]=s
        order=[]
    for v in adjacency_list[s]:
        if parent[v] is None:
            parent[v]=s
            dfs(adjacency_list,v,parent,order)
    order.append(s)
    return parent,order

def full_dfs(adjacency_list):
    connected_components=0
    parent=[None for v in adjacency_list]
    #print(len(parent))
    order=[]
    for v in range(len(adjacency_list)):
        #print(v)
        if parent[v] is None:
            parent[v]=v
            connected_components+=1

            #print(f"normal v:{v}")

            dfs(adjacency_list,v,parent,order)
            #print(f"Fucker v:{v}")
    return parent,order,connected_components
parent,order,cc=full_dfs(adj)
parent=list(map(lambda x:x+1,parent))
order=list(map(lambda x:str(x+1),order))
print(" ".join(order[::-1]))