class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            for c in s:
                res.append(chr(ord(c) + 1))
            res.append(chr(0))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        word = []
        for c in s:
            if ord(c) == 0:
                res.append("".join(word))
                word = []
                continue
            word.append(chr(ord(c) -1))
        return res
            
            

