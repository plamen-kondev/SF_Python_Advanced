num_queries = int(input())

queries = []

for i in range(num_queries):
    query = input()
    if query.startswith("1"):
        query = query.split(" ")
        queries.append(int(query[1]))
    elif query == "2":
        if queries:
            queries.pop()
    elif query == "3":
        if queries:
            sorted_queries = sorted(queries)
            maxi = sorted_queries.pop()
            print(maxi)
    elif query == "4":
        if queries:
            sorted_queries = sorted(queries, reverse=True)
            mini = sorted_queries.pop()
            print(mini)

while len(queries) > 1:
    print(queries.pop(), end=", ")
if queries:
    print(queries.pop())