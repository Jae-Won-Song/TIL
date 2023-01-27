import sys

sys.stdin = open('input.txt')

# row, col 의 최댓값 과 대각선 합의 최댓값 구하기

for tc in range(10):  # 테스트 케이스 값 할당
    N = int(input())
    arr = []
    for i in range(100):
        numbers = list(map(int, input().split()))  # 리스트 만들기
        arr.append(numbers)

    colum_sum_max = 0  # col_max 변수 초기화
    row_sum_max = 0  # row_max 변수 초기화
    diagonal_sum = 0  # 우하향 변수 초기화
    opposite_diagonal = 0  # 우상향 변수 초기화

    for row in range(100):
        diagonal_sum += arr[row][row]  # 대각선 더하기
        opposite_diagonal += arr[row][row - 1]  # 반대쪽 대각선 더하기
        colum_sum = 0  # col 값마다 더한  값
        row_sum = 0  # row 값마다 더한 값

        for column in range(100):  # col 합 구하기
            colum_sum += arr[row][column]
            row_sum += arr[column][row]

        if colum_sum_max < colum_sum:  # 합의 최댓값 구하기
            colum_sum_max = colum_sum
        if row_sum_max < row_sum:
            row_sum_max = row_sum

    print(f'#{tc + 1} {max(colum_sum_max, row_sum_max, diagonal_sum, opposite_diagonal)}')
