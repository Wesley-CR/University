def balanced_parenthesis(text, stack=0):
    if text == '':
        return stack == 0
    if text[0] == '(':
        return balanced_parenthesis(text[1:], stack + 1)
    elif text[0] == ')':
        if stack == 0:
            return False
        return balanced_parenthesis(text[1:], stack - 1)

    return balanced_parenthesis(text[1:], stack)

print(balanced_parenthesis("(()())"))  # Output should be True
print(balanced_parenthesis("(()()"))   # Output should be False

