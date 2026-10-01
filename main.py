source = "2 + 3"

tokens = []

for char in source:
    if char.isdigit():
        tokens.append(("NUMBER", char))
    elif char == "+":
        tokens.append(("PLUS", char))

print(tokens)
