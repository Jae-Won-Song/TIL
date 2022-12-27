import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    max(numbers) - min(numbers)

    max_value = max(numbers)
    min_value = min(numbers)


    ans = max_value - min_value



    print (f'#{tc} {ans}')