import keyword

def check_keyword(word):
    if word in keyword.kwlist:
        print(word, "is a keyword")
    else:
        print(word, "is identifier")

code = """
x=10
y=x+20
print(y)
"""

numbers = []
identifiers = []
special_chars = []
lineno = 1
i = 0

while i < len(code):
    c = code[i]

    if c.isdigit():
        token_value = c
        i += 1
        while i < len(code) and code[i].isdigit():
            token_value += code[i]
            i += 1
        numbers.append(int(token_value))
        continue

    if c.isalpha() or c == '_':
        word = c
        i += 1
        while i < len(code) and (code[i].isalnum() or code[i] == '_'):
            word += code[i]
            i += 1
        identifiers.append(word)
        continue

    if c in [' ', '\t']:
        i += 1
        continue

    if c == '\n':
        lineno += 1
        i += 1
        continue

    special_chars.append(c)
    i += 1
print("Numbers in the program:", numbers)

print("\nKeywords and identifiers:")
for word in identifiers:
    check_keyword(word)

print("\nSpecial characters:", special_chars)
print("\nTotal number of lines:", lineno)