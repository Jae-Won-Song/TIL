import sys

sys.stdin = open('input.txt')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]

# row 합
row_total_list = []
for r in range(100):
# 각 행의 합을 구하는 r_total 변수 초기화
    r_total = 0
# 각 행의 합을 구하고, 그 값을 row_total_list 에 추가
    for j in range(100):
        r_total += arr[r][j]
        row_total_list.append(r_total)
       # print(r_total)

# col 합

col_total_list = []

for c in range(100):
    c_total = 0

    for cc in range(100):
        c_total += arr[c][cc]
        col_total_list.append(c_total)
        #print(c_total)

find_max_value = [max(row_total_list), max(col_total_list)]
result = max(find_max_value)

print(f'#{T}, {result}')
# cross 합

#cross_total_list = []

#for cross in range(100):
