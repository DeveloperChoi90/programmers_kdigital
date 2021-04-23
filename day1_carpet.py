def solution(brown, red):
    s = brown + red
    for i in range(s, 2, -1):
        if s % i == 0:
            a = s // i
            if red == (i - 2) * (a - 2):
                return [i, a]


def exactSolution(brown, red):  # 답안
    w = (brown + red) // 3
    h = 3
    while (w - 2) * (h - 2) != red:
        w -= 1
        h = (brown + red) // w
    return [w, h]


print(solution(24, 24))