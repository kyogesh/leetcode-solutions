class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        list_ = s.strip().split(' ')
        return len(list_[-1])
        
