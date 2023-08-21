import time
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1J\rosalind_ba1j.txt') as f:
    text=f.readline().strip()
    k,d=[int(i) for i in f.readline().strip().split()]

def reverse_complement(strand):
    return strand.replace("A","X").replace("C","Y").replace("G","C").replace("T","A").replace("X","T").replace("Y","G")[::-1]

#text ='ACGTTGCATGTCGCATGATGCATGAGAGCT'
#k=4
#d=1

def HammingDistance(p,q):
    distance=0
    for i in range(len(p)):
        #print(p,q,sep="*")
        if p[i]!=q[i]:
            distance+=1
    return distance


def Neighbors(pattern,d):
    bases=['A','C','G','T']
    if d==0:
        return pattern
    if len(pattern)==1:
        return {'A','C','G','T'}
    suffixpattern = pattern[1:]
    firstsymbol = pattern[0]
    Neighborhood=set()
    for i in Neighbors(suffixpattern,d):
        if HammingDistance(i,suffixpattern)<d:
            for base in bases:
                new = base+i
                Neighborhood.add(new)
            
        else:#HammingDistance==d
            new = firstsymbol+i
            Neighborhood.add(new)
    return Neighborhood
frequency_dict = {}
"""
def frequent_words_with_mismatches(text,k,d):
    frequency_dict = {}
    for i in range(len(text)-k+1):
        subtext = text[i:i+k]
        for i in Neighbors(subtext,d):
            if (i not in frequency_dict) and (reverse_complement(i) not in frequency_dict):
                frequency_dict[i]=1
                frequency_dict[reverse_complement(i)]=1
                        
            elif (i  in frequency_dict) and (reverse_complement(i) not in frequency_dict):
                frequency_dict[i]+=1
                frequency_dict[reverse_complement(i)]=1
                
                
            elif (i not in frequency_dict) and (reverse_complement(i)  in frequency_dict):
                frequency_dict[i]=1
                frequency_dict[reverse_complement(i)]+=1                
                
            else:
                frequency_dict[i]+=1
                frequency_dict[reverse_complement(i)]+=1                
    return frequency_dict
        """

def frequent_words_with_mismatches(text,k,d):
    frequency_dict = {}
    for i in range(len(text)-k+1):
        subtext = text[i:i+k]
        for i in Neighbors(subtext,d):
            if i not in frequency_dict:
                frequency_dict[i]=1
            else:
                frequency_dict[i] +=1
            if reverse_complement(i) not in frequency_dict:
                frequency_dict[reverse_complement(i)]=1
            else:
                frequency_dict[reverse_complement(i)] +=1              
    return frequency_dict
        
start = time.time()
frequency_dict = frequent_words_with_mismatches(text,k,d)
maximum = max(frequency_dict.values())
frequent_patterns = {k:v for k,v in frequency_dict.items() if v==maximum}

#print(frequency_dict)
print(" ".join(frequent_patterns))
print(frequent_patterns)
end = time.time()
print(end - start)