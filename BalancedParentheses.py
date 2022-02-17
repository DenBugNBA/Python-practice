def balanced(expression):
    s = []
    for i in expression:
        if i == "(":
            s.insert(0, i)
        elif i == ")":
            if not s:
                return False
            else:
                s.pop(0)
    return not s


print(balanced(input()))
