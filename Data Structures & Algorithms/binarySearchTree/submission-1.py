from typing import Optional, List, Dict

class TreeNode:

    def __init__(self, key:int , val:int):
        self.key = key
        self.val = val
        self.left : Optional[TreeNode] = None
        self.right : Optional[TreeNode] = None

    def __str__(self):
        return f'{self.key}: {self.val}'

    def get_key(self):
        return self.key

    def get_val(self):
        return self.val

class TreeMap:
    
    def __init__(self):
        self.root : Optional[TreeNode] = None
        #self.size = 0

    def __str__(self):
        return f'{self.getInorderAll()}'

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(key,val)
            return
        curr = self.root
        while True:
            if key == curr.key:
                curr.val = val
                return
            if key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key,val)
                    return
                curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key,val)
                    return
                curr = curr.left  


    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        curr = self.root
        while True:
            if key == curr.key:
                return curr.val
            if key > curr.key:
                if curr.right is None:
                    return -1
                curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    return -1
                curr = curr.left         


    def getMin(self) -> int:
        if self.root is None:
            return -1
        curr = self.root
        while True:
            if curr.left is None:
                return curr.val
            else:
                curr = curr.left

    def getMax(self) -> int:
        if self.root is None:
            return -1
        curr = self.root
        while True:
            if curr.right is None:
                return curr.val
            else:
                curr = curr.right

    def remove(self, key: int) -> None:
        def _min_node(node: TreeNode) -> TreeNode:
            curr = node
            while curr.left is not None:
                curr = curr.left
            return curr

        def  _remove(node:Optional[TreeNode], key:int) -> Optional[TreeNode]:

            if node is None:
                return

            if key > node.key:
                node.right =_remove(node.right,key)
            elif key < node.key:
                node.left = _remove(node.left,key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    succesor = _min_node(node.right)
                    node.key = succesor.key
                    node.val = succesor.val
                    node.right = _remove(node.right, succesor.key)         
            return node
        self.root = _remove(self.root,key)

    def getInorderKeys(self) -> List[int]:
        result : List[int] = []
        
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            result.append(node.key)
            inorder(node.right)
        
        inorder(self.root)
        return result

    def getInorderAll(self) -> Dict[int,int]:
        result : Dict[int:int] = {}
        
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            result[node.key] = node.val
            inorder(node.right)
        
        inorder(self.root)
        return result