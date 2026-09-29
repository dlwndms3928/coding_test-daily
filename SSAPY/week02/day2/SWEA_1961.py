"""
N*N 행렬이 주어질 때.
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

[제약사항]
N은 3이상 7이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어짐
다음 N줄에는 N*N 행렬이 주어짐.
10
3
1 2 3
4 5 6
7 8 9
.
.
.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
#1
741 987 369
852 654 258
963 321 147
#2
.
.
.
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    rotate = lambda b: [list(row) for row in zip(*b[::-1])]
    r90 = rotate(matrix)
    r180 = rotate(r90)
    r270 = rotate(r180)

    print(f"#{test_case}")
    for i in range(N):
        print(
            f"{''.join(map(str,r90[i]))} {''.join(map(str,r180[i]))} {''.join(map(str,r270[i]))}"
        )
