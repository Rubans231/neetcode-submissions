class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for i in s1:
            count1[i] = 1 + count1.get(i, 0)
        
        for j in range(len(s2)):
            count2, cur = {}, 0
            for r in range(j, len(s2)):
                count2[s2[r]] = 1 + count2.get(s2[r], 0)
                if count1.get(s2[r], 0) < count2.get(s2[r]):
                    break
                if count1.get(s2[r]) == count2.get(s2[r]):
                    cur += 1

                if cur == len(count1): return True
        return False