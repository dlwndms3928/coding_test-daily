"""
시간 : 10개 테스트케이스를 합쳐서 C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

N개의 숫자로 구성된 숫자열 A_i(i=1~N)와
M개의 숫자로 구성된 숫자열 B_j(j=1~M)가 있다.
A_i나 B_j를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하여라.

[제약사항]
N과 M은 3이상 20 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N과 M이 주어지고,
두 번째 줄에는 A_j,
세 번째 줄에는 B_j가 주어진다.
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
...

[출력]
출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음 정답을 출력한다.
#1 30
#2 63
...

"""

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    if N > M:
        long_list, short_list = A_list, B_list
    else:
        long_list, short_list = B_list, A_list
    window_iter = len(long_list) - len(short_list) + 1
    max_value = float("-inf")
    for offset in range(window_iter):
        sum_value = sum(
            long_list[j + offset] * short_list[j] for j in range(len(short_list))
        )
        max_value = max(sum_value, max_value)
    print(f"#{test_case} {max_value}")
