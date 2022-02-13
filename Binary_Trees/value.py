from typing import Type
from collections import deque
from trees import Node, create_test_tree_chars



def is_val_rec(root: Type[Node], val: str) -> bool:
    """Is a value in a binary tree. Recursivly"""
    if root is None:
        return False

    if root.val == val:
        return True
        
    return is_val_rec(root.left, val) or is_val_rec(root.right, val) 


def is_val_iter(root: Type[Node], val: str) -> bool:
    """
        Is a value in a binary tree.
        Iterably.
    """
    queue = deque([root])

    while len(queue) != 0:
        current = queue.popleft()
        if current.val == val:
            return True
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    return False

a = create_test_tree_chars()

print(is_val_rec(a, '0'))
print(is_val_iter(a, '0'))