brackets = input()

is_balanced = False
opening_brackets = []

for el in brackets:
    if el == "{" or el == "[" or el == "(":
        opening_brackets.append(el)
    elif el == "}":
        if opening_brackets:
            if opening_brackets.pop() == "{":
                is_balanced = True
            else:
                is_balanced = False
                break
    elif el == "]":
        if opening_brackets:
            if opening_brackets.pop() == "[":
                is_balanced = True
            else:
                is_balanced = False
                break
    elif el == ")":
        if opening_brackets:
            if opening_brackets.pop() == "(":
                is_balanced = True
            else:
                is_balanced = False
                break
    if opening_brackets:
        is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")
