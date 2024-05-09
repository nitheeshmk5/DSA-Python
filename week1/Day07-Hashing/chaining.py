# Chaining

class MyHash():
    def __init__(self,b):
        self.BUCKET = b
        self.table = [[] for _ in range(b)]

    def insert(self,value):
        i = value % self.BUCKET
        self.table[i].append(value)

    def delete(self,value):
        i = value % self.BUCKET
        if value in self.table[i]:
            self.table[i].remove(value)
    
    def search(self,value):
        i = value % self.BUCKET
        return value in self.table[i]  # True / false


h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.delete(56)
print(h.search(56))
h.delete(56)
print(h.table)