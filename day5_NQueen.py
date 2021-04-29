# N-Queen은 다해봐야겠다.
# 리스트로 열을 나타냄 -> 인덱스로 행을 표현 ( 2차원 -> 1차원으로 낮춤)
# 리스트의 값은 열, 인덱스는 행 -> 공간복잡도를 획기적으로 줄일 수 있음
# 대각선 -> 우하향 : row - col 가 같다, 우상향 : row + col 이 같다
# 백트래킹 : 가지치기
# DFS : Depth First Search - 깊이 우선 탐색 (Stack, Recursive)
def n_queen(lst, row, n):
    """
    lst : 어떤 열에 담았는지 두는 List
    row : 현재 행
    n : 체스판 사이즈(N * N) 종료조건
    """
    count = 0
    if row == n:
        return 1
    # check를 안한 상태!
    for col in range(n):
        lst[row] = col  # 인덱스 : row, 값 : col
        for i in range(row):  # 0 ~ 바로 전까지!
            # 열 체크
            if lst[i] == lst[row]:
                break
            # 대각선 체크(우상향, 우하향) --> 한줄로 구현 가능
            # 우상향
            if lst[i] + i == lst[row] + row:
                break
            # 우하향
            if lst[i] - i == lst[row] - row:
                break
        else:
            count += n_queen(lst, row + 1, n)
    return count


def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count


def solution(n):
    return n_queen([-1] * n, 0, n)  # zero-base indexing


def solution2(n):
    return dfs([0]*n, 0, n)