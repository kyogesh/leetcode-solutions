class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < min(nums):
            return 0
        elif target > max(nums):
            return len(nums)
        for index, num in enumerate(nums):
            if target == num:
                return index
            elif target < num:
                return index
        
