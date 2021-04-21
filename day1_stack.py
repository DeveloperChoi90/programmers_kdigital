from day1_doublyLinkedLists import Node
from day1_doublyLinkedLists import DoublyLinkedList


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):  # 스택의 크기를 리턴
        return len(self.data)

    def isEmpty(self):  # 스택이 비어있는지 판단
        return self.size == 0

    def push(self, item):  # 데이터 원소 추가
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):  # 스택의 가장 꼭대기의 data값을 불러옴
        return self.data[-1]


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)  # 노드의 마지막에 추가됨

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data


def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty():
                return False

            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()


test = "[(A + B) * C"
print(solution(test))
