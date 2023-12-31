class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = '{|}'.join(strs)
        return encoded 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = s.split('{|}')
        return decoded
        
