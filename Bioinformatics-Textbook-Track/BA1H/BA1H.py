

with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1H\rosalind_ba1h.txt') as f:
    pattern=f.readline().strip()
    text=f.readline().strip()
    d= int(f.readline().strip())
#pattern="ATTCTGGA"
#text="CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
#d=3
def HammingDistance(p,q):
    distance=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            distance+=1
    return distance
def ApproximatePatternCount(text,pattern,d):
    for i in range(len(text)-len(pattern)+1):
        subtext = text[i:i+len(pattern)]
        if HammingDistance(pattern,subtext)<=d:
            yield i
        
print(" ".join([str(i) for i in ApproximatePatternCount(text,pattern,d)]))