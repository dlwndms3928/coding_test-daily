"""
[문제 설명]
rows * colums까지의 숫자가 한 줄씩 순서대로 적혀있다
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해,
테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 한다.
각 회전은 (x1,y1,x2,y2)인 정수 4개로 표현하며, 그 의미는 다음과 같다.
 - x1행 y1열부터 x2행 y2열 까지의 영역에 해당하는 직사각형에서
    테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전한다.
"""


def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)]
    number = 1
    answer = []
    # 매트릭스 완성
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = number
            number += 1
    # 배열 리스트 마다 값 설정하기
    for query in range(len(queries)):
        start_row = queries[query][0] - 1
        start_col = queries[query][1] - 1
        end_row = queries[query][2] - 1
        end_col = queries[query][3] - 1
        temp = matrix[start_row][start_col]
        min_val = temp
        # 1. 왼쪽 변: 아래 값을 위로 당김
        for r in range(start_row, end_row):
            matrix[r][start_col] = matrix[r + 1][start_col]
            if matrix[r][start_col] < min_val:
                min_val = matrix[r][start_col]
        # 2. 아래 변: 오른쪽 값을 왼쪽으로 당김
        for c in range(start_col, end_col):
            matrix[end_row][c] = matrix[end_row][c + 1]
            if matrix[end_row][c] < min_val:
                min_val = matrix[end_row][c]
        # 3. 오른쪽 변: 위 값을 아래로 당김 (아래에서부터 거꾸로)
        for r in range(end_row, start_row, -1):
            matrix[r][end_col] = matrix[r - 1][end_col]
            if matrix[r][end_col] < min_val:
                min_val = matrix[r][end_col]
        # 4. 위쪽 변: 왼쪽 값을 오른쪽으로 당김 (오른쪽에서부터 거꾸로)
        for c in range(end_col, start_col, -1):
            matrix[start_row][c] = matrix[start_row][c - 1]
            if matrix[start_row][c] < min_val:
                min_val = matrix[start_row][c]
        # 5. temp를 한 칸 오른쪽에
        matrix[start_row][start_col + 1] = temp
        answer.append(min_val)
    return answer
