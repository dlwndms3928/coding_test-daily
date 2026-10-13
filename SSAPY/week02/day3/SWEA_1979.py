"""
1979. 어디에 단어가 들어갈 수 있을까

[문제설명]
N * N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는
프로그램을 작성하라.

N =5, k=3이고, 퍼즐 모양이 아래 그림과 같이 주어졌을 때
길이가 3인 단어가 들어갈 수 있는 자리는 2곳(가로1번, 가로4번)이 된다.

[제약사항]
1. N은 5이상 15이하의 정수이다.
2. K는 2이상 N이하의 정수이다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 두 번재 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은1, 검은색 부분은 0으로 주어진다.

[출력]
테스트 케이스 t에 대한 결과는 '#t'를 찍고, 한칸 띄고, 정답을 출력한다.
"""


def yunsk(line, K):
    length = 0
    count = 0
    for x in line:
        if x == 1:
            length += 1
        else:  # 0을 만나면 덩어리 끝
            if length == K:
                count += 1
            length = 0
    if length == K:
        count += 1
    return count


def garo(matrix, K):
    count = 0
    for r in matrix:
        count += yunsk(r, K)
    return count


def sero(matrix, K):
    count = 0
    for c in zip(*matrix):
        count += yunsk(c, K)
    return count


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{test_case} {garo(matrix,K)+sero(matrix,K)}")
