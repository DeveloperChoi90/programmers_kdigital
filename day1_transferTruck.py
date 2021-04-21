def solution(max_weight, specs, names):
    dic = dict(specs)
    load_max = max_weight
    count = 1
    for name in names:
        val = int(dic[name])
        if val <= load_max:
            load_max -= val
        else:
            count += 1
            load_max = max_weight - val

    return count


max_weight = 300
spaces = [["toy", "70"], ["snack", "200"]]
names = ["toy", "snack", "toy"]

print(solution(max_weight, spaces, names))
