import random
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        last_value = self.list[-1]

        self.list[idx] = last_value
        self.map[last_value] = idx

        self.list.pop()
        del self.map[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()