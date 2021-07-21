

def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated


@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World!')



def decorator(func):
    def decorated(a,b):
        if a > 0 and b > 0:
            func(a,b)
        else:
            print('err')


@decorator
def area(a,b):
    T_A = a * b * 1/2
    S_A = a * b
    print('삼각형의 넓이 :', T_A)
    print('사각형의 넓이 :', S_A)

area(2,-1)