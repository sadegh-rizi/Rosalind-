lex= {"A":0,"C":1,"G":2,"T":3}
pattern="ATGCAAA"

symbol=['A','C','G','T']
number=[0,1,2,3]

def patterntonumber(pattern):
    base4= [symbol.index(x) for x in pattern]
    base10=0
    for i in range(len(pattern)):
        base10 += base4[i]*4**(len(pattern)-i-1)
    return base10 

#recursive version 
def recursive_patterntonumber(pattern):
    if not pattern:
        return 0
    last_symbol = pattern[-1] 
    prefix = pattern[:-1]
    return symbol.index(last_symbol)+ 4*recursive_patterntonumber(prefix) 
recursive_patterntonumber("CCCATTC")

def numbertopattern(index,k):
    base4 =[]
    quotient = index
    while quotient != 0 :
        quotient = index//4 
        remainder = index%4
        index=quotient
        #print(quotient)
        #print(remainder)
        base4.append(remainder)
    base4.extend((k-len(base4))*[0])
    base4= base4[::-1] 
    #print(base4)  
    #print([symbol[x] for x in base4])
    pattern= "".join([symbol[x] for x in base4])
    return pattern

#OR > This one is better ! 

def numbertopattern2(index,k):
    pattern = ''
    for i in range(k):
        pattern += symbol[index%4]
        index = index // 4

    return pattern
numbertopattern2(5437,7)




#numbertopattern(7450,9)

#Recursive approach 
def recursive_numbertopattern(index,k):
    if k==1:
        return symbol[index]
    
    prefix_index = index//4 
    remainder = index%4 
    lsymbol = symbol[remainder]
    prefix_pattern= recursive_numbertopattern(prefix_index,k-1)
    return prefix_pattern+lsymbol
#recursive_numbertopattern(5437,8)
  
##numbertopattern(0,2)


def computing_frequencies(text,k):
    frequency_array = [0]*(4**k)
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        index = patterntonumber(pattern)
        frequency_array[index]+=1
    return frequency_array
#computing_frequencies("AAGCAAAGGTGGG",2)

def faster_frequent_words(text,k):
    frequents_patterns=set()
    frequency_array=computing_frequencies(text,k)
    #print(frequency_array)
    patterns = [numbertopattern(i,k) for i in range(len(frequency_array)) if frequency_array[i]==max(frequency_array) ]
    return patterns
seq='CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC'

def finding_frequent_words_by_sorting(text , k,t='maximum'):
    index_list = []
    count_list = []
    for i in range(len(text)-k+1):
    
        pattern = text[i:i+k]
        index = patterntonumber(pattern)
        #print(index)
        #print(index_list)
        #print(count_list)
        if index not in index_list:
            
            index_list.append(index)
            count_list.append(1) 
        else:
            count_list[index_list.index(index)]+=1
    #print(index_list)
    #print(count_list)
    if t=='maximum':
        frequent_patterns = [numbertopattern2(index,k) for index in index_list if count_list[index_list.index(index)]==max(count_list)]
    else:
        frequent_patterns = [numbertopattern2(index,k) for index in index_list if count_list[index_list.index(index)]==t]
    return (frequent_patterns)
#finding_frequent_words_by_sorting("AAGCAAAGGTGGG",2)



#k=5
#print(" ".join(faster_frequent_words(seq,k)))

#numbertopattern(5437,4)

#recursive_patterntonumber("GTCCATATGCGTCGAACGGACATTTCTCT")
#patterntonumber("GTCCATATGCGTCGAACGGACATTTCTCT")
