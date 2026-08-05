class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        return list(seen.values())