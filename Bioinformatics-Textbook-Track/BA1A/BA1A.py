
with open(r"D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\rosalind_ba1a.txt") as f:
    text = f.readline().strip()
    pattern = f.readline().strip()
    
def PatternCount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        #print(f"i:{i}")
        #print(f"subtext:{text[i:i+len(pattern)]}")
        if text[i:i+len(pattern)] == pattern:
            c+=1
    return c 
print(PatternCount(text ,pattern))
"""
for i in range(1,9):
    i = str(i)
    filename=fr"D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1A-PatternCount\1A\inputs\input_{i}.txt"
    with open(filename) as f:
        text = f.readline()
        pattern = f.readline()
        print(f"input_{i}.txt")
        print(PatternCount(text ,pattern))
        """