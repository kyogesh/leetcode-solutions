class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        sum_ = 0
        product = 1
        for num in nums:
            sum_ += num
            product *= num
        return product - sum_
