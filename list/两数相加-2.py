'''
add-two-numbers
出现一个bug　忽略了加法的进位
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = l1, l2
        add = 0
        dummy = ListNode(0)
        prev = dummy
        while n1 and n2:
            val = n1.val + n2.val + add
            node = ListNode(val % 10)
            add = val // 10
            prev.next = node
            prev = node
            n1 = n1.next
            n2 = n2.next

        while n1:
            val = add + n1.val
            node = ListNode(val % 10)
            add = val // 10
            prev.next = node
            prev = node
            n1 = n1.next

        while n2:
            val = add + n2.val
            node = ListNode(val % 10)
            add = val // 10
            prev.next = node
            prev = node
            n2 = n2.next

        # 边界条件未考虑清楚
        if add:
            prev.next = ListNode(add)

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(2, ListNode(4))
    head2 = ListNode(5, ListNode(6, ListNode(4)))
    n = s.addTwoNumbers(head1, head2)
    while n:
        print(n)
        n = n.next
