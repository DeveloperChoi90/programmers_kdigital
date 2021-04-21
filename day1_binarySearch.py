def solution(L, x):  # L 리스트는 정렬된 정수형 타입의 리스트라고 가정
    lower = 0
    upper = len(L)
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle
        if lower == upper:
            return idx


# 재귀 함수로 구현
def binsearch(L, x, l, u):
    if l == u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binsearch(L, x, l, mid)
    else:
        return binsearch(L, x, mid + 1, u)
