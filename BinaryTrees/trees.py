
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
def create_test_tree_chars() -> Node:
    a = Node('a') # Root
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def create_test_tree_ints() -> Node:
    a = Node(3) # Root
    b = Node(9)
    c = Node(12)
    d = Node(0)
    e = Node(4)
    f = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a