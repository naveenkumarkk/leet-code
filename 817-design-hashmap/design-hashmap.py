class LinkedList:
    def __init__(self,key,value,next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.head = [None] * self.size
    
    def make_index(self,key):
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        idx = self.make_index(key)
        if not self.head[idx]:
            self.head[idx] = LinkedList(key,value)
            return
        current = self.head[idx]

        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:break
            current = current.next
        current.next = LinkedList(key,value
        )
    def get(self, key: int) -> int:
        idx = self.make_index(key)
        if not self.head[idx]:
            return -1
        current = self.head[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1


    def remove(self, key: int) -> None:
        idx = self.make_index(key)
        if not self.head[idx]:
            return
        current = self.head[idx]
        if current.key == key:
            self.head[idx] = current.next
            return 
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)