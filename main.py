source = "25 + 300"

tokens = []

for char in source:
    if char.isdigit():
        tokens.append(("NUMBER", char))
    elif char == "+":
        tokens.append(("PLUS", char))

print(tokens)
