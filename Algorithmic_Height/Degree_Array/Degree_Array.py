nodes=[]
with open(r'D:\Python Codes\Rosalind-\Algorithmic_Height\Degree_Array\rosalind_deg.txt') as f:
    n_nodes,n_edges = [int(i) for i in f.readline().strip().split()]
    lines = f.readlines()
    for line in lines:
        nodes += [int(i) for i in line.strip().split()]
nodes_without_repeat = list(range(1,n_nodes+1))
result= list(map(lambda x: str(nodes.count(x)),nodes_without_repeat))
print(" ".join(result))

B = list(map(int, open('rosalind_deg.txt', 'r').read().strip().replace('\n', ' ').split(' ')))
print(*[B[2:].count(i) for i in range(1, B[0]+1)], end = ' ')