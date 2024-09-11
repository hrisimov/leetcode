class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_brackets_stack = []
        brackets_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for bracket in s:
            if bracket in brackets_map:
                if not open_brackets_stack or open_brackets_stack[-1] != brackets_map[bracket]:
                    return False
                open_brackets_stack.pop()
            else:
                open_brackets_stack.append(bracket)

        return not open_brackets_stack
