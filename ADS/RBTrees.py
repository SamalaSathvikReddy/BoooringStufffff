class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.red = True

        current = self.root
        
        # finding the node
        while current is not None:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
         
        new_node.parent = parent 
        
        # linking the node
        if parent is None:
            self.root = new_node
        elif parent.val > new_node.val:
            parent.left = new_node
        else:
            parent.right = new_node

    def fix_insert(self, new_node):
        pass
    
    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        
        """
        self.root = pivot_parent.left
        pivot_parent.right = pivot_parent.left.left
        pivot_parent.left.left = None
        """
        if pivot_parent.right is None:
            return 
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left.parent is not None:
            pivot.left.parent = pivot_parent
        
        pivot.parent = pivot_parent.parent

        if self.root == pivot_parent:
            self.root = pivot
        
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot

        else:
            pivot_parent.parent.right = pivot


    def rotate_right(self, pivot_parent):
         if pivot_parent.left is None:
            return 
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right.parent is not None:
            pivot.right.parent = pivot_parent
        
        pivot.parent = pivot_parent.parent

        if self.root == pivot_parent:
            self.root = pivot
        
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot

        else:
            pivot_parent.parent.left = pivot



