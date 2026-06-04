class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for ch in s:
            if ch == '-':
                negative = True
            elif ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(NestedInteger())
            elif ch in ',]':
                if num:
                    val = int(num)
                    if negative:
                        val = -val
                    stack[-1].add(NestedInteger(val))
                    num = ""
                    negative = False

                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]