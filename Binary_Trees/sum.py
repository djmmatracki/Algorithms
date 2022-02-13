from typing import Type
from trees import Node, create_test_tree_ints
from collections import deque


def dbs_sum_rec(root: Type[Node]):
    """Find sum of elements is binary tree."""
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    if root.left is None:
        return  root.val + dbs_sum_rec(root.right)
    
    if root.right is None:
        return  root.val + dbs_sum_rec(root.left)

    left = dbs_sum_rec(root.left)
    right = dbs_sum_rec(root.right)
    return left + right + root.val

a = create_test_tree_ints()

print(dbs_sum_rec(a))
