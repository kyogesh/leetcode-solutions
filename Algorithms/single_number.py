class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = dict()
        for num in nums:
            if num not in result:
                result[num] = 1
                continue
            result[num] += 1
        return [k for k,v in result.items() if v == 1][0]
            
