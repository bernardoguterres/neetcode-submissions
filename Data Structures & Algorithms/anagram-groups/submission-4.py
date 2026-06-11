class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sw = "".join(sorted(s))
            if sw in seen:
                seen[sw] += [s]
            else:
                seen[sw] = [s]
        return list(seen.values())