from list_node import ListNode

class MyList:
    def __init__(self, head=None):
        if head is not None:
            if isinstance(head, ListNode):
                self.head = head
            else:
                self.head = ListNode(head)
        else:
            self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "(" + ") -> (".join(values) + ") -> None" if values else "None"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, MyList):
            return False
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.value != current2.value:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def clear(self):
        self.head = None

    def copy(self):
        new_list = MyList()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list

    def remove(self, value):
        if not self.head:
            raise ValueError("Value not found in list")
            
        if self.head.value == value:
            self.head = self.head.next
            return
            
        prev = self.head
        current = self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError("Value not found in list")

    def pop(self, index=-1):
        if not self.head:
            raise IndexError("pop from empty list")
            
        length = len(self)
        if index < 0:
            index += length
        if index < 0 or index >= length:
            raise IndexError("pop index out of range")
            
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            return value
            
        prev = None
        current = self.head
        for _ in range(index):
            prev = current
            current = current.next
            
        prev.next = current.next
        return current.value

    def extend(self, iterable):
        if not isinstance(iterable, MyList):
            raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
            
        current = iterable.head
        while current:
            self.append(current.value)
            current = current.next

    def insert(self, index, value):
        if not isinstance(index, int):
            raise IndexError("insert index out of range")
            
        length = len(self)
        if index < 0:
            index += length
        if index < 0:
            raise IndexError("insert index out of range")
            
        if not self.head or index >= length:
            self.append(value)
            return
            
        if index == 0:
            self.head = ListNode(value, self.head)
            return
            
        prev = None
        current = self.head
        for _ in range(index):
            prev = current
            current = current.next
            
        prev.next = ListNode(value, current)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def index(self, value):
        current = self.head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        raise ValueError(f"{value} not in list")

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def sort(self):
        if not self.head or not self.head.next:
            return
            
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next
