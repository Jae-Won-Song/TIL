import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 0,0,0,0,0,0,0,0,0,0의 2차원 리스트 만들기
    result = [[0] * 10 for ___ in range(10)]
# row의 범위(input 값 넣을 위치 정하기)
    for row in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
# 정해진 구역에 색칠하기
        for col in range(r1, r2 + 1):
            for new_col in range(c1, c2 + 1):
                # 색이 안칠해졌으면 pass
                if result[col][new_col] == color:
                    pass
                # 색이 칠해졌으면 color에 더하기
                result[col][new_col] += color

    count = 0
    for row in range(len(result)):
        for col in range(len(result[row])):
            if result[row][col] >= 3:
                count += 1

    print(f'#{tc} {count}')


#    for row in range(10):
#        map(int, input().split())
#    for col in range(10):
#        map(int, input().split())

    #if matrix in
        #for col in range(10):
       #[1, 1, 3, 3, 1] : [시작r, 시작c, 끝r, 끝c 색깔]