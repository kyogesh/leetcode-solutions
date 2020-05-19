class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for index, num in enumerate(nums):
            for idx, second in enumerate(nums[index+1:]):
                if index == 1 and idx == 40:
                    print(num, second)
                if num + second == target:
                    print(f"{num=}, {second=}, {nums.index(num)=}, {nums.index(second)=}")
                    if nums.index(num) == nums.index(second):
                        indices1 = [i for i, x in enumerate(nums) if x == num]
                        indices2 = [i for i, x in enumerate(nums) if x == second]
                        if len(indices1) == 2:
                            return indices1
                    return [nums.index(num), nums.index(second)]
