import matplotlib.pyplot as plt
with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1F\rosalind_ba1f.txt') as f:
    genome=f.readline().strip()
#genome="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG" 
values = {'A':0,'T':0,'C':-1,'G':1}
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

'''
NOTE:
If you hadn't used the minimum variable,python had to 
calculate it for each iteration and it would've taken too long
to execute the program
'''
minimum = min(skews)
minima = [str(i+1) for i in range(len(skews)) if skews[i]==minimum]
#print(minima)
print(' '.join(minima))
plt.plot(range(len(skews)),skews)
plt.show()
#rint(genome)

def minimum_skew(genome):
    
    '''Skew : #G-#C '''
    minima_index=[]
    minimum = 0
    current_skew = 0
    for i in range(len(genome)):
        if genome[i]=="G":
            current_skew+=1
        if genome[i]=="C":
            current_skew-=1
        else:
            pass
        if current_skew < minimum:
            minimum= current_skew
            minima_index=[]
            minima_index.append(i)
        elif current_skew==minimum:
            minima_index.append(i)
        else:
            pass
                
    return minima_index

#for i in minimum_skew(genome):
#    print(i+1,end=' ')


