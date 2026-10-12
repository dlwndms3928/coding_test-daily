# 1-9까지 있는지 확인해주는 함수
# + 겹치는게 있는지까지 확인(set은 중복 없애서)
def is_valid(nums):
    return set(nums) == set(range(1, 10))


def solve(matrix):
    # 가로
    for r in matrix:
        if not is_valid(r):
            return 0

    # 세로
    for c in zip(*matrix):
        if not is_valid(c):
            return 0

    # 3*3
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            box = []
            for m in range(3):
                for k in range(3):
                    box.append(matrix[i + m][j + k])
            if not is_valid(box):
                return 0
    return 1


T = int(input())
for test_case in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{test_case} {solve(matrix)}")
