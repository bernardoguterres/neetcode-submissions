class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + str(len(s)) + "#" + s
        return ret



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            hashtag = s.find("#",i)
            length = int(s[i:hashtag])
            word = s[hashtag+1:hashtag+1+length]
            result.append(word)
            i = hashtag + 1 + length
        return result

