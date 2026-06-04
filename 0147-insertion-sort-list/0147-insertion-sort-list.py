class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)

        while head:
            prev = dummy

            while prev.next and prev.next.val < head.val:
                prev = prev.next

            nxt = head.next
            head.next = prev.next
            prev.next = head
            head = nxt

        return dummy.next