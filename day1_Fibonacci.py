# 재귀적으로 풀었을 경우
def solution(x):
    if x <= 1:
        return x
    else:
        return solution(x - 1) + solution(x - 2)


# 반복문으로 풀었을 경우
def iter(x):
    if x <= 1:
        return x
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= x:
            t0, t1 = t1, t0 + t1
            i += 1
        return t1


a = 8
print(solution(a))
print(iter(a))
