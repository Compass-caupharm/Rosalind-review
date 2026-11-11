seqs = {}
with open("rosalind_gc.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]
            seqs[name] = ""
        else:
            seqs[name] += line

def gc_content(s):
    return (s.count("G") + s.count("C")) / len(s) * 100

best = max(seqs, key=lambda k: gc_content(seqs[k]))
print(best)
print(f"{gc_content(seqs[best]):.6f}")


##  biopython 
!pip install biopython
from fasta_utils import read_fasta, highest_gc

seqs = read_fasta("rosalind_gc.txt")
best_id, best_gc = highest_gc(seqs)
print(best_id)
print(f"{best_gc:.6f}")
