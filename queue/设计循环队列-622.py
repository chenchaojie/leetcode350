class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head = 0
        self.tail = 0
        self.arr = []
        self.length = k+1
        i = 0
        while i < k + 1:
            self.arr.append(0)
            i += 1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            print(self.tail)
            return False

        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.length
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.arr[self.head] = 0
        self.head = (self.head + 1) % self.length

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.arr[self.head]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.arr[(self.tail + self.length - 1) % self.length]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == self.tail:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.head == (self.tail + 1) % self.length:
            return True
        return False


if __name__ == "__main__":
    c = MyCircularQueue(3)
    print(c.enQueue(1))
    print(c.enQueue(2))
    print(c.enQueue(3))
    print(c.enQueue(4))
    print(c.Rear())
    print(c.isFull())
    print(c.deQueue())
    print(c.enQueue(4))
    print(c.Rear())
