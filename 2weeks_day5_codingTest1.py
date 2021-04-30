def solution(n, signs):
    for start in range(n):
        tmps = [idx for idx, flat in enumerate(signs[start]) if flat]
        while tmps:
            tmp = tmps.pop()
            for end, flat in enumerate(signs[tmp]):
                if flat and signs[start][end] == 0:
                    signs[start][end] = 1
                    tmps.append(end)
    return signs
