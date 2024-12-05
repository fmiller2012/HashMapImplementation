class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def add(self, value):
        if self.head.next is None:
            self.head.next = Node(value)
            self.head.next.prev = self.head
        else:
            nodeToFind = self.head
            while nodeToFind.next is not None and nodeToFind.value != value:
                nodeToFind = nodeToFind.next
                if nodeToFind.next is None:
                    if nodeToFind.value != value:
                        nodeToFind.next = Node(value)
                        #print(nodeToFind.next.value)
                        nodeToFind.next.prev = nodeToFind
            
    def remove(self, value):
        nodeToFind = self.head
        while nodeToFind.next is not None and nodeToFind.value != value:
            nodeToFind = nodeToFind.next
            if nodeToFind.value == value:
                if nodeToFind.next is None:
                    nodeToFind.prev.next = None
                    nodeToFind.prev = None
                else:
                    nodeToFind.prev.next = nodeToFind.next
                    nodeToFind.next.prev = nodeToFind.prev
                    nodeToFind.next = None
                    nodeToFind.prev = None
                
    def get(self, value):
        nodeToFind = self.head
        while nodeToFind.next is not None and nodeToFind.value != value:
            nodeToFind = nodeToFind.next
            if nodeToFind.value == value:
                return True
        return False
    
    def __str__(self):
        current = self.head
        i = 0
        while current:
            #FIRST NODE IS ALWAYS SENTINEL NODE
            print(f"Node {i}: {current.value}")
            current = current.next
            i += 1
        return ""
            
class MyHashSet:
    
    #Python Set Data Structure Implementation
    def __init__(self):
        self.hashSet = set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        else:
            return False
    
    
    '''
    #Python List Direct Address Table Implementation
    def __init__(self):
        self.hashSet = [None] * ((10**6)+1)

    def add(self, key: int) -> None:
        self.hashSet[key] = key     

    def remove(self, key: int) -> None:
        if self.hashSet[key] == key:
            self.hashSet[key] = ""

    def contains(self, key: int) -> bool:
        if self.hashSet[key] == key:
            return True
        else:
            return False
    '''
    
    '''
    #Python List Hash Table Implementation without Collision Resolution
    def __init__(self):
        self.hashSet = [None] * ((10 ** 6) + 1)

    def add(self, key: int) -> None:
        hashFunction = key % ((10 ** 6) + 1)
        self.hashSet[hashFunction] = key

    def remove(self, key: int) -> None:
        hashFunction = key % ((10 ** 6) + 1)
        if self.hashSet[hashFunction] == key:
            self.hashSet[hashFunction] = None

    def contains(self, key: int) -> bool:
        hashFunction = key % ((10 ** 6) + 1)
        if self.hashSet[hashFunction] == key:
            return True
        else:
            return False
    '''
    
    '''
    #Python Linear Chaining Implementation with Duplicates
    def __init__(self):
        self.hashSet = [None] * 10
        
    def add(self, key: int) -> None:
        hashFunction = key % 10 
        if isinstance(self.hashSet[hashFunction], LinkedList):
            self.hashSet[hashFunction].add(key)
            print("old add")
        else:
            print("newly created add")
            self.hashSet[hashFunction] = LinkedList()
            self.hashSet[hashFunction].add(key)
            
    def remove(self, key: int) -> None:
        hashFunction = key % 10
        if isinstance(self.hashSet[hashFunction], LinkedList):
            self.hashSet[hashFunction].remove(key)
            
    def contains(self, key: int) -> bool:
        hashFunction = key % 10
        if isinstance(self.hashSet[hashFunction], LinkedList):
            print("entered into if contains")
            return self.hashSet[hashFunction].get(key)
        else:
            print("entered into else contains")
            return False
    '''  
    
    ''' 
    #Python Linear Chaining Implementation without Duplicates
    def __init__(self):
        self.hashSet = [None] * ((10 ** 6) + 3)
        
    def add(self, key: int) -> None:
        hashFunction = key % ((10 ** 6) + 3) 
        if isinstance(self.hashSet[hashFunction], LinkedList):
            self.hashSet[hashFunction].add(key)
        else:
            self.hashSet[hashFunction] = LinkedList()
            self.hashSet[hashFunction].add(key)
            
    def remove(self, key: int) -> None:
        hashFunction = key % ((10 ** 6) + 3)
        if isinstance(self.hashSet[hashFunction], LinkedList):
            self.hashSet[hashFunction].remove(key)
            
    def contains(self, key: int) -> bool:
        hashFunction = key % ((10 ** 6) + 3)
        if isinstance(self.hashSet[hashFunction], LinkedList):
            return self.hashSet[hashFunction].get(key)
        else:
            return False
    '''
    def __str__(self):
        j = 1
        for i in self.hashSet:
            print(f"node {j}: {i} ")
            j += 1
        return ""
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#DOUBLY LINKED LIST IMPLEMENTATION
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
print("DOUBLY LINKED LIST IMPLEMENTATION:\n", ll)
ll.remove(3)
print("DOUBLY LINKED LIST IMPLEMENTATION:\n", ll)

#BUILT-IN PYTHON HASHSET IMPLEMENTATION
mhs = MyHashSet()
mhs.add(1)
mhs.add(2)
mhs.add(3)
mhs.add(4)
mhs.add(5)
print("HASH SET IMPLEMENTATION:\n", mhs)
mhs.remove(3)
print("HASH SET IMPLEMENTATION:\n", mhs)
print(mhs.contains(10))
print(mhs.contains(1))