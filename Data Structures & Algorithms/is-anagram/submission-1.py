class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for j in t:
            if j in hashmap and hashmap[j] > 0:
                hashmap[j] -= 1
            else:
                return False
        return True