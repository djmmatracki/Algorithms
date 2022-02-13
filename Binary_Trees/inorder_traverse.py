from typing import Dict, Optional, List

TreeNode = Dict[int, List[int]]

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
        
def helper(self, root: Optional[TreeNode], visited: List[int]) -> None:
    if root:
        if root.left:
            self.helper(root.left, visited)
            
        visited.append(root.val)
        
        if root.right:
            self.helper(root.right, visited)