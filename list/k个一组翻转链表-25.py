from list.node import ListNode


class Solution:
    # 解法1 应该还有更优的解法 O(2n)
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        prev, node = dummy, head

        while node:
            src, dst = node, node
            i = 1
            while i < k and dst:
                dst = dst.next
                i += 1

            # print(i,k)
            if not dst:
                break

            next = dst.next
            sprev, s = None, src
            while s and id(s) != id(next):
                snext = s.next
                s.next = sprev
                sprev = s
                s = snext
            prev.next = dst
            src.next = next
            prev = src
            node = next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4,ListNode(5)))))
    n = s.reverseKGroup(head1, 3)
    while n:
        print(n)
        n = n.next
