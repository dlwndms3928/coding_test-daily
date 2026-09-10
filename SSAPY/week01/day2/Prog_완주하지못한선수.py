"""
[문제설명]
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
완주한 선수들의 이름이 담긴 completion이 주어질 때,
완주하지 못한 선수의 이름을 return하도록 solutoin 함수를 작성하시오.

[제한사항]
- 마라톤 경기에 참여한 선수의 수는 1명이상 100,000명 이하이다
- completion의 길이는 participant의 길이보다 1 작다
- 참가자의 이름은 1개이상 20개 이하의 알파벳 소문자로 이루어져있다
- 참가자 중에는 동명이인이 있을 수 있음
"""

from collections import Counter


def solution(participant, completion):
    p_count = Counter(participant)
    c_count = Counter(completion)
    diff = p_count - c_count
    answer = list(diff.keys())[0]
    return answer
