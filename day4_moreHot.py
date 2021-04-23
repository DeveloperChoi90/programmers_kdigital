# Heaps 관련 알고리즘 문제
# 입력으로 주어지는 리스트의 길이가 길어지는 경우 효율성이 떨어지므로 효율성도 생각해야한다.
# 1 < scoville 길이 < 1,000,000
# 0 < K < 1,000,000,000
# 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우 -1 return

# Heaps 성질 : 최대/최소 원소를 빠르게 찾을 수 있음
# 연산
# 힙 구성(heapify) O(NlogN)
# 삽입    O(logN)
# 삭제    O(logN)

import heapq


# 전체 시간 복잡도는 NlogN
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:                     # n - 1 번 반복
        min1 = heapq.heappop(scoville)  # logN
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)  # logN
        new_scoville = min1 + min2 * 2
        heapq.heappush(scoville, new_scoville) # logN
        answer += 1

    return answer