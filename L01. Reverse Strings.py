text = [l for l in input()]

new_text = []

for i in range(len(text)):
    new_text.append(text.pop())

print(''.join(new_text))