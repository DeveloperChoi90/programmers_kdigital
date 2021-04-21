class Node:
    def __init__(self, item):
        self.node = item
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)  #
        self.tail = None
        self.head.next = self.tail

    # def __repr__(self):
    #     if self.nodeCount == 0:
    #         return 'LinkedList: empty'
    #
    #     s = ''
    #     curr = self.head.next
    #     while curr is not None:
    #         s += repr(curr.data)
    #         if curr.next is not None:
    #             s += ' -> '
    #         curr = curr.next
    #     return s

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0  # dummy node가 생기면서 i = 1 번째가 아니라 i = 0 으로 바뀜
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:  # dummy node때문에 curr.next 시작
            curr = curr.next  # dummy node때문에 이동 후 curr.data 확인
            result.append(curr.data)
        return result

    # def insertAt(self, pos, newNode):                     # insertAfter 함수 작성 전
    #     if pos < 1 or pos > self.nodeCount + 1:
    #         return False
    #     if pos == 1:
    #         newNode.next = self.head
    #         self.head = newNode
    #     else:
    #         if pos == self.nodeCount + 1:
    #             prev = self.tail
    #         else:
    #             prev = self.getAt(pos - 1)
    #         newNode.next = prev.next
    #         prev.next = newNode
    #     if pos == self.nodeCount + 1:
    #         self.tail = newNode
    #
    #     self.nodeCount += 1
    #     return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    # def popAt(self, pos):                        # pos가 가리키는 위치의 (1 <= pos <= nodeCount) node를 삭제하고 그 node의 데이터를 리턴
    #     if pos < 1 or pos > self.nodeCount:      # 주의사항 : (1) 삭제하려는 node 가 맨 앞의 것일 때 -> prev가 없음
    #         raise IndexError                     # -> Head 조정 필요  ( * 유일한 노드를 삭제할 때? -> 이 두 조건에 의해 처리되는가?
    #                                              #         (2) 리스트 맨 끝의 node를 삭제할 때 -> tail 조정 필요
    #     if self.nodeCount == 1:
    #         data = self.head.data
    #         self.head = None
    #         self.tail = None
    #         self.nodeCount -= 1
    #         return data
    #
    #     if pos == 1:
    #         data = self.head.data
    #         self.head = self.head.next
    #         self.nodeCount -= 1
    #         return data
    #
    #     else:
    #         prev = self.getAt(pos - 1)
    #         curr = prev.next
    #         data = curr.data
    #         if pos == self.nodeCount:
    #             prev.next = None
    #             self.tail = prev
    #         else:
    #             prev.next = curr.next
    #
    #     self.nodeCount -= 1
    #     return data

    def popAfter(self, prev):
        if prev.next is None:
            return None
        curr = prev.next
        data = curr.data
        prev.next = curr.next
        if curr.next is None:
            self.tail = prev

        self.nodeCount -= 1
        return data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.next = L.head.next  # self.tail.next = L.head (dummy node 생성전 code)
        if L.tail:  # L의 리스트가 비어있는 경우 tail은 None이기 때문
            self.tail = L.tail
        self.nodeCount += L.nodeCount
