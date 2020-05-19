class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = [s for s in S for j in J if j==s]
        return len(result)

        
