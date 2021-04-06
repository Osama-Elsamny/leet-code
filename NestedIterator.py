class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatten_list = []
        for item in nestedList:
            self._dfs(item)
        self.counter = 0

    def _dfs(self, item):
        my_stack = item
        while my_stack:
            elem = my_stack.pop()
            if elem.isInteger():
                self.flatten_list.append(elem)
            else:
                my_stack.extend(reversed(elem.getList()))

    def next(self):
        """
        :rtype: int
        """
        elem = self.flatten_list[self.counter]
        self.counter += 1
        return elem

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.flatten_list) > self.counter
