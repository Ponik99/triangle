def get_triangle(count: int):
    for ii in range(count):
        n = 2 + ii
        summ = 2 * n - 1
        for i in range(1, n + 1):
            star = 2 * i - 1
            backspace = int((summ - star) / 2 + (count - ii))
            print(backspace * ' ' + star * '*' + backspace * ' ')


get_triangle(14)
