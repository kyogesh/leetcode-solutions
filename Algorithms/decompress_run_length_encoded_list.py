class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        last = 0
        result = list()
        for i in range(0, len(nums)+1, 2):
            f_v = nums[last:i]
            freq, value = f_v if f_v else (None, None)
            if freq is None and value is None:
                continue
            result.extend([value]*freq)
            last = i
        return result
        
