with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1C\rosalind_ba1c.txt') as f:
    
    strand1= f.read()
 
strand2 = strand1.replace("A","X").replace("C","Y").replace("G","C").replace("T","A").replace("X","T").replace("Y","G")
print(strand2[::-1])

print(strand1[::-1].translate(str.maketrans('ACGT', 'TGCA')))