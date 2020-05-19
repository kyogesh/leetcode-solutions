class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while True:
            quotient, remainder = divmod(n, 5)
            if quotient == 0:
                break
            result += quotient
            n = quotient
        return result
