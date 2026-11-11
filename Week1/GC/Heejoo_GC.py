# ROSALIND GC - Computing GC Content
# GC-content: 서열 전체 길이 중 G 또는 C가 차지하는 비율(%)

# STEP 1. FASTA 파일 읽어서 서열 모으기
seqs = {}                                  # {이름: 서열} 형태로 저장할 딕셔너리

with open("rosalind_gc.txt") as f:         # 입력 파일 열기
    for line in f:                         # 파일을 한 줄씩 읽기
        line = line.strip()                # 줄 끝의 줄바꿈 문자 제거
        if line.startswith(">"):           # '>'로 시작하면 이름 줄
            name = line[1:]                # '>'를 떼고 이름만 저장 (예: Rosalind_6404)
            seqs[name] = ""                # 그 이름으로 빈 서열 칸 만들기
        else:                              # 이름 줄이 아니면 서열 줄
            seqs[name] = seqs[name] + line # 여러 줄로 나뉜 서열을 하나로 이어 붙이기

# STEP 2. 1등을 기록할 변수 만들기
top = ""                                   # GC-content가 가장 높은 서열의 이름
top_gc = 0                                 # 그 서열의 GC-content 값

# STEP 3. 서열마다 GC-content 계산해서 가장 높은 것 찾기
for name in seqs:                          # 서열을 하나씩 꺼내기
    dna = seqs[name]                       # 현재 서열
    gc = (dna.count("G") + dna.count("C")) / len(dna) * 100   # (G 개수 + C 개수) / 전체 길이 × 100
    if gc > top_gc:                        # 지금까지의 1등보다 높으면
        top = name                         # 1등 이름 바꾸기
        top_gc = gc                        # 1등 값 바꾸기

# STEP 4. 결과 출력
print(top)                                 # 예: Rosalind_0808
print(top_gc)                              # 예: 60.919540
