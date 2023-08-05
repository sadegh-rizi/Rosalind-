with open(r'D:\Python Codes\Rosalind-\Bioinformatics-Textbook-Track\BA1D\rosalind_ba1d.txt') as f:
    pattern=f.readline().strip()
    genome =f.readline().strip()
    

starting_positions =[str(i) for i in range(len(genome)-len(pattern)+1) if genome[i:i+len(pattern)]==pattern]
print(" ".join(starting_positions))

'''
import re
pattern = 'ATAT'
string = 'GATATATGCATATACTT'
matches = re.finditer('(?={0})'.format(pattern), string)
positions = [str(match.start()) for match in matches]
result = ' '.join(positions)
print(result)

'''