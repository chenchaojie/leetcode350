class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enstack = []
        self.destack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.enstack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return -1

        if not self.destack:
            while self.enstack:
                self.destack.append(self.enstack.pop())

        return self.destack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return -1
        if not self.destack:
            while self.enstack:
                self.destack.append(self.enstack.pop())
        return self.destack[len(self.destack) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.enstack and not self.destack:
            return True
        return False


if __name__ == "__main__":
   q = MyQueue()
   q.push(1)
   q.push(2)
   print(q.peek())
   print(q.pop())
   print(q.empty())
