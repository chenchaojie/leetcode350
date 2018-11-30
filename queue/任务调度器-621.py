import collections


class Solution:
    # x 错误解答　考虑问题简单了
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        for v in tasks:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        lens = len(tasks)
        q = []
        while lens > 0:
            j = n
            for k, v in d.items():
                if v > 0:
                    d[k] -= 1
                    q.append(k)
                    lens -= 1
                    j -= 1

            while j >= 0 and lens > 0:
                q.append('#')
                j -= 1
        print(q)
        return len(q)

    # 　贪心算法来解决
    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        for v in tasks:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        max = 0
        for v in d.values():
            if v > max:
                max = v

        max_count = 0
        for v in d.values():
            if max == v:
                max_count += 1
        # max-1去除最后个
        return (n + 1) * (max - 1) + max_count

    def leastInterval3(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        d = collections.OrderedDict()
        for v in tasks:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        s = []
        lens = len(tasks)

        while lens > 0:
            j = n
            for task, num in d.items():

                if j < 0:
                    break
                if num > 0:
                    s.append(task)
                    d[task] -= 1
                    lens -= 1
                    j -= 1

            while j >= 0 and lens > 0:
                s.append('#')
                j -= 1
        return len(s)


if __name__ == "__main__":
    print(Solution().leastInterval3(['A', 'A', 'A', 'B', 'B','B'], 2))
