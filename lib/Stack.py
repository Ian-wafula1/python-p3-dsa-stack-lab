class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return not len(self.items)

    def push(self, item):
        if self.size() >= self.limit:
            return
        self.items.append(item)
        return self

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        try:
            return self.size() - self.items.index(target) - 1
        except:
            return -1
