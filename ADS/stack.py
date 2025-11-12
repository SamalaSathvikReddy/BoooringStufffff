class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) 

    def size(self):
        return len(self.items) 
    
    def peek(self):
        if(len(self.items) == 0):
            return None
        return self.items[-1]

    def pop(self):
        if(len(self.items) == 0):
            return None
        item = self.items[-1]
        del self.items[-1]
        return item


def is_balanced(input_str):
    st = Stack()
    for i in input_str:
        if i == '(':
            st.push('(')
        else:
            if st.peek() == '(':
                st.pop()
            else:
                return False
    return (st.size() == 0)

print(is_balanced('(()))'))
print(is_balanced('(()(()))'))
