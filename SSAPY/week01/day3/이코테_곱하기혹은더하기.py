"""
[입력 조건]
첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어진다.
( 1<= S의 길이 <= 20 )

[출력 조건]
첫째 줄에 만들어질 수 있는 가장 큰 수를 출력
"""

T = input()
ans = int(T[0])
for i in T[1:]:
    i = int(i)

    if ans != 0 and i <= 1:
        ans *= i
    else:
        ans += i
print(f"{ans}")
