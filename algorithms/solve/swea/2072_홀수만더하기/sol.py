import sys
sys.stdin = open('input.txt')


T = int(input())


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    total = 0

    for num in numbers:
        if num % 2:
            total += num

    print(f'#{tc} {total}')