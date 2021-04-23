# 빌려줄 학생들을 "정해진 순서"로 살펴야 하고, 이 "정해진 순서"에 따라 우선하여 빌려줄 방향을 정해야 함
# (착안점) 학생의 수는 기껏 30명
#학생 수만큼 배열로 확보
#여기에 각자가 가지고 있는 체육복의 수를 기록
#번호 순서대로 "스캔"하면서 빌려줄 관계 형성
#알고리즘의 복잡도
#여벌을 가져온 학생 처리 : reserve의 길이에 비례
#체육복을 잃어버린 학생 처리: lost의 길이에 비례
#체육복 빌려주기 처리 : 전체 학생 수 n에 비례    -> O(n)

#방법 2
#만약 전체 학생 수가 매우 크다면? -> 하지만 문제의 성질상 O(n)보다 낮은 복잡도 알고리즘은 어려움
#그런데 여벌의 체육복을 가져온 학생은 매우 적다면
#여벌의 체육복을 가져온 학생들의 번호(reserve)를 정렬하고 이것을 하나 하나 순서대로 살펴보면 빌려줄 수 있다는 다른 학생을 찾아서 처리한다. * 정렬 -> O(nlogn)
# 체육복을 빌려줄 수 있는 학생을 찾아 처리 -> O(k) * O(1)

def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1, n+1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1: i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i: i + 2] = [1, 1]
    return len([x for x in u[1:-1] if x > 0])


def solution2(n, lost, reserve): #set이라는 자료구조는 key, value값을 갖는게 아니라 있는지 없는지만 확인가능한 자료구조
    s = set(lost) & set(reserve) #set() -> O(k)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r): #sorted() -> O(klogk)
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
