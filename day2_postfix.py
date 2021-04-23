class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for word in S:
        if word in prec:
            if opStack.isEmpty():
                opStack.push(word)

            elif prec[word] == 1:
                opStack.push(word)

            elif prec[opStack.peek()] < prec[word]:
                opStack.push(word)

            else:
                if opStack.peek() == word:
                    answer += opStack.pop()
                    answer += word
                else:
                    answer += opStack.pop()
                    opStack.push(word)

        elif word == ')':
            while True:
                tmp = opStack.pop()
                if tmp == '(':
                    break
                answer += tmp

        else:
            if word != ')':
                answer += word

    while not opStack.isEmpty():
        tmp = opStack.pop()
        if tmp != '(':
            answer += tmp

    return answer


def solution2(S):  # 통과한 코드
    answer = ''
    opStack = ArrayStack()
    for word in S:
        if word != '*' and word != '/' and word != '+' and word != '-' and word != '(' and word != ')':
            answer += word

        elif word == ')':
            while True:
                x = opStack.pop()
                if x == '(':
                    break
                answer += x

        elif prec[word] == 1:
            opStack.push(word)

        elif prec[word] == 2 or prec[word] == 3:
            p = prec[word]
            while not opStack.isEmpty():
                top = opStack.peek()
                if prec[top] < p:
                    break
                answer += opStack.pop()
            opStack.push(word)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


S = "A**B+C"
print(solution(S))
