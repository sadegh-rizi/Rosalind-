import time
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1I\rosalind_ba1i.txt') as f:
    text=f.readline().strip()
    k,d=[int(i) for i in f.readline().strip().split()]
    
from functions import patterntonumber,numbertopattern
#text="ACGTTGCATGTCGCATGATGCATGAGAGCT"
#k=4
#d=1
def HammingDistance(p,q):
    distance=0
    for i in range(len(p)):
        #print(p,q,sep="*")
        if p[i]!=q[i]:
            distance+=1
    return distance
def ApproximatePatternCount(text,pattern,d):
    for i in range(len(text)-len(pattern)+1):
        subtext = text[i:i+len(pattern)]
        if HammingDistance(pattern,subtext)<=d:
            yield i


def computing_frequencies_with_mismatches(text,k,d):
    ''' Computes the kmers of text and the frequency of their occurence '''
    frequency_array = [0]*(4**k)
    for i in range(len(frequency_array)):
        pattern = numbertopattern(i,k)
        for j in range(len(text)-k+1):
            subtext = text[j:j+k]
            
            if HammingDistance(pattern,subtext)<=d:
                frequency_array[i]+=1 
    return frequency_array
def frequent_words_with_mismatches(text,k,d):
    frequency_array = computing_frequencies_with_mismatches(text,k,d)
    maximum = max(frequency_array)
    frequent_patterns = [numbertopattern(i,k) for i in range(len(frequency_array)) if frequency_array[i]==maximum]
    return frequent_patterns

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
def frequent_words_with_mismatches2(text,k,d):
    frequency_dict = {}
    for i in range(len(text)-k+1):
        subtext = text[i:i+k]
        for i in Neighbors(subtext,d):
            if i not in frequency_dict:
                frequency_dict[i]=1
            else:
                frequency_dict[i]+=1
    return frequency_dict
        



start = time.time()

print(" ".join(frequent_words_with_mismatches(text,k,d)))


end = time.time()
print(end - start)


start = time.time()

frequency_dict = frequent_words_with_mismatches2(text,k,d)
maximum = max(frequency_dict.values())
frequent_patterns = [k for k,v in frequency_dict.items() if v==maximum]
print(" ".join(frequent_patterns))

end = time.time()
print(end - start)