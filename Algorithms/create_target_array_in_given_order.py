class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = list()
        for idx, num in enumerate(nums):
            result.insert(index[idx], num)
        return result
            
