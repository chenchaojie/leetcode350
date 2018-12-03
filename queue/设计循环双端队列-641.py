class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.length = k + 1
        self.head = 0
        self.tail = 0
        self.arr = []
        i = 0
        while i < self.length:
            self.arr.append(0)
            i += 1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.length) % self.length
        self.arr[self.head] = value
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.length
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        ret = self.arr[self.head]
        self.head = (self.head + 1) % self.length
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        ret = self.arr[self.tail - 1 + self.length % self.length]
        self.tail = (self.tail - 1 + self.length) % self.length
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.tail - 1 + self.length) % self.length]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.head == self.tail:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if (self.tail + 1) % self.length == self.head:
            return True
        return False


if __name__ == "__main__":
    c = MyCircularDeque(3)
    c.insertFront(3)
    c.deleteLast()
    print(c.head, c.tail)
    print(c.isEmpty())
