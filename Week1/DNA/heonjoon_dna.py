dna = open("rosalind_dna.txt").read().strip()

counts = {"A": 0, "C": 0, "G": 0, "T": 0}
for base in dna:
    counts[base] += 1

print(" ".join(str(counts[b]) for b in "ACGT"))
