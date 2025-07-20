
class Stack:
    def __init__(self, items=None, limit=100):
        # Safely initialize items list and capacity limit
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        # True when no items are in the stack
        return len(self.items) == 0

    def push(self, item):
        # Only append if under the capacity
        if not self.full():
            self.items.append(item)

    def pop(self):
        # Return None on empty, otherwise pop the top
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        # Return None on empty, otherwise the top element
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        # Number of items in the stack
        return len(self.items)

    def full(self):
        # True when capacity reached or exceeded
        return self.size() >= self.limit

    def search(self, target):
        """
        Return distance from the top (0-based) if found,
        or -1 if not present.
        """
        for distance, item in enumerate(reversed(self.items)):
            if item == target:
                return distance
        return -1