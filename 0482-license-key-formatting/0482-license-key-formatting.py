class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()
        
        # First group can have 1 to k characters
        first = len(s) % k
        parts = []
        
        if first:
            parts.append(s[:first])
        
        for i in range(first, len(s), k):
            parts.append(s[i:i+k])
        
        return "-".join(parts)