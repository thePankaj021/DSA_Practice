class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")

        result = []

        for word in words:
            s = set(word)

            if s <= row1 or s <= row2 or s <= row3:
                result.append(word)

        return result