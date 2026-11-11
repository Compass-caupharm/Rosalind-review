# ROSALIND REVC - Complementing a Strand of DNA

with open("rosalind_revc.txt") as f:
    dna = f.read().strip()

pair = {"A": "T", "T": "A", "C": "G", "G": "C"}

result = ""
for base in dna[::-1]:
    result = result + pair[base]

print(result)
