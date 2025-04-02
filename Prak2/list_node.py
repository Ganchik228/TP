class ListNode:
    def __init__(self, value, next_node=None):
        if next_node is not None and not isinstance(next_node, ListNode):
            raise TypeError("next must be ListNode or None")
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"({self.value}) -> {self.next}" if self.next else f"({self.value}) -> None"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.value == other.value and self.next == other.next
