class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node 

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __iter__(self):
        ref = self.head
        while(ref.next != None):
            yield(ref.val) 
            ref = ref.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node 
            self.tail = node
            new_node = Node(node.val)
            return 
        last = self.tail
        last.set_next(node)

    def add_to_head(self, node):
        if self.head is None:
            self.tail = node    
        node.set_next(self.head)
        self.head = node


class LLQueue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __iter__(self):
        ref = self.head
        while(ref.next != None):
            yield(ref.val) 
            ref = ref.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node 
            self.tail = node
            new_node = Node(node.val)
            return 
        last = self.tail
        last.set_next(node)

    def remove_from_head(self):
        if self.head is None:
            return None
        
        prev_head = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        del prev_head
