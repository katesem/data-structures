import collections

my_deque = collections.deque([]) # creating an empty deque

my_deque.append('one')
my_deque.appendleft('two')
my_deque.appendleft('three')
my_deque.append('four')
my_deque.popleft()
my_deque.pop()

print(my_deque) 

#Output : deque(['two', 'one'])
