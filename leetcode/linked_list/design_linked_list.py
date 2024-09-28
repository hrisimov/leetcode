class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        i = 0

        while current != self.right:
            if i == index:
                return current.val
            current = current.next
            i += 1

        return -1

    def addAtHead(self, val: int) -> None:
        self.__insert_node_between_nodes(
            ListNode(val),
            self.left,
            self.left.next,
        )

    def addAtTail(self, val: int) -> None:
        self.__insert_node_between_nodes(
            ListNode(val),
            self.right.prev,
            self.right,
        )

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        i = 0

        while current:
            if i == index:
                self.__insert_node_between_nodes(
                    ListNode(val),
                    current.prev,
                    current,
                )
                break
            current = current.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        i = 0

        while current != self.right:
            if i == index:
                current.prev.next = current.next
                current.next.prev = current.prev
                break
            current = current.next
            i += 1

    @staticmethod
    def __insert_node_between_nodes(new, prev, next):
        new.next = next
        next.prev = new
        new.prev = prev
        prev.next = new
