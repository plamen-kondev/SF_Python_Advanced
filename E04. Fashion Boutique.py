box = [int(n) for n in input().split(" ")]
capacity = int(input())

racks = 1
current_capacity = 0

while box:
    cloth = box.pop()
    if current_capacity + cloth <= capacity:
        current_capacity += cloth
    else:
        racks += 1
        current_capacity = cloth

print(racks)