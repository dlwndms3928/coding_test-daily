'''
[문제 설명]
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
각 기능은 진도가 100%일 때 서비스에 반영할 수 있다.
또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 
앞에 있는 기능보다 먼저 개발될 수 있고,
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.

먼저 배포되어야하는 순서대로 작업의 진도가 적힌 정수배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 sppeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성해라

[제한 사항]
1. 작업의 개수(progresses, speeds 배열의 길이)는 100개 이하이다.
2. 작업 진도는 100 미만의 자연수이다.
3. 작업 속도는 100 이하의 자연수이다.
4. 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정
    예를들어 진도율이 95%인 작업의 개발 속도가 하루에 4%면, 배포는 2일뒤에 일어남

[입출력 에]
progresses	    speeds	     return
[93, 30, 55]	[1, 30, 5]	 [2, 1]

'''
import math

def solution(progresses, speeds):
    answer = []
    comple_day = []
    length = len(progresses)
    for i in range(length):
        k=math.ceil((100-progresses[i])/speeds[i])
        comple_day.append(k)
    group_most = comple_day[0]
    count = 1
    for j in range(1,length) :
        # 같은 그룹인 경우
        if group_most >= comple_day[j]:
            count += 1
        # 다른 그룹인 경우
        else :
            answer.append(count)
            group_most = comple_day[j]
            count = 1
    answer.append(count)  

    return answer
