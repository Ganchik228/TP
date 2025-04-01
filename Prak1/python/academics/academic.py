from datetime import datetime

class Academic:
    def __init__(self, name: str, field: str, election_date: str):
        self.name = name
        self.field = field
        self.election_date = datetime.strptime(election_date, "%d.%m.%Y")
        
    def __str__(self):
        return f"{self.name} ({self.field}), избран: {self.election_date.strftime('%d.%m.%Y')}"

class CircularListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
        
    def append(self, value):
        new_node = CircularListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self._length += 1
        
    def sort_by_election_date(self):
        if not self.head or self.head == self.tail:
            return
            
        nodes = []
        current = self.head
        for _ in range(self._length):
            nodes.append(current)
            current = current.next
            
        nodes.sort(key=lambda node: node.value.election_date)
        
        self.head = nodes[0]
        self.tail = nodes[-1]
        for i in range(len(nodes)):
            nodes[i].next = nodes[(i+1) % len(nodes)]
            nodes[i].prev = nodes[(i-1) % len(nodes)]
            
    def __iter__(self):
        current = self.head
        for _ in range(self._length):
            yield current.value
            current = current.next
            
    def __str__(self):
        if not self.head:
            return "Empty CircularList"
            
        elements = []
        current = self.head
        for _ in range(self._length):
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) + " -> ..."
