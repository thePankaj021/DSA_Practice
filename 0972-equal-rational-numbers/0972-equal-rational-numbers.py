from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(x):
            if '(' not in x:
                return Fraction(x)

            nonrep, rep = x.split('(')
            rep = rep[:-1]

            if '.' in nonrep:
                integer, frac = nonrep.split('.')
            else:
                integer, frac = nonrep, ""

            base = Fraction(int(integer), 1)

            if frac:
                base += Fraction(int(frac), 10 ** len(frac))

            if rep:
                numerator = int(rep)
                denominator = (10 ** len(rep) - 1) * (10 ** len(frac))
                base += Fraction(numerator, denominator)

            return base

        return convert(s) == convert(t)