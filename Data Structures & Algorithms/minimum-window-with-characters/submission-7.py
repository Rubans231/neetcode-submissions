from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""
