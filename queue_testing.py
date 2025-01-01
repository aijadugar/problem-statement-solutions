from collections import deque


class MyStack(object):

    def __init__(self):
        self.qu1 = deque()
        self.qu2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.qu1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.qu2:
            while self.qu1:
                self.qu2.append(self.qu1.popleft())
        return self.qu2.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.qu2:
            while self.qu1:
                self.qu2.append(self.qu1.popleft())
        return self.qu2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.qu1 or self.qu2:
            return False
        else:
            return True
        


obj = MyStack()
obj.push(12)
obj.push(13)
obj.push(14)
obj.push(15)

print(obj.pop())
print(obj.pop())

print(obj.top())

print(obj.empty())
