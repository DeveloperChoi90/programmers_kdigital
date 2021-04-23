# 원칙
# - 앞 자리에 큰 수가 오는 것이 전체를 크게 만든다.
#  -> 따라서, 큰 것을 우선해서 골라 담고 싶다.

# 방법
# -앞 자리에서부터 하나씩 골라 담되, 지금 담으려는 것보다 작은 것들은 도로 뻰다! 단, 뺄 수 있는 수효에 도달할 때까지만
# - 큰 수가 앞 자리에, 작은 수가 뒷자리 놓이도록
# - 아직 뺄 개수(k)를 채우지 못한 경우는 반환되는 숫자에서 뒤에서 k자리를 빼주고 반환

#복잡도의 경우 O(n)
def solution(number, k):
    collected = []
    for idx, num in enumerate(number): # O(n^2) 가 아니라 O(n)이다 이유 : 최악의 경우 num이 한번 들어가거나 한번 빠져나오는 경우만 존재
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[idx:])
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)

    return answer