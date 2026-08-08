class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for i in range(len(nums)):
            res = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res = postfix
            postfix *= nums[i]
        return res