import sys
sys.stdin = open('input.txt')


T = int(input())

def solve(numbers):
    total = 0
    for num in numbers:
        if num % 2:
            total += num

    return total

    print(f'#{tc} {total}')