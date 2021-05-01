from collections import deque

quantity = int(input())
data = input()

people = deque([])

while not data == "Start":
    people.append(data)

    data = input()

data = input()

while not data == "End":
    if data.startswith("refill"):
        refill, l = data.split(" ")
        quantity += int(l)
    else:
        person = people.popleft()
        if int(data) <= quantity:
            print(f"{person} got water")
            quantity -= int(data)
        else:
            print(f"{person} must wait")

    data = input()

print(f"{quantity} liters left")