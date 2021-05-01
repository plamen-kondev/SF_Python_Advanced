from collections import deque

n_stations = int(input())

starting_station = 0
full_circle = False
stations = deque([])

for _ in range(n_stations):
    stations.append(input())

for starting_station in range(n_stations):
    tank = 0
    for station in range(n_stations):
        current_station = stations[station]
        petrol, distance = current_station.split(" ")
        distance = int(distance)
        tank += int(petrol)
        if distance > tank:
            stations.append(stations.popleft())
            break
        else:
            tank -= distance
        if station == n_stations-1:
            full_circle = True
            break
    if full_circle:
        break

print(starting_station)
