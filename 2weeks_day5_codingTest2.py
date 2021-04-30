def solution(arr):
    arr.sort()
    start = 0
    cnt = 0
    for s, e in arr:
        if s >= start:
            start = e
            cnt += 1

    return cnt


def solution2(arr):
    arr.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 기준으로 우선정렬

    end = 0
    cnt = 0
    for s, e in arr:
        if s >= end:
            end = e
            cnt += 1

    return cnt


arr = [[1, 4], [2, 6], [4, 7]]
print(solution(arr))
