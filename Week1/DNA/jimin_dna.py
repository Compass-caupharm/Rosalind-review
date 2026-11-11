with open("rosalind_dna.txt", "r") as f:
    dna = f.read().strip()

nA= dna.count('A')
nC= dna.count('C')
nG= dna.count('G')
nT= dna.count('T')


print(f"{nA} {nC} {nG} {nT}")
