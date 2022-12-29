from itertools import combinations
import sys
sys.stdin = open('input.txt')
T = int(input())
tc = (1, T+1)
count = 0
N, K = list(map(int, input().split()))
A_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A_subs = list(combinations(A_set, N))  # **
for i in A_subs:
    if sum(i) == 6:
        count += 1


print(f'{tc}, {count}')
