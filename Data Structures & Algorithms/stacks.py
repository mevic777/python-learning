# Stacks - LIFO

stk = []

# Add elem to the stack
stk.append(5)
stk.append(4)
stk.append(3)
stk.append(2)

# Pop smth from the stack
x = stk.pop()
print(x)
print(stk)

# What's the top of the stack
print(stk[-1])

# IsEmpty
if stk:
    print(True)

# Queues - FIFO
from collections import deque

q = deque()
print(q)

# Enqueue
q.append(5)
q.append(2)
q.append(6)
q.append(7)
print(q)

# Dequeue - remove pop from left
y = q.popleft()
print(y)
print(q)

# Peek from the left side
print(q[0])

# Peek from the right side
print(q[-1])