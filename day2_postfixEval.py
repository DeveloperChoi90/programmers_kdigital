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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif token == ')':
            while True:
                x = opStack.pop()
                if x == '(':
                    break
                postfixList.append(x)
        # elif token == ')':
        #     pass
        else:
            if prec[token] == 1:
                opStack.push(token)
            elif prec[token] == 2 or prec[token] == 3:
                tmp = prec[token]
                while not opStack.isEmpty():
                    top = opStack.peek()
                    if prec[top] < tmp:
                        break
                    postfixList.append(opStack.pop())
                opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)

        elif token == '*':
            val1 = valStack.pop()
            val2 = valStack.pop()
            valStack.push(val2 * val1)

        elif token == '/':
            val1 = valStack.pop()
            val2 = valStack.pop()
            valStack.push(val2 / val1)

        elif token == '+':
            val1 = valStack.pop()
            val2 = valStack.pop()
            valStack.push(val2 + val1)

        elif token == '-':
            val1 = valStack.pop()
            val2 = valStack.pop()
            valStack.push(val2 - val1)

    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)          # ?????????????????? ???????????? ??????
    postfix = infixToPostfix(tokens)    # ?????? ???????????? ?????? ??????????????? ??????
    val = postfixEval(postfix)          # ?????? ???????????? ??????????????? ?????? ?????? ???????????? ???????????? ??????
    return val


print(solution("(1 + 2) * (3 + 4)"))