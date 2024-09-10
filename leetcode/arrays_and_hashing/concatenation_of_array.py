from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums * 2


# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return [
#             num
#             for _ in range(2)
#             for num in nums
#         ]
