symbol=['A','C','G','T']
number=[0,1,2,3]

def patterntonumber(pattern):
    base4= [symbol.index(x) for x in pattern]
    base10=0
    for i in range(len(pattern)):
        base10 += base4[i]*4**(len(pattern)-i-1)
    return base10 
def numbertopattern(index,k):
    pattern = ''
    for i in range(k):
        pattern =symbol[index%4]+pattern
        index = index // 4
    return pattern

def computing_frequencies_with_mismatches(text,k):
    ''' Computes the kmers of text and the frequency of their occurence '''
    frequency_array = [0]*(4**k)
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        index = patterntonumber(pattern)
        frequency_array[index]+=1
    return frequency_array
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
        frequent_patterns = [numbertopattern(index,k) for index in index_list if count_list[index_list.index(index)]==max(count_list)]
    else:
        frequent_patterns = [numbertopattern(index,k) for index in index_list if count_list[index_list.index(index)]>=t]
    return (frequent_patterns)
