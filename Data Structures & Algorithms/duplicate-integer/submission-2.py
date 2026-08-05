class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashlist = {}

        for i in nums:
            if i in hashlist:
                return True
            hashlist[i] = 1
        return False
