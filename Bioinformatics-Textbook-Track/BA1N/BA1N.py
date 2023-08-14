import time




def HammingDistance(p,q):
    distance=0
    for i in range(len(p)):
        #print(p,q,sep="*")
        if p[i]!=q[i]:
            distance+=1
    return distance
def Neighbors(pattern,d):
    if d==1:
        neighbors=set()
        for i in range(len(pattern)):
            bases= {'A','T','C','G'}
              
            base_to_mutated = pattern[i]
            bases.remove(base_to_mutated)
            
            neighbors.update({pattern[:i]+x+pattern[i+1:] for x in bases})
        return neighbors
    else:
        neighbors = set()
        for neighbor in Neighbors(pattern,d-1):

            
            neighbors.update(Neighbors(neighbor,1))
        return neighbors

#Another approach:
def Neighbors2(pattern,d):
    bases=['A','C','G','T']
    if d==0:
        return pattern
    if len(pattern)==1:
        return {'A','C','G','T'}
    suffixpattern = pattern[1:]
    firstsymbol = pattern[0]
    Neighborhood=set()
    for i in Neighbors2(suffixpattern,d):
        if HammingDistance(i,suffixpattern)<d:
            for base in bases:
                new = base+i
                Neighborhood.add(new)
            
        else:#HammingDistance==d
            new = firstsymbol+i
            Neighborhood.add(new)
        
    return Neighborhood

pattern='CTTATTAG'






#print("\n".join(Neighbors(pattern,2)))

start = time.time()
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1N\rosalind_ba1n_solution.txt','w') as f:
    f.write("\n".join(Neighbors(pattern,3)))
end = time.time()
print(end - start)

start = time.time()
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1N\rosalind_ba1n_solution.txt','w') as f:
    f.write("\n".join(Neighbors2(pattern,3)))
end = time.time()
print(end - start)


with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1N\rosalind_ba1n_solution.txt','w') as f:
    f.write("\n".join(Neighbors(pattern,3)))
#print(len(Neighbors(pattern,2)))
#print(list(set(Neighbors(pattern,2))))s
#print(len(list(set(Neighbors(pattern,2)))))
