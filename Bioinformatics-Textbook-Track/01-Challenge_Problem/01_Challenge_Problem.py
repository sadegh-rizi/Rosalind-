#Importing and inputs
from Bio import SeqIO
import matplotlib.pyplot as plt
import time
input_file = r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\01-Challenge_Problem\ncbi_dataset\ncbi_dataset\data\GCA_000006945.2\GCA_000006945.2_ASM694v2_genomic.fna'
fasta_sequences = list(SeqIO.parse(open(input_file),'fasta'))
#print(fasta_sequences[0])
for seq in fasta_sequences:
    print(seq.description)
genome = fasta_sequences[0].seq
values = {'A':0,'T':0,'C':-1,'G':1}
#Functions
#Function 1 : Skew
def Skew(genome):
    skew = []
    '''Skew : #G-#C '''
    current_skew = 0
    for i in range(len(genome)):
        current_skew += values[genome[i]]
        skew.append(current_skew)
            
    return skew

skews = Skew(genome)
minima=[]
minimum = min(skews)
minima = [i+1 for i in range(len(skews)) if skews[i]==minimum]
#print(minima)
avg_minimum_position = sum(minima)//len(minima)
print(avg_minimum_position)
#print(' '.join(minima))
plt.plot(range(len(skews)),skews)
plt.show()

#Function set2: Most frequent with mismatches
def reverse_complement(strand):
    return strand.replace("A","X").replace("C","Y").replace("G","C").replace("T","A").replace("X","T").replace("Y","G")[::-1]

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
L = 1000 #window size
k=9
d=1

text1= genome[avg_minimum_position-L:avg_minimum_position]
text2= genome[avg_minimum_position-(L//2):avg_minimum_position+(L//2)]
text3= genome[avg_minimum_position:avg_minimum_position+L]

frequency_dict = frequent_words_with_mismatches(text1,k,d)
maximum = max(frequency_dict.values())
frequent_patterns = {k:v for k,v in frequency_dict.items() if v==maximum}
print(frequent_patterns)

frequency_dict = frequent_words_with_mismatches(text2,k,d)
maximum = max(frequency_dict.values())
frequent_patterns = {k:v for k,v in frequency_dict.items() if v==maximum}
print(frequent_patterns)

frequency_dict = frequent_words_with_mismatches(text3,k,d)
maximum = max(frequency_dict.values())
frequent_patterns = {k:v for k,v in frequency_dict.items() if v==maximum}
print(frequent_patterns)

#Correct answer TTATCCACA was among the candidates :) Hooray