from functions import finding_frequent_words_by_sorting,computing_frequencies,patterntonumber,numbertopattern


with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1E\rosalind_ba1e.txt') as f:
    genome=f.readline().strip()
    k,L,t =[int(x) for x in f.readline().strip().split()]

#genome='CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
#k,L,t =[int(x) for x in '5 75 4'.strip().split()]
def clump_finding0(genome,k,t,L):
    clump_seqs=[]
    for i in range(len(genome)-L):
        clump_seqs += finding_frequent_words_by_sorting(genome[i:i+L],k,t)
    return(set(clump_seqs))

def clump_finding(genome,k,t,L):
    frequent_patterns = set()
    clumps = 4**k * [0]
    #print(clumps)
    for i in range(len(genome)-L+1):
        text = genome[i:i+L]
        frequency_array= computing_frequencies(text,k)
        #print(frequency_array)
        clumps = [clumps[j]+1 if frequency_array[j]>=t else clumps[j] for j in range(len(clumps)) ]    
    #print(clumps)
    for i in range(len(clumps)):

        if clumps[i]!=0:
            frequent_patterns.add(numbertopattern(i,k))
            #print(numbertopattern(i,k))
    return frequent_patterns


def clump_finding2(genome,k,t,L):
    frequent_patterns = set()
    clumps = 4**k * [0]
    #print(clumps)
    frequency_array= computing_frequencies(genome[0:L],k)
    clumps = [clumps[j]+1 if frequency_array[j]>=t else clumps[j] for j in range(len(clumps)) ]    
    
    for i in range(len(genome)-L+1):
        substract_first = genome[i-1:i-1+k]
        add_last = genome[i+L-k:i+L]
        frequency_array[patterntonumber(substract_first)] -= 1
        frequency_array[patterntonumber(add_last)] += 1
        
        
        clumps = [clumps[j]+1 if frequency_array[j]>=t else clumps[j] for j in range(len(clumps)) ]    
    #print(clumps)
    for i in range(len(clumps)):
        if clumps[i]!=0:
            frequent_patterns.add(numbertopattern(i,k))
            #print(numbertopattern(i,k))
    return frequent_patterns

"""def ComputingFrequencies(text, k):
    frequency_dict = { }

    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        if pattern in frequency_dict:
            frequency_dict[pattern] += 1
        else:
            frequency_dict[pattern] = 1

    return frequency_dict"""
def clump_finding3(genome,k,t,L):
    frequent_patterns = set()
    
    #print(clumps)
    frequency_array= computing_frequencies(genome[0:L],k)
    for i in range(len(frequency_array)):
        if frequency_array[i]>=t:
            frequent_patterns.add(numbertopattern(i,k))

    for i in range(1,len(genome)-L+1):
        substract_first = genome[i-1:i-1+k]
        add_last = genome[i+L-k:i+L]
        frequency_array[patterntonumber(substract_first)] -= 1
        frequency_array[patterntonumber(add_last)] += 1
    if frequency_array[patterntonumber(add_last)]>=t:
        frequent_patterns.add(add_last)    
        
    #print(clumps)

            #print(numbertopattern(i,k))
    return frequent_patterns  

def clump_finding4(strings,k,L,t):
    substrings = []

    for i in range(len(strings)-k-1):
        substrings.append(strings[i:i+k])

    for i in list(set(substrings)):
        temp = 0
        j = 0

        while j<= (len(strings)-L-1):
            f = strings[j:j+L].count(i)

            if f>=t:
                print(i,end=" ")
                break

            j+=(t-f-1)*k+1  
    
#print(clump_finding0(genome,k,t,L))
#print(clump_finding(genome,k,t,L))
#print(clump_finding2(genome,k,t,L))
#print(clump_finding3(genome,k,t,L))
(clump_finding4(genome,k,L,t))
