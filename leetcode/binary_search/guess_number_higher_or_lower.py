# Sample 'guess' implementation
def guess(num):
    if num > 6:
        return -1
    elif num < 6:
        return 1
    else:
        return 0


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# Binary Search
# Time Complexity: O(log(k))
# Space Complexity: O(1)
# k - Size of the search space (from 1 to n)
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = l + (r - l) // 2
            result = guess(m)

            if result == -1:
                r = m - 1
            elif result == 1:
                l = m + 1
            else:
                return m

        return -1


# Iterative Ternary Search
# Time Complexity: O(log3(k))
# Space Complexity: O(1)
# k - Size of the search space (from 1 to n)
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            result1 = guess(m1)
            result2 = guess(m2)

            if result1 == 0:
                return m1
            elif result2 == 0:
                return m2

            if result1 == -1:
                r = m1 - 1
            elif result2 == 1:
                l = m2 + 1
            else:
                l = m1 + 1
                r = m2 - 1

        return -1


# Recursive Ternary Search
# Time Complexity: O(log3(k))
# Space Complexity: O(log3(k))
# k - Size of the search space (from 1 to n)
class Solution:
    def guessNumber(self, n: int) -> int:
        return self.__ternary_search(1, n)

    def __ternary_search(self, l, r):
        if l > r:
            return -1

        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        result1 = guess(m1)
        result2 = guess(m2)

        if result1 == 0:
            return m1
        elif result2 == 0:
            return m2

        if result1 == -1:
            return self.__ternary_search(l, m1 - 1)
        elif result2 == 1:
            return self.__ternary_search(m2 + 1, r)
        else:
            return self.__ternary_search(m1 + 1, m2 - 1)
