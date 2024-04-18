def get_graphs():
    with open("rosalind_dag.txt") as f:
        n=int(f.readline())
        for i in range(n):
            if f.readline()=='\\n':
                pass
            else:
                adj=create_adjacency_list(f,directed=True)
                print(full_dfs(adj),end=" ")

def create_adjacency_list(f,directed=False):
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


#print(create_adjacency_list(directed=True))
#print(adj)
#While addressing Nodes in arrays
#We do -1 because of Indexing
#Hash tables(dict) could also be used as adj lists
def dfs(adjacency_list,s,parent=None,order=None,ancestor_stack=[]):
    cycle=False

    #print(ancestor_stack)
    ancestor_stack.append(s)

    if parent is None:
        parent = [None for v in adjacency_list]
        
        parent[s]=s
        order=[]
    for v in adjacency_list[s]:
        if parent[v] is None:
            parent[v]=s

            dfs(adjacency_list,v,parent,order,ancestor_stack)
        
        if v in ancestor_stack:
            cycle=True
           # print('y')
            return parent,order,cycle

     #       print(f"{v}:y")
            #We have a back edge
    order.append(s)
    ancestor_stack.pop()
    return parent,order,cycle

def full_dfs(adjacency_list):

    cycle=False
    parent=[None for v in adjacency_list]
    ancestor_stack=[]
    #print(len(parent))
    order=[]
    for v in range(len(adjacency_list)):
        #print(v)
        if parent[v] is None:
            parent[v]=v

            #print(f"normal v:{v}")

            parent,order,cycle=dfs(adjacency_list,v,parent,order,ancestor_stack)
            if cycle==True:
                return -1
    return 1


get_graphs()