import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        ans = node.val
        count = 1

        while node:
            if random.randint(1, count) == 1:
                ans = node.val

            node = node.next
            count += 1

        return ans