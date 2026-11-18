# ROSALIND ORF - Open Reading Frames

# FASTA 파일 읽기 (서열 1개, 여러 줄 이어 붙이기)
dna = ""
with open("rosalind_orf.txt") as f:
    for line in f:
        line = line.strip()
        if not line.startswith(">"):
            dna = dna + line

# 코돈표 만들기
# 코돈을 TTT, TTC, TTA, TTG, TCT, ... GGG 순서로 만들면
# aminos의 글자가 그 순서대로 각 코돈의 아미노산 (* = 종결 코돈)
bases = "TCAG"
aminos = ("FFLLSSSSYY**CC*W"   # T로 시작하는 코돈 16개
          "LLLLPPPPHHQQRRRR"   # C로 시작하는 코돈 16개
          "IIIMTTTTNNKKSSRR"   # A로 시작하는 코돈 16개
          "VVVVAAAADDEEGGGG")  # G로 시작하는 코돈 16개

codon = {}
i = 0
for a in bases:                # 첫째 글자
    for b in bases:            # 둘째 글자
        for c in bases:        # 셋째 글자
            codon[a + b + c] = aminos[i]
            i = i + 1


# 풀이 1. 직접 구현

# 역상보 서열 만들기 (REVC)
pair = {"A": "T", "T": "A", "C": "G", "G": "C"}
revc = ""
for base in dna[::-1]:
    revc = revc + pair[base]

proteins = set()   # 같은 단백질은 한 번만 저장

for s in [dna, revc]:
    for i in range(len(s) - 2):
        if s[i:i+3] == "ATG":                # 시작 코돈 찾기
            protein = ""
            for j in range(i, len(s) - 2, 3):  # 3글자씩 번역
                aa = codon[s[j:j+3]]
                if aa == "*":                # 종결 코돈이면 저장하고 멈춤
                    proteins.add(protein)
                    break
                protein = protein + aa

for p in proteins:
    print(p)


# 풀이 2. Biopython 사용
from Bio.Seq import Seq

proteins2 = set()

for s in [Seq(dna), Seq(dna).reverse_complement()]:
    s = str(s)
    for i in range(len(s) - 2):
        if s[i:i+3] == "ATG":
            part = s[i:]
            part = part[:len(part) // 3 * 3]          # 3의 배수 길이로 자르기
            aa = str(Seq(part).translate())          # 종결 코돈은 '*'로 번역됨
            if "*" in aa:
                proteins2.add(aa.split("*")[0])      # 첫 '*' 앞까지가 단백질

for p in proteins2:
    print(p)
