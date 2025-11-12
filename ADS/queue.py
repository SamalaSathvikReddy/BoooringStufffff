class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if(len(self.items) == 0):
            return None
        item = self.items[0]
        del self.items[0]
        return item

    def peek(self):
        if(len(self.items) == 0):
            return None
        return self.items[0]

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item
    
    def size(self):
        return (len(self.items)) 

def matchmake(queue, user):
    if user[1] == 'join':
        queue.push(user)

    if user[1] == 'leave':
        queue.search_and_remove(user) 

    if queue.size() >= 4:
        player_1 = queue.pop()
        player_2 = queue.pop()
        return f"{player_1[0]} matched {player_2[0]}"
    
    return "No match found"
