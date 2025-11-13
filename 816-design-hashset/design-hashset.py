class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.head = [None] * self.size

    def make_or_find_key(self,key):
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key): return
        idx = self.make_or_find_key(key)
        self.head[idx] = ListNode(key,self.head[idx])

    def remove(self, key: int) -> None:   
        idx = self.make_or_find_key(key)
        linkList = self.head[idx]

        if linkList is None:
            return

        if  linkList.val == key:
            self.head[idx] = linkList.next
            return
        prev = linkList
        while prev and prev.next:
            if prev.next.val == key:
                prev.next =  prev.next.next
                return
            prev = prev.next
            
    
    def contains(self, key: int) -> bool:
        idx = self.make_or_find_key(key)
        linkList = self.head[idx]

        while linkList:
            if linkList.val == key:
                return True
            linkList = linkList.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)