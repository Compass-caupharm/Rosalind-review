with open("rosalind_dna.txt", "r") as f:
    s = f.read().strip()

nA= s.count('A')
nC= s.count('C')
nG= s.count('G')
nT= s.count('T')


print(f"{nA} {nC} {nG} {nT}")
