def solution(seat):
    dit = {}
    for coord in seat:
        dit[str(coord)] = dit.get(str(coord), 0) + 1

    holdSeat = [k for k in dit.keys()]
    answer = len(holdSeat)

    return answer


seat = [[1,1], [2,2], [3,3]]
print(solution(seat))
