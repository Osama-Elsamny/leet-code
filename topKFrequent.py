import heapq
import collections


class Solution(object):
    def topKFrequent(self, words, k):
        # build word count hash
        hashed = collections.Counter(words)
        heap = [(-hashed[word], word) for word in hashed]

        # turn into tuple for heap comparison predicate
        # based on count
        heapq.heapify(heap)

        # get top k words
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def topKFrequentNum(self, nums, k):
        # Count the recurrence of numbers
        hashed = collections.Counter(nums)
        heap = [(-hashed[num], num) for num in hashed]

        # Convert list to heap to then return the maximum
        # recurrence
        heapq.heapify(heap)

        # get top k words
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
