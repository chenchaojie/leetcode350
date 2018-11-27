from list.node import ListNode


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, prev = head, None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    n = Solution().reverseList(head)
    while n:
        print(n)
        n = n.next
