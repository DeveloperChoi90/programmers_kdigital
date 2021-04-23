#DFS / BFS 문제
# 요약
# - 재귀적인 성질을 가진 "한 붓 그리기" 문제
#  -> 재귀적인 성질을 가진 "그래프의 깊이 우선 탐색"을 응용하여 해결

# 사전을 이용하여 각 공항에서 출발하는 항공권의 리스트를 표현

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]] #t[0] : 출발공항, t[1] : 도착공항
    for r in routes:  # 시간 복잡도 NlogN # r 은 routes의 key 값
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0: #더 이상 갈 수 있는곳이 없는 경우
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]