from collections import Counter


# def solution(v): #test시 런타임에러 발생
#     answer = []
#     x = []
#     y = []
#     for idx in range(len(v)):
#         x.append(v[idx][0])
#         y.append(v[idx][1])
#
#     for v in x:
#         if Counter(x)[v] == 1:
#             answer.append(v)
#     for v in y:
#         if Counter(y)[v] == 1:
#             answer.append(v)
#
#     return answer

def solution(v):
    answer = []
    for i in zip(*v):
        y = Counter(i)
        answer.extend([i for i in y if y[i] == 1])

    return answer


v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))
