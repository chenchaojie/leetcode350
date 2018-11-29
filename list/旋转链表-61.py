from list.node import ListNode


class Solution:

    def rotateRight(self,head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 边界条件未考虑
        if not head:
            return head
        n = head
        lens = 0
        while n:
            lens += 1
            n = n.next

        duumy = ListNode(0)
        duumy.next = head
        e = lens - (k % lens)
        if k % lens:
            s = 1
            n = head
            while s < e:
                n = n.next
                s += 1

            duumy.next = n.next
            end = n.next
            while end.next:
                end = end.next
            end.next = head
            n.next = None

        return duumy.next

    # 通过循环队列来解决问题
    def rotateRight2(self, head, k):
        """
               :type head: ListNode
               :type k: int
               :rtype: ListNode
               """
        if not head:
            return head
        lens = 0
        n, prev = head, None
        while n:
            lens += 1
            prev = n
            n = n.next

        if k % lens:
            prev.next = head
            s, e = 1, lens - (k % lens)
            node = head
            while s < e:
                node = node.next
                s += 1

            ret = node.next
            node.next = None
            return ret

        return head

if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = Solution().rotateRight2(head1, 4)
    while n:
        print(n)
        n = n.next
