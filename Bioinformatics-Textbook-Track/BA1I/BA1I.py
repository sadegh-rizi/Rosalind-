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
print(" ".join(frequent_words_with_mismatches(text,k,d)))