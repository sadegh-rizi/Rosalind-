
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1G\rosalind_ba1g.txt') as f:
    p=f.readline().strip()
    q=f.readline().strip()
#p="GGGCCGTTGGT"
#q="GGACCGTTGAC"
def HammingDistance(p,q):
    distance=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            distance+=1
    return distance
distance = sum(1 for i,j in zip(p,q) if i!=j)
print(distance)
print(HammingDistance(p,q))