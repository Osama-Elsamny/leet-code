class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [0] * 300
        self.my_list = [0] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        if self.my_list[index] != timestamp:
            self.my_list[index] = timestamp
            self.counter[index] = 1
        else:
            self.counter[index] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        result = 0
        for i in range(300):
            if timestamp - self.my_list[i] < 300 and self.counter[i] > 0:
                result += self.counter[i]
        return result

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
