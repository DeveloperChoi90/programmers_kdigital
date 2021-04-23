from day1_doublyLinkedLists import Node, DoublyLinkedList


class PriorityQueue:

    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.data.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):  # 주의 : 양방향 연결리스트의 getAt() 메서드를 이용하지 않음, 이유 : getAt() 메서드의 경우 찾는 위치까지 모든 원소를 찾아야 하므로 반복 호출 시 시간 소요가 큼
        newNode = Node(x)
        curr = self.queue.head  # 현재 위치
        while curr.next.data is not None and newNode.data < curr.next.data:  # 끝을 만나지 않는 동안 and 우선 순위 조건 (작은 수가 우선)
            curr = curr.next
        self.queue.insertAfter(curr, newNode)  # insertBefore ? insertAfter?

    def dequeue(self):
        return self.data.popAt(self.queue.getLength())

    def peek(self):
        return self.data.getAt(self.queue.getLength()).data
