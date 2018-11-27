'''
remove-nth-node-from-end-of-list
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    # 解法1 O(n)　利用了数学的性质
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        while n > 0:
            node1 = node1.next
            n -= 1

        node2 = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while node1:
            prev = node2
            node2 = node2.next
            node1 = node1.next

        prev.next = node2.next
        return dummy.next

    # 解法2 时间复杂度O(2n-2)
    def removeNthFromEnd2(self, head, n):
        node1 = head
        lens = 0
        while node1:
            lens += 1
            node1 = node1.next

        s = lens - n
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        node1 = head
        while s > 0:
            prev = node1
            node1 = node1.next
            s -= 1
        prev.next = node1.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head2 = ListNode(5, ListNode(6, ListNode(4)))
    n = s.removeNthFromEnd2(head2, 1)
    while n:
        print(n)
        n = n.next
