from collections import deque

name = input()
queue = deque()

while not name == "End":
    if name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)
    name = input()

print(f"{len(queue)} people remaining.")