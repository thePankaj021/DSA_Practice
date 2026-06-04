from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))

        c1 = Counter(secret)
        c2 = Counter(guess)

        cows = sum((c1 & c2).values()) - bulls

        return f"{bulls}A{cows}B"