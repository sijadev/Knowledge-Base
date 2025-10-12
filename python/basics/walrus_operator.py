from package.console_clear import clear
clear()

"""
There is new syntax := that assigns values to variables as part of a larger expression. 
It is affectionately known as “the walrus operator” 
In this example, the assignment expression helps avoid calling len() twice
"""

text = 'Hello my friend!'

# Example 1:
if (length := len(text)) > 10:
    print(f"List is too long ({length} elements, expected <= 10)")

print('\n')

# Example 2:
while ((length := len(text)) > 1):
    print(length)
    # In jeden loop wird wird eine Stelle vom String entfernt.
    text = text[:-1]

print('\n' + text)
