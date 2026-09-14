"""
0~999999 사이의 수를 나열하여 만든 암호문이 있다.
암호문을 급히 수정해야 할 일이 발생했는데, 이 함호문은 특수 제작된 처리기로만 수정 가능하다.
이 처리기는 다음과 같이 1개의 기능을 제공한다.
1. !(삽입) x,y,s: 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
s는 덧붙일 숫자들이다.
위 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 암호문을 수정하고,
수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.

[입력]

첫번째 줄: 원본 암호문의 길이 N(10<=N<=20의 정수)
두번째 줄: 원본 암호문
세번째 줄: 명령어 개수
네번째 줄: 명령어
위와같은 네 줄이 한개의 테스트 케이스이며, 총 10개의 테스트가 주어진다.

[출력]
#기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.
"""

for test_case in range(1, 11):
    length = int(input())
    origin = list(map(int, input().split()))
    command_num = int(input())
    command = list(input().split())
    idx = 0
    count = 0
    while 1:
        if command[idx] == "I":
            x = int(command[idx + 1])
            y = int(command[idx + 2])
            for i in range(1, y + 1):
                origin.insert(x + (i - 1), int(command[idx + 2 + i]))
            idx += 3 + y
            count += 1
            if count == command_num:
                break
    print(f"#{test_case} {' '.join(map(str,origin[0:10]))}")
