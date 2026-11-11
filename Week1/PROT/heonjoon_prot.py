# prot.py
import sys

# 1. 코돈표 만들기 (표준 유전 암호, UCAG 순서)
BASES = "UCAG"
AAS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {}
i = 0
for a in BASES:
    for b in BASES:
        for c in BASES:
            CODON_TABLE[a + b + c] = AAS[i]
            i += 1

# 2. RNA -> 단백질 번역
def translate(rna):
    protein = []
    for j in range(0, len(rna) - 2, 3):
        aa = CODON_TABLE[rna[j:j+3]]
        if aa == "*":          # 종결 코돈(UAA, UAG, UGA)에서 멈춤
            break
        protein.append(aa)
    return "".join(protein)

# 3. 실행부
if __name__ == "__main__":
    # 파일 이름을 인자로 받고, 없으면 기본값 사용
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_prot.txt"

    with open(filename) as f:
        rna = "".join(f.read().split()).upper()   # 줄바꿈/공백 제거

    result = translate(rna)
    print(result)

    with open("answer.txt", "w") as f:
        f.write(result)
    print("-> answer.txt 에 저장했습니다.")
