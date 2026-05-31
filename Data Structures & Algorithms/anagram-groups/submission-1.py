class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            sw = "".join(sorted(w))
            if sw not in seen:
                seen[sw] = [w]
            else:
                seen[sw] += [w]
        return list(seen.values())