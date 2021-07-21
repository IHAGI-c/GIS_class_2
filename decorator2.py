def decorator(func):
    def decorated(a, b):
        if a > 0 and b > 0:
            func(a, b)
        else:
            print('err')
    return decorated


@decorator
def area(a, b):
    T_A = a * b * 1/2
    S_A = a * b
    print('삼각형의 넓이 :', T_A)
    print('사각형의 넓이 :', S_A)


area(2,8)
area(-2,4)