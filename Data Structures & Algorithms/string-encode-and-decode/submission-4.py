class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0, len(strs)):
            encoded += strs[i]
            encoded += "."
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded = []
        decoded = s.split(".")
        decoded = decoded[:-1]
        return decoded