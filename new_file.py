def best_func_ever(a, b):
    while a:
        b += 1
        a -= 1
    return b


print(best_func_ever(int(input()), int(input())))
