class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '[]'
        return chr(257).join(strs)
        


    def decode(self, s: str) -> List[str]:
        if s == '[]':
            return []
        return s.split(chr(257))
