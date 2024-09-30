class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val

# class BrowserHistory:
#
#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.i = 0
#         self.len = 1
#
#     def visit(self, url: str) -> None:
#         if self.i + 1 < len(self.history):
#             self.history[self.i + 1] = url
#         else:
#             self.history.append(url)
#
#         self.i += 1
#         self.len = self.i + 1
#
#     def back(self, steps: int) -> str:
#         self.i = max(self.i - steps, 0)
#         return self.history[self.i]
#
#     def forward(self, steps: int) -> str:
#         self.i = min(self.i + steps, self.len - 1)
#         return self.history[self.i]
