class MedianFinder:
    def __init__(self):
        self.data = []
    
    def addNum(self, num):
        self.data.append(num)
    
    def findMedian(self):
        sum = 0
        for i in self.data:
            sum += i
        return sum / len(self.data)
            
medianFinder = MedianFinder()
medianFinder.addNum(1); #// arr = [1]
medianFinder.addNum(2); #// arr = [1, 2]
medianFinder.findMedian(); #// return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3); #// arr[1, 2, 3]
medianFinder.findMedian(); #// return 2.0
