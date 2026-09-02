class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        needed = {}
        for c in t:
            needed[c] = 1 + needed.get(c, 0)

        window = {}
        have, need = 0, len(needed)
        res, min_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in needed and window[char] == needed[char]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = [l, r]

                left_char = s[l]
                window[left_char] -= 1
                if left_char in needed and window[left_char] < needed[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if min_len != float("inf") else ""