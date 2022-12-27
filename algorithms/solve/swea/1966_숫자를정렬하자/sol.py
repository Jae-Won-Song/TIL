import sys

sys.stdin = open('input.txt')

# n길이의 숫자열을 오름차순으로 정렬해 출력.

# T = int(input())

# for num in range(1, T + 1):
#    nums = list(map(int, input().split()))
#    str(nums.sort())
#    sor_num = nums.sort()


# print(f'#{num}', nums)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    target_list = list(map(int, (input().split())))
    target_list.sort()
    target_list = list(map(str, target_list))
    target_str = ' '.join (target_list)

    print(f'#{tc} {target_str}')
