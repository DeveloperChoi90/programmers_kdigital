# 1. 빈 문자열로 수 초기화
# 2. 수의 목록을 (크게 만드는 것 우선) 정렬
# 3. 목록에서 하나씩 꺼내어 현재 수에 이어 붙인다.
# 4. 모든 수를 다 사용할 때 까지 반복

# "크게 만드는 수"의 기준

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True) # (x * 4)[:4] 조건으로 내림차순
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer


test = [3, 30, 34, 5, 9]
print(solution(test))