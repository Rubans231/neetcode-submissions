class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        for i in range(len(numbers)):
            sum = numbers[l] + numbers[r]
            if l == r:
                r += 1
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                r += 1
            else:
                l += 1