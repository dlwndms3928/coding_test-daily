"""
SWEA_1964 달팽이 숫자

[문제]
달팽이는 1부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

[예제]
N이 3일 경우,
1 2 3
8 9 4
7 6 5

N이 4일 경우
1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7

[제약사항]
달팽이 크기 N은 1이상 10 이하의 정수이다

[입력]
가장 첫 줄에는 테스트 케이스 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
2
3
4

[출력]
각 줄은 '#t'로 시작하고,
다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

"""
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    x,y = 0,0
    num = 1
    matrix[0][0]=num
    num += 1
    while num <= N*N:
        # 오른쪽
        while (y+1<N and matrix[x][y+1]==0):
            y += 1
            matrix[x][y] = num
            num += 1
        # 아래
        while (x+1<N and matrix[x+1][y]==0):
            x += 1
            matrix[x][y] = num
            num += 1
        # 왼쪽
        while (y-1>=0 and matrix[x][y-1]==0):
            y -= 1
            matrix[x][y] = num
            num += 1
        while (x-1>=0 and matrix[x-1][y]==0):
            x -= 1
            matrix[x][y] = num
            num += 1
    print(f"#{test_case}")
    for i in range(N):
        print(f"{' '.join(map(str,matrix[i]))}")
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    x, y = 0, 0  # 현재 위치
    direction = 0  # 현재 이동 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for num in range(1, N * N + 1):
        matrix[x][y] = num

        # 다음번의 이동 x좌표와 y좌표 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 다음 칸으로 갈 수 없다면 방향 변경
        if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny] != 0:

            # 방향을 변경
            direction = (direction + 1) % 4

            # 방향을 변경해서 다시 이동할 x좌표량 y좌표 계산
            nx = x + dx[direction]
            ny = y + dy[direction]

        # 계산한 다음 위치를 현재로 이동
        x = nx
        y = ny
    print(f"#{test_case}")
    for i in range(N):
        # 배열의 각 행을 하나씩 확인
        print(" ".join(map(str, matrix[i])))
