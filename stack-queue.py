from collections import deque

# Implementing stack using list
stack = ["Monday", "Tuesday", "Wednesday"]
stack.append("Thursday")
stack.append("Friday")
print(stack)

# Removes the last item
print(stack.pop())
print(stack)

# Implementing queue using list
queue = ["Monday", "Tuesday", "Wednesday"]
queue.append("Thursday")
queue.append("Friday")
print(queue)

#Remove the first item
print(queue.pop(0))
print(queue)

# Deque (Doubly Ended Queue) in Python is implemented using the 
# module “collections“. Deque is preferred over list in the cases where 
# we need quicker append and pop operations from both the ends of 
# container, as deque provides an O(1) time complexity for append and 
# pop operations as compared to list which provides O(n) time complexity.

# Implementing stack using deque
stackqueue = deque(["Monday", "Tuesday"])
print(stackqueue)
stackqueue.append("Wednesday")
print(stackqueue)
print(stackqueue.pop())
stackqueue.appendleft("Sunday")
print(stackqueue.popleft())
print(stackqueue)