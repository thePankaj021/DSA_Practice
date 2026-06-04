from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [Counter()]
        i = 0

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1

            elif formula[i] == ')':
                i += 1
                start = i

                while i < n and formula[i].isdigit():
                    i += 1

                mult = int(formula[start:i] or "1")
                top = stack.pop()

                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mult

            else:
                start = i
                i += 1

                while i < n and formula[i].islower():
                    i += 1

                atom = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1

                cnt = int(formula[start:i] or "1")
                stack[-1][atom] += cnt

        result = []

        for atom in sorted(stack[-1]):
            result.append(atom)
            if stack[-1][atom] > 1:
                result.append(str(stack[-1][atom]))

        return "".join(result)