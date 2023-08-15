nodes=[]

with open(r'D:\Python Codes\Rosalind-\Algorithmic_Height\Double_Degree_Array\rosalind_ddeg.txt') as f:
    n_nodes,n_edges = [int(i) for i in f.readline().strip().split()]
    adjacency_list={key:[] for key in range(1,n_nodes+1)}
    nodes_degree = n_nodes*[0]

    lines = f.readlines()
    for line in lines:
        u,v = [int(i) for i in line.strip().split()]
        nodes_degree[u-1]+=1
        nodes_degree[v-1]+=1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

#print(nodes_degree)
#print(adjacency_list)
for i in adjacency_list:
     print(sum(map(lambda x : nodes_degree[x-1],adjacency_list[i])),end=' ')
"""
nodes_without_repeat = list(range(1,n_nodes+1))
result= list(map(lambda x: str(nodes.count(x)),nodes_without_repeat))
print(" ".join(result))

B = list(map(int, open('rosalind_deg.txt', 'r').read().strip().replace('\n', ' ').split(' ')))
print(*[B[2:].count(i) for i in range(1, B[0]+1)], end = ' ')"""