def check_valid_parentheses(s: str) -> bool:
    ''' check if s is valid parentheses string '''

    stack = []
    parentheses = {'[':']', '{':'}', '(': ')'}
    open_parentheses = parentheses.keys()
    closed_parentheses = parentheses.values()

    for c in s:
        if c in open_parentheses:
            stack.append(c)
        if c in closed_parentheses:
            p = stack.pop()
            print(f"{p=}")
            print(f"{parentheses[p]=}")
            print(f"{c=}")
            if parentheses[p] != c:
                return False
        
    if len(stack) != 0:
        return False
    else:
        return True


s='abc'
assert check_valid_parentheses(s) is True

s='ab{c}'
assert check_valid_parentheses(s) is True

s='a(b{c)d}'
assert check_valid_parentheses(s) is False