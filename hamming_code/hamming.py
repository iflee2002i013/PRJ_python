# 参数
DATA = 128
ECC = 9
R = ECC
N = DATA + ECC

# 字段规划举例 (R = 9): [half(1) | quarter(2) | offset(6)] => 1+2+6 = 9 bits
# half: 1 bit (top/bottom)
# quarter: 2 bits (Q1..Q4)
# offset: 6 bits (64 positions per quarter -> 足够覆盖各自的位数)

def make_column(half, quarter, offset):
    # half: 0/1, quarter: 0..3, offset: 0..63
    return (half<<8) | (quarter<<6) | offset  # 9-bit integer

# 生成 data 列向量（把 data 分配到 Q1..Q4，按象限内顺序分配 offset）
cols = []
for q in range(4):            # q = 0..3 -> Q1..Q4
    half = 1 if q in (0,1) else 0   # 举例：Q1,Q2 -> top(1); Q3,Q4 -> bottom(0)
    for j in range(DATA//4):   # 每象限 32 位 (128/4)
        offset = j+1          # 避免 offset == 0 导致全零列
        cols.append(make_column(half, q, offset))

# 生成 ECC 列（选取未用的非零向量）
used = set(cols)
ecc_cols = []
for v in range(1, 1<<R):
    if v not in used and len(ecc_cols) < ECC:
        ecc_cols.append(v)
cols.extend(ecc_cols)
print(cols)
# cols 长度应为 N；将它们转换成 H 的列（每列是 R 位向量）
# H[j][i] = bit j of cols[i]
