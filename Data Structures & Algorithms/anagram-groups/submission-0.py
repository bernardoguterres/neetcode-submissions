class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sorted_w = "".join(sorted(s))
            if sorted_w not in seen:
                seen[sorted_w] = [s]
            else:
                seen[sorted_w] += [s]
        return list(seen.values())