# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str((self.start, self.end))


class Solution:
    # timeout
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        lens = len(intervals)
        i = 1
        while i < lens:
            j = i - 1
            value = intervals[i]
            while j >= 0 and intervals[j].start > value.start:
                intervals[j + 1] = intervals[j]
                j -= 1

            intervals[j + 1] = value
            i += 1

        ret = []
        interval = intervals[0]
        i = 1
        while i < lens:
            if interval.end >= intervals[i].start:
                interval = Interval(interval.start, max(interval.end, intervals[i].end))
            else:
                ret.append(interval)
                interval = intervals[i]

            i += 1
        ret.append(interval)

        return ret


if __name__ == "__main__":
    ret = (Solution().merge([
        # Interval(0, 0),
        # Interval(15, 18),
        # Interval(1, 3),
        # Interval(8, 10),
        # Interval(2, 6),
        Interval(1, 4),
        Interval(4, 5),

    ]))
    for v in ret:
        print(v)
