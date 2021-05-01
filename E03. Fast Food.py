from collections import deque

food_quantity = int(input())
orders = deque([int(order) for order in input().split(" ")])

max_order = sorted(orders).pop()

while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.popleft()
    else:
        break

print(f"{max_order}")
if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", end=" ")
    while len(orders) > 1:
        print(orders.pop(), end=" ")
    if len(orders) == 1:
        print(orders.pop())