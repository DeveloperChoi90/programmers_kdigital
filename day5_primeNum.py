from itertools import combinations


def solution(n):
    answer = 0

    # 먼저 n 이하의 소수를 알아내자.
    a = [False,False] + [True]*(n-1) #  왜 2가 아니고 1이지? -> 0부터 시작이니까

    primes = []
    for i in range(2,n+1): # 2~n
        if a[i] == True: # 먼저 가장 작은 수를 소수 리스트에 추가하고,
            primes.append(i)
            # 그의 배수들을 제거해준다 (False)
            for j in range(2*i, n+1 ,i):
                a[j] = False


    # 알아낸 소수들이 들어있는 리스트에서 3가지를 뽑는 조합을 모두 구해서 리스트화 시킨다.
    # for loop 중첩시켜야한다.
    result = list(combinations(primes,3))

    # 합이 n인지 확인한다.
    for r in result:
        if sum(r) == n:
            answer += 1


    return answer