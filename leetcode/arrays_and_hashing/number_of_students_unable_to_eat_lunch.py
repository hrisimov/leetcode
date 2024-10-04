from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        students_rotations = 0

        while students_rotations != len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                students_rotations = 0
            else:
                students.rotate(-1)
                students_rotations += 1

        return len(students)

# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         students_count = Counter(students)
#
#         for s in sandwiches:
#             if students_count[s] == 0:
#                 return students_count[1 - s]
#             students_count[s] -= 1
#
#         return 0
