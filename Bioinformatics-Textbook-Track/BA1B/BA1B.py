#Frequent Words Problem:
'''
    Input: A string Text and an integer k.
    Output: All most frequent k-mers in Text
'''
    #Approach 1 : find all k-mers and count their frequency and sort them
def PatternCount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        #print(f"i:{i}")
        #print(f"subtext:{text[i:i+len(pattern)]}")
        if text[i:i+len(pattern)] == pattern:
            c+=1
    return c 

def get_k_mers(seq,k):
    k_mers={}
    for i in range(len(seq)-k+1):
        k_mer = seq[i:i+k]
        frequency = PatternCount(seq,k_mer)
        k_mers[k_mer] = frequency
    return k_mers


#Approach2: just as before but only store the ones with highest freq at the list , if another one with more frequency shows up delete last 
#ones and instert the new one. if the freq equals the last one just add the new one and else pass 
def get_k_mers2(seq,k):
    most_frequent_k_mers=[seq[:k]]
    for i in range(1,len(seq)-k+1):
        k_mer = seq[i:i+k]
        new_kmer=PatternCount(seq,k_mer) 
        last_kmer =PatternCount(seq,most_frequent_k_mers[-1])
        if new_kmer>last_kmer :
            
            most_frequent_k_mers=[k_mer]
        elif new_kmer== last_kmer:
            most_frequent_k_mers.append(k_mer)
        else:
            pass
            
    return list(set(most_frequent_k_mers))

        
seq='CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC'

k=5
#sorted_k_mers = sorted(get_k_mers(seq,k).items(),key = lambda x:x[1],reverse=True)
        
print(" ".join(get_k_mers2(seq,k))) 

kmers=[]
frqs = []
def freq_array(seq,k):
    global kmers
    global frqs
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        if kmer not in kmers:
        
            kmers +=[kmer]
            frqs += [1] 
        if kmer in kmers:
            frqs[kmers.index(kmer)] += 1 
freq_array(seq,k)
print(kmers)
print(frqs)





if __name__ == "__main__":
    with open(r"D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1B\rosalind_ba1b.txt") as f:
        seq = f.readline().strip()
        k = int(f.readline().strip())
    print(" ".join(get_k_mers2(seq,k)))     



