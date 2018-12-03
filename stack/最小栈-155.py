class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minarr = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)
        # bug　逻辑冲突
        if not self.minarr:
            self.minarr.append(x)
        elif x <= self.getMin():
            self.minarr.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.arr:
            return
        val = self.arr.pop()
        # print(val,self.getMin())
        if val == self.getMin():
            self.minarr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[len(self.arr) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minarr[len(self.minarr) - 1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.minarr)
    s.pop()
    s.pop()
    s.pop()
    print(s.minarr)
    s.push(1)
    print(s.minarr)
