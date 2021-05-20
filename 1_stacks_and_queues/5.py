from collections import deque

children = deque(input().split())
count = int(input())

while len(children) > 1:
    children.rotate(-count)
    print(f"Removed {children.pop()}")

print(f"Last is {children.pop()}")