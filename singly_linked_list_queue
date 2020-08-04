class Node: #class which stores nodes of our list
    
    def __init__(self, data): #constructor
       self.data = data
       self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class Queue: #class for queue
    
    def __init__(self):   #constructor
        self.head = None
        self.last = None

    def enqueue(self, data):  #adding elelemt to queue
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self): #delete element from queue
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def IsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def __len__(self):
        return len(self.temp)

    def print_struct(self):
        current = self.head
        self.temp = []

        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)

print("Queue was successufully initiaized")

my_struct = Queue()
try:
    while True:

        print('\n'+'Availible operations :')
        print('add <value>')
        print('delete')
        print('quit')
        print('empty?')
        print('show')
        print('size'+'\n')

        do = input('What would you like to do? ').split()

        operation = do[0].strip().lower()
        if operation == 'empty?':
            answer = my_struct.IsEmpty()
            if answer is True:
                print("Queue is empty")
            else:
                print("Queue is not empty")

        elif operation == 'add':
            my_struct.enqueue(int(do[1]))

        elif operation == 'delete':
            dequeued = my_struct.dequeue()
            if dequeued is None:
                print("You can't delete element while queue is empty !")
            else:
                print('Element that was deleted : ', int(dequeued))

        elif operation == 'show':
            check = my_struct.IsEmpty()
            if check == False:
                my_struct.print_struct()
            else:
                print("Queue can not be shown because it is empty.")

        elif operation == 'size':
            print(my_struct.__len__())

        elif operation == 'quit':
            break
except Exception:
    print("Error. Wrong input !")
