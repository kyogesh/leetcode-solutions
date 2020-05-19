class Solution:
    def titleToNumber(self, s: str) -> int:
        pow = 1
        col_num = 0
        for letter in s[::-1]:
            col_num += (ord(letter) - 64)*pow
            pow *= 26
        return col_num
        
