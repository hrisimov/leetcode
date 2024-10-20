from functools import lru_cache


# Recursive Fibonacci sequence using memoization
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Iterative Fibonacci sequence with space optimization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         previous = current = 1
#
#         for _ in range(2, n + 1):
#             previous, current = current, previous + current
#
#         return current


# Fibonacci sequence with matrix exponentiation
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 1:
#             return 1
#
#         matrix_power = n - 1
#         matrix_power_binary = bin(matrix_power)[2:]
#
#         exponents = self.__calculate_exponents(len(matrix_power_binary) - 1)
#         result = self.__multiply(
#             self.__multiply_exponents(matrix_power_binary, exponents),
#             [
#                 [1],
#                 [1],
#             ],
#         )
#
#         return result[0][0]
#
#     def __calculate_exponents(self, two_power):
#         exponents = [
#             [
#                 [1, 1],
#                 [1, 0],
#             ],
#         ]
#
#         for _ in range(1, two_power + 1):
#             exponents.append(
#                 self.__multiply(exponents[-1], exponents[-1])
#             )
#
#         return exponents
#
#     def __multiply_exponents(self, matrix_power_binary, exponents):
#         result = [
#             [1, 0],
#             [0, 1],
#         ]
#
#         two_power = len(matrix_power_binary) - 1
#
#         for digit in matrix_power_binary:
#             if digit == '1':
#                 result = self.__multiply(result, exponents[two_power])
#             two_power -= 1
#
#         return result
#
#     @staticmethod
#     def __multiply(matrix1, matrix2):
#         result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
#
#         for i in range(len(matrix1)):
#             for j in range(len(matrix2[0])):
#                 for k in range(len(matrix1[0])):
#                     result[i][j] += matrix1[i][k] * matrix2[k][j]
#
#         return result
