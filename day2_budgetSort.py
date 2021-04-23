def solution(d, budget):
    sum = 0
    count = 0
    d.sort()
    for idx in range(len(d)):
        sum += d[idx]
        if sum > budget:
            break
        count += 1

    return count


d = [2, 2, 3, 3]
budget = 10
print(solution(d, budget))
