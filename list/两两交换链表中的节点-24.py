from list.node import ListNode


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev, node = dummy, head

        while node and node.next:
            next = node.next
            node.next = next.next
            prev.next = next
            next.next = node
            prev = node
            node = node.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    n = s.swapPairs(head1)
    while n:
        print(n)
        n = n.next
