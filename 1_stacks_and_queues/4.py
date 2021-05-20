from collections import deque

liters = int(input())

name = input()
queue = deque()


while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        liters += int(command.split()[-1])
    else:
        liters_wanted = int(command)
        name = queue.popleft()
        if liters >= liters_wanted:
            liters -= liters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()

print(f"{liters} liters left")


a = deque()