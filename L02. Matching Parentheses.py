text = input()

indexes = []

for i in range(len(text)):
    if text[i] == "(":
        indexes.append(i)
    elif text[i] == ")":
        end_i = i
        start_i = indexes.pop()
        print(text[start_i:end_i+1])