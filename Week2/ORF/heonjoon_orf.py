"""Rosalind ORF: Open Reading Frames
사용법: python3 orf.py rosalind_orf.txt
"""
import sys

BASES = "TCAG"
AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON = {a + b + c: AMINO[16 * i + 4 * j + k]
         for i, a in enumerate(BASES)
         for j, b in enumerate(BASES)
         for k, c in enumerate(BASES)}


def read_fasta(text):
    return "".join(l.strip() for l in text.splitlines() if not l.startswith(">"))


def revcomp(s):
    return s[::-1].translate(str.maketrans("ACGT", "TGCA"))


def orfs(dna):
    found = set()
    for seq in (dna, revcomp(dna)):
        for i in range(len(seq) - 2):
            if seq[i:i + 3] != "ATG":
                continue
            prot = []
            for j in range(i, len(seq) - 2, 3):
                aa = CODON[seq[j:j + 3]]
                if aa == "*":          # 정지 코돈을 만나야만 유효한 ORF
                    found.add("".join(prot))
                    break
                prot.append(aa)
    return found


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = open(sys.argv[1]).read()
    else:  # 샘플 데이터
        text = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""
    print("\n".join(sorted(orfs(read_fasta(text)))))
