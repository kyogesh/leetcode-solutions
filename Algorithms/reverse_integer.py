class Solution:
    def reverse(self, x: int) -> int:
        result = None
        if x > 0:
            result = int(str(x)[::-1])
        elif x < 0:
            result = -int(str(x)[1:][::-1])
        else:
            result = x

        if result < -2**31  or result > (2**31 -1 ):
            return 0
        return result
        
