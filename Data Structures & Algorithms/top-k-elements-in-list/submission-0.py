class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        for j in range(k):
            max_count = max(seen, key = seen.get)
            res.append(max_count)
            seen[max_count] = 0
        return res