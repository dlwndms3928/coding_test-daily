"""
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약사항]
N은 5이상 50 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고, 다음 줄에 N개의 숫자가 주어진다.
10
5
1 4 7 8 0

[출력]
출력의 각 줄은 #t로 시작하고, 공백을 한칸 둔 다음 정답을 출력한다.
#1 0 1 4 7 8
...

"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    test = list(map(int, input().split()))
    test.sort()
    print(f"#{test_case} {' '.join(map(str,test))}")
