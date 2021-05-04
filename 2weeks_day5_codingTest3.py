"""
문제 설명

단어 퍼즐은 주어진 단어 조각들을 이용해서 주어진 문장을 완성하는 퍼즐입니다.
이때, 주어진 각 단어 조각들은 각각 무한개씩 있다고 가정합니다.
예를 들어 주어진 단어 조각이 [“ba”, “na”, “n”, “a”]인 경우 "ba", "na", "n", "a" 단어 조각이 각각 무한개씩 있습니다.
이때, 만들어야 하는 문장이 “banana”라면 “ba”, “na”, “n”, “a”의 4개를 사용하여 문장을 완성할 수 있지만,
“ba”, “na”, “na”의 3개만을 사용해도 “banana”를 완성할 수 있습니다.
사용 가능한 단어 조각들을 담고 있는 배열 strs와 완성해야 하는 문자열 t가 매개변수로 주어질 때,
주어진 문장을 완성하기 위해 사용해야 하는 단어조각 개수의 최솟값을 return 하도록 solution 함수를 완성해 주세요.
만약 주어진 문장을 완성하는 것이 불가능하면 -1을 return 하세요.

제한사항
- strs는 사용 가능한 단어 조각들이 들어있는 배열로, 길이는 1 이상 100 이하입니다.
- strs의 각 원소는 사용 가능한 단어조각들이 중복 없이 들어있습니다.
- 사용 가능한 단어 조각들은 문자열 형태이며, 모든 단어 조각의 길이는 1 이상 5 이하입니다.
- t는 완성해야 하는 문자열이며 길이는 1 이상 20,000 이하입니다.
- 모든 문자열은 알파벳 소문자로만 이루어져 있습니다.
"""

"""
DP문제지만 BFS로 푼 문제.
"banana"에서 "ba"는 0 -> 2로 가는 간선,
"na"는 2 -> 4, 4 -> 6,
"n"는 2 -> 3, 4 -> 5, "a"는 3 -> 4, 5 -> 6,
이렇게 간선을 다 만든 다음에 0에서 출발해서 6 (t의 길이)까지의 최단 길이를 BFS로 구하는 풀이입니다.
"""

from collections import deque
import re


def solution(strs, t):
    graph = [[] for _ in range(len(t))]
    for s in strs:
        i, p = 0, re.compile(s)
        while True:
            m = p.search(t, pos=i)
            if not m:
                break
            graph[m.start()].append(m.end())
            i = m.start() + 1

    queue = deque([0])
    visited = [0] * len(t)

    while queue:
        c = queue.popleft()

        for a in graph[c]:
            if a == len(t):
                return visited[c] + 1
            if not visited[a]:
                visited[a] = visited[c] + 1
                queue.append(a)

    return -1


"""
DP풀이
strs에 존재하는 문자열의 길이만을 담은 set을 이용해서
0부터 len(n)까지의 i에 대해
i + size가 t의 길이보다 작고, t[i : i + size]가 strs에 있는 문자열이면
i + size에서의 dp값은 기존의 값, dp[i + size]와
dp[i]에서 문자 하나를 더 붙인 값, dp[i] + 1 둘 중
작은 값으로 바꿉니다.
그리고 최종적으로 dp[-1]을 반환합니다.
"""


def solution2(strs, t):
    n = len(t)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    sizes = set(map(len, strs))
    strs = set(strs)

    for i in range(n + 1):
        for size in sizes:
            if i + size < n + 1 and t[i: i + size] in strs:
                dp[i + size] = min(dp[i + size], dp[i] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


str1 = ["ba", "na", "n", "a"]  # t = "banana"
str2 = ["app", "ap", "p", "l", "e", "ple", "pp"]  # t = "apple"
str3 = ["ba", "an", "nan", "ban", "n"]  # t = "banana"
