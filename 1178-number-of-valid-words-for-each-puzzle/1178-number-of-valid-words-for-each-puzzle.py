from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        freq = Counter()

        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))

            if mask.bit_count() <= 7:
                freq[mask] += 1

        ans = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))

            mask = 0
            for ch in puzzle[1:]:
                mask |= 1 << (ord(ch) - ord('a'))

            sub = mask
            total = 0

            while True:
                total += freq[sub | first]

                if sub == 0:
                    break

                sub = (sub - 1) & mask

            ans.append(total)

        return ans