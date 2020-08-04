class Node: 
	def __init__(self, data):  #class constructor
		self.data = data
		self.next = None   #stores link to the nextlist element
		self.prev = None    #stores link to the previous list element


class Stack:
	def __init__(self): #class constructor
		self.head = None   #stores head list element

	def push(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			self.head.prev = new_node
			new_node.next = self.head
			new_node.prev = None
			self.head = new_node

# Function to pop top element and return the element from the stack
	def pop(self):
		if self.head is None:
			return None
		else:
			temp = self.head.data
			self.head = self.head.next
			self.head.prev = None
			return temp

	def top(self):
		return self.head.data

# Function to return the size of the stack
	def size(self):
		temp = self.head
		count = 0
		while temp is not None:
			count = count + 1
			temp = temp.next
		return count

# Function to check if the stack is empty or not
	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

# Function to show list 
	def show_list(self):
		print("Stack elements are:")
		temp = self.head
		while temp is not None:
			print(temp.data, end="->")
			temp = temp.next

print("Stack was successufully initiaized")

stack = Stack()
try:
    while True:
        print('\n'+'Availible operations for stack:')
        print('add')
        print('delete')
        print('quit')
        print('empty?')
        print('show')
        print('size')

        do = input('What would you like to do? ').split()

        operation = do[0].strip().lower()


        if operation == 'empty?':
            answer = stack.IsEmpty()
            if answer is True:
                print("Stack is empty")
            else:
                print("Stack is not empty")

        elif operation == 'delete':

            if stack.top() is None:
                print("You can't delete element while stack is empty !")
            else:
            	print("Deleting element from stack: ", stack.top())
            	stack.pop()

        elif operation == 'show':
            stack.show_list()

        elif operation == 'size':
            print("Size of stack now : ", stack.size())

        elif operation == 'add':
            add_el = input("Enter the value you want to add : ")
            stack.push(int(add_el))

        elif operation == 'quit':
            break

except Exception:
    print("Error. Incorrect input !")

