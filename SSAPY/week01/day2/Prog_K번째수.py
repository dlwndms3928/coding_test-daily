'''
[문제설명]
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려한다.
예를 들어 array가 [1,5,2,6,3,7,4], i=2, j=5, k=3이라면
1. array의 2번째부터 5번째까지 자르면 [5,2,6,3]입니다.
2. 1에서 나온 배열을 정렬하면 [2,3,5,6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i,j,k]를 원소로 가진 2차원 배열 commands가 
매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한
연산을 적용했을 때 나온 결과를 배열에 담아 return하도록
solution 함수를 작성해주세요.

[제한사항]
- array의 길이는 1이상 100이하입니다.
- array의 각 원소는 1이상 100 이하입니다.
- commands의 길이는 1이상 50 이하입니다.
- commands의 각 원소의 길이가 3입니다.
'''
# 더 효율적인 코드
def solution(array, commands):
    answer=[]
    
    for start,end,k in commands:
        sort_array=array[(start-1):end]
        sort_array.sort()
        answer.append(sort_array[k-1])
    return answer


'''array[3:0-
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        sort_array=array[commands[i][0]-1:commands[i][1]]
        sort_array.sort()
        answer.append(sort_array[commands[i][2]-1])
    return answer
'''


'''
    array[commands[0][0]:commands[0][1]+1]
    array[commands[1][0]:commands[1][1]+1]
    array[commands[2][0]:commands[2][1]+1]
'''