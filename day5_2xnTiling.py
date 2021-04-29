def solution(n):
    # 기저 조건 n = 1, n = 2
    if n == 1:
        return 1
    if n == 2:
        return 2

    return (solution(n - 1) + solution(n - 2)) % 1000000007

# 반복 호출이 너무 많이 일어난다 -> dynamics programming
# 메모이제이션


def solution2(n):
    dp = [1, 2] # 1일때랑 2일때
    for i in range(2, n):
        dp.append((dp[i-1] + dp[i-2]) % 1000000007)
    return dp[-1]   # dp가 점점 너무 커지는 경우가 생겨서 %100000007를 미리 해주는 것이 중요