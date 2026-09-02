class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remaining = len(t)
        needed = {}
        res = ""

        if remaining == 0 or remaining > len(s):
            return ""

        for r in range(remaining):
            needed[t[r]] = 1 + needed.get(t[r], 0)
        
        min_len = float("inf")

        for i in range(len(s)):
            if (len(s) - i) < len(t):
                break
            remaining = len(t)
            if remaining == 1 and s[i] in needed:
                res = s[i]
                return res
            cache = {}
            if s[i] in needed:
                if needed[s[i]] > cache.get(s[i], 0):
                    remaining -= 1
                cache[s[i]] = 1 + cache.get(s[i], 0)
                for j in range(i+1, len(s)):
                    if s[j] in needed and needed[s[j]] > cache.get(s[j], 0):
                        cache[s[j]] = 1
                        remaining -= 1
                        if remaining == 0:
                            if(j - i + 1) < min_len:
                                min_len = j - i + 1
                                res = s[i:j+1]
                            break
        return res