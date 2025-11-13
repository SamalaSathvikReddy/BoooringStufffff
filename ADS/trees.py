class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            new_node = BSTNode(val)
            return 
        
        if self.val == val:
            # No duplicates
            return
    
        if self.val > val:
            if self.left is None:
                self.left = BSTNode(val) 
            else:
                insert(self.left, val)

        if self.val < val:
            if self.right is None:
                self.right = BSTNode(val) 
            else:
                insert(self.right, val)


    def get_min(self):
        if self.left is None:
            return self.val
        get_min(self.left)

    def get_max(self):
        if self.right is None:
            return self.val
        get_max(self.right)
    
    """
    def delete(self, val):
        if self.val is None:
            return None

        if self.val > val:
            if self.left is not None:
                delete(self.left, val)
            return self.val

        if self.val < val:
            if self.right is not None:
                delete(self.right, val)
            return self.val

        if self.val == val:
            if self.right is None:
                return self.left

            if self.left is None:
                return self.right

    """

    def preorder(self, visited):
        visited.append(self.val)
        preorder(self.left, visited)
        preorder(self.right, visited)
        return visited

    def postorder(self, visited):
        postorder(self.left, visited)
        postorder(self.right, visited)
        visited.append(self.val)
        return visited


    def inorder(self, visited):
        inorder(self.left, visited)
        visited.append(self.val)
        inorder(self.right, visited)
        return visited 

    def exists(self, val):
        if self.val == val:
            return True 
        if self.val > val:
            exists(self.left, val)
        if self.val < val:
            exists(self.right, val)
    
    def height(self):
        if self.val is None:
            return 0
        return max(height(self.left), height(self.right)) + 1
    
