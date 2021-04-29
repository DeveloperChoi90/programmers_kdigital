from itertools import combinations


def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        combi = combinations(weights, i)
        answer += [sum(candies) for candies in combi].count(m)

    return answer


def solution2(m, weights):
    answer = 0
    for i in range(len(weights)):
        results = map(sum, combinations(weights, i))
        for result in results:
            if result == m:
                answer += 1
    return answer


# 비트 연산자 사용 하여 무게를 사용, 사용하지않음 두가지 경우의 수 즉, 2^n 승 이용 모든 경우의 수를 가지고 계산
def solution3(m, weights):
    answer = 0
    for stat in range(1, (1 << len(weights))):
        now = 0
        for i in range(len(weights)):
            if stat & 1 << i:
                now += weights[i]
        if now == m:
            answer += 1
    return answer


m = 3000
weights = [500, 1500, 2500, 1000, 2000]
# print(solution(m, weights))
print(solution2(m, weights))
# print(solution3(m, weights))
