class BinaryTree:
    class Node:
        def __init__(self, key, left_node=None, right_node=None):
            self.key = key
            self.left_node = left_node
            self.right_node = right_node
    
    def __init__(self):
        self.root = None

    def add(self, key):
        def _add(key, node):
            if node is None:
                return BinaryTree.Node(key)
            if key <= node.key:
                node.left_node = _add(key, node.left_node)
            else:
                node.right_node = _add(key, node.right_node)
            return node
        
        self.root = _add(key, self.root)

def tree_sort(sequence):
    tree = BinaryTree()
    for element in sequence:
        tree.add(element)
    insert_index = 0
    
    def tree_visit(node):
        nonlocal insert_index
        if node is None:
            return
        tree_visit(node.left_node)
        sequence[insert_index] = node.key
        insert_index += 1
        tree_visit(node.right_node)
    
    tree_visit(tree.root)
    return sequence

if __name__ == "__main__":
    '''
    numbers = [1,2,4,2,5,0,5,7,3,7,8]
    tree_sort(numbers)
    print(numbers)
    tests = [
        "123456", "12345", "123456789", "password", "iloveyou",
        "princess", "1234567", "rockyou", "12345678", "abc123",
        "nicole", "daniel", "babygirl", "monkey", "lovely",
        "jessica", "654321", "michael", "ashley", "qwerty",
        "111111", "iloveu", "000000", "michelle", "tigger",
        "sunshine", "chocolate"
    ]
    tree_sort(tests)
    print("\nSorted passwords:")
    for test in tests:
        print(test)
    '''
    with open('sort_benchmark.txt', "r") as file:
        lines = file.readlines()
        data = [line.strip() for line in lines]
    tree_sort(data)
    with open('sorted_binary_tree_data.txt', 'w') as file:
        for item in data:
            file.write(f"{item}\n")
