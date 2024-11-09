import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1, l2):
    head = tail = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return head.next


# Merging lists one by one
# Time Complexity: O(n * k)
# Space Complexity: O(1)
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        result = lists[0]

        for i in range(1, len(lists)):
            result = merge(result, lists[i])

        return result


# Divide and Conquer with iteration
# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            len(lists) % 2 == 1 and lists.append(None)

            for i in range(0, len(lists), 2):
                merged_lists.append(merge(lists[i], lists[i + 1]))

            lists = merged_lists

        return lists[0]


# Divide and Conquer with recursion
# Time Complexity: O(n * log(k))
# Space Complexity: O(log(k))
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.__divide(lists, 0, len(lists) - 1)

    def __divide(self, lists, s, e):
        if s == e:
            return lists[s]

        # m = (s + e) // 2
        m = s + (e - s) // 2
        left_half = self.__divide(lists, s, m)
        right_half = self.__divide(lists, m + 1, e)
        return merge(left_half, right_half)  # conquer


class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


# Heap Queue
# Time Complexity: O(k * log(k) + n * log(k))
# Space Complexity: O(k)
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []

        for l in lists:
            l and heapq.heappush(hq, ListNodeWrapper(l))

        head = tail = ListNode()

        while hq:
            l = heapq.heappop(hq).node
            tail.next = l
            tail = tail.next
            l.next and heapq.heappush(hq, ListNodeWrapper(l.next))

        return head.next


# Brute Force
# Time Complexity: O(n + n * log(n) + n)
# Space Complexity: O(n)
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for l in lists:
            while l:
                nodes.append(l)
                l = l.next

        nodes.sort(key=lambda n: n.val)
        head = tail = ListNode()

        for node in nodes:
            tail.next = node
            tail = tail.next

        return head.next


# Finding head node with min value iteratively
# Time Complexity: O(n * k)
# Space Complexity: O(1)
# k - Number of linked lists
# n - Total number of nodes across k linked lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = ListNode()

        while True:
            index = self.__get_index_of_min_node(lists)

            if index is None:
                return head.next

            tail.next = lists[index]
            tail = tail.next
            lists[index] = lists[index].next

    @staticmethod
    def __get_index_of_min_node(nodes):
        min_value = float('inf')
        index = None

        for i in range(len(nodes)):
            if nodes[i] is None or nodes[i].val >= min_value:
                continue
            min_value = nodes[i].val
            index = i

        return index
