class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            string = s[i]
            r = i + 1
            while r < len(s):
                if s[r] not in string:
                    string += s[r]
                    r += 1
                else:
                    break
            longest = max(longest, len(string))
        return longest