import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_history = []

    def push(self, x: int) -> None:
        lenth = len(self.min_history)
        if lenth == 0:
            self.min_history.append(x)
        elif self.min_history[lenth - 1] >= x:
            self.min_history.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) != 0:
            elem = self.stack.pop()
            if elem == self.min_history[len(self.min_history) - 1]:
                self.min_history.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        print('self.min_history: {}'.format(self.min_history))
        lenth = len(self.min_history)
        if lenth == 0:
            return None
        else:
            return self.min_history[lenth - 1]


if __name__ == "__main__":
    # obj = MinStack()
    # obj.push(5)
    # obj.pop()
    # obj.push(5)
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # print('param_3: {}, param_4: {}'.format(param_3, param_4))
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    print('minStack.getMin(): {} --> Returns 0.'.format(minStack.getMin()))
    minStack.pop()
    print('minStack.getMin(): {} --> Returns 0.'.format(minStack.getMin()))
    minStack.pop()
    print('minStack.getMin(): {} --> Returns 0.'.format(minStack.getMin()))
    minStack.pop()
    print('minStack.getMin(): {} --> Returns 2.'.format(minStack.getMin()))
