def solution(board, nums):
    answer = 0
    size = len(board)  # 빙고판의 사이즈 (N)

    hor = [0] * size   #가로
    ver = [0] * size   #세로
    diag = [0] * 2

    idx = {}

    # 빙고에서 중요한건 결국 "인덱스"
    # 인덱스를 먼저 기억해두는게 중요
    # 이중 loop를 통해서 -> (x, y)
    for i in range(size):   # 행
        for j in range(size):   # 열 [i][j]
            idx[board[i][j]] = (i, j)
    # "num"을 순회
    # i 는 행 좌표상 y값, j는 x값
    for elem in nums:
        y, x = idx[elem]
    # 대각선의 값은 어떻게 처리?
    # x = y, x + y == size - 1
        if y == x:
            diag[0] += 1
        if y == size - x - 1:
            diag[1] += 1
        ver[x] += 1
        hor[y] += 1

    # counting
    # hor = [2, 4, 3, 2, 5]

    return hor.count(size) + ver.count(size) + diag.count(size)


# index 가 중요
# dictionary : 키의 유일성, 가장 빠르게 계산 가능
# N x N 빙고판에서 빙고가 나오기 위해선 한줄에 nums의 몇개의 원소
board = [[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]]
