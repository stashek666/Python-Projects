with open('calc.txt', 'r') as f:
    s = 0
    for line in f:
        try:
            s += eval(line)
        except (SyntaxError, TypeError):
            pass
    print(s)
