from typing import Type
from collections import deque
from trees import Node, create_test_tree_chars


def dbs_rec(root: Type[Node]):
    """
        Depth first serach recursively.
        Left to right search.
    """
    if not isinstance(root, Node):
        return []

    if root.right is None and root.left is None:
        return [root.val]

    if root.left is None:
        return [root.val] + dbs_rec(root.right)

    if root.right is None:
        return [root.val] + dbs_rec(root.left)

    left = dbs_rec(root.left)
    right = dbs_rec(root.right)
    return [root.val] + left + right

def dbs_iter(root: Type[Node]):
    """
        Depth first serach iter.
        Right to left search.
    """
    if not isinstance(root, Node):
        return []

    stack = deque([root])
    result = []

    while len(stack) != 0:
        current = stack.pop()
        result.append(current.val)
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)
    return result

def bbs_iter(root: Type[Node]):
    """
        Breath first serach iter.
    """
    if not isinstance(root, Node):
        return []

    queue = deque([root])
    result = []

    while len(queue) != 0:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
        
    return result

a = create_test_tree_chars()

print(dbs_iter(a))
print(dbs_rec(a))
print(bbs_iter(a))
