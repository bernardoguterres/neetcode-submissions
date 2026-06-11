class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        delim = "#"
        for s in strs:
            length = str(len(s))
            result = result + length + delim + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j + 1 + length
        return result
