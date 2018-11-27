from list.node import ListNode


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        n = head
        while n:
            s.append(n.val)
            n = n.next

        n = head
        while n:
            if s.pop() != n.val:
                return False
            n = n.next
        return True


if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(1)))
    print(Solution().isPalindrome(head))
