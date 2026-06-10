class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in seen:
                seen[sortedword] += [word]
            else:
                seen[sortedword] = [word]
        return list(seen.values())