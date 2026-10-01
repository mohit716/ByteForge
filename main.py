source = "25 + 300"

tokens = []

i = 0

while i < len(source):
    char = source[i]

    if char.isspace():
        i += 1
        continue


    if char.isdigit():
        number = ""

        while i < len(source) and source[i].isdigit():
            number += source[i]
            i += 1
        
        tokens.append(("NUMBER", number))
        continue
    
    elif char == "+":
        tokens.append(("PLUS", char))

    elif char == "-":
        tokens.append(("MINUS", char))

    elif char == "*":
        tokens.append(("MULTIPLY", char))

    elif char == "/":
        tokens.append(("DIVIDE", char))

    else:
        raise Exception(f"Invalid character: {char}")

    i += 1

left = tokens[0]
operator = tokens[1]
right = tokens[2]

ast = {
    "type": "BinaryExpression",
    "left": left,
    "operator": operator,
    "right": right
}

print(ast)