import sys

sys.stdin = open('input.txt')

N = int(input())

switches = list(map(int, input().split()))
student_cnt = int(input())

for _ in range(student_cnt):
    gender, num = map(int, input().split())

    if gender == 1:
        i = 1
        idx = num - 1
        while idx < N:  # switches[idx] ^= 1 (bit 연산자 XOR)
            # = switches = 0 if switches[idx] else 1
            if switches[idx] == 0:
                switches[idx] = 1

            else:
                switches[idx] = 0
            i += 1
            idx = (num * 1) - 1


    # 여자 -> num 은 바꾸고, 좌우대칭이면 바꾼다
    else:
        switches[idx] ^= 1
        side = 1

        while 0 <= idx - side and (idx + side) < N:
            left = switches[idx - side]
            right = switches[idx + side]

            if left != right:
                break
            else:
                switches[idx - side] ^= 1
                switches[idx + side] ^= 1
                side += 1
        for part_no in range(N // 20 + 1):
            start = 20 * part_no
            end = 20 * (part_no + 1)
            print(' '.join(map(str, switches[start:end])))
