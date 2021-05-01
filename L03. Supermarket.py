from collections import deque

data = input()

clients = deque([])

while not data == 'End':
    if data == 'Paid':
        for cl in range(len(clients)):
            print(clients.popleft())
    else:
        clients.append(data)

    data = input()

print(f"{len(clients)} people remaining.")