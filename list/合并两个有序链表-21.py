'''
merge-two-sorted-lists
'''

from list.node import ListNode


class Solution:
    # 时间复杂度O(m+n)
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1, node2 = l1, l2
        dummy = ListNode(0)
        prev = dummy
        while node1 and node2:
            if node1.val < node2.val:
                prev.next = node1
                prev = node1
                node1 = node1.next
            else:
                prev.next = node2
                prev = node2
                node2 = node2.next

        while node1:
            prev.next = node1
            prev = node1
            node1 = node1.next

        while node2:
            prev.next = node2
            prev = node2
            node2 = node2.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(2, ListNode(4))
    head2 = ListNode(4, ListNode(5, ListNode(6)))
    n = s.mergeTwoLists(head1, head2)
    while n:
        print(n)
        n = n.next
