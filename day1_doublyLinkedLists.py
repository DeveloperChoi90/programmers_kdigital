class Node:
    def __init__(self, item):
        self.node = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:  # tail 도 dummy node가 존재 하기 때문에
            curr = curr.next
            result.append(curr.data)
        return result

    def revers(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        if pos > self.nodeCount // 2:  #pos가 뒤쪽과 가까운 위치일 경우 뒤쪽에서부터 찾기 위해
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1

        else:
            i = 0  # dummy node가 생기면서 i = 1 번째가 아니라 i = 0 으로 바뀜
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        data = curr.data
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return data

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        data = curr.data
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

