import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input(), split()))

    print(numbers)

    print(f'#{tc}')