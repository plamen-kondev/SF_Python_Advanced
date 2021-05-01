from collections import deque

kids = deque([kid for kid in input().split()])
step = int(input())

current_position = 0

while len(kids) > 1:
    for i in range(step):
        if i < step - 1:
            kids.append(kids.popleft())
        elif i == step - 1:
            removed_kid = kids.popleft()
            print(f"Removed {removed_kid}")

print(f"Last is {kids.popleft()}")