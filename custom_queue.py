class Q:
    
    def __init__(self):
        self.queue = []
        
    def add(self,data):
        if not self.queue:
            self.queue.insert(0,data)
        else:
            self.queue.append(data)
        return f'Item {data} added to queue'
    
    def remove(self):
        if not self.queue:
            return 'Queue is empty'
        else:
            self.queue = self.queue[1:]
    
    def size(self):
        if not self.queue:
            return 'Queue is empty'
        else:
            return len(self.queue)
        
    def show(self):
        if not self.queue:
            return 'Queue is empty'
        else:
            return self.queue
        
    def __str__(self):
        return str(self.queue)
        
