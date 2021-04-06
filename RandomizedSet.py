from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = []
        self.my_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.my_map:
            return False

        self.my_map[val] = len(self.my_list)
        self.my_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.my_map:
            return False

        last_element, index_to_put_in = self.my_list[-1], self.my_map[val]
        self.my_list[index_to_put_in], self.my_map[last_element] = last_element, index_to_put_in
        self.my_list.pop()
        del self.my_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.my_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
