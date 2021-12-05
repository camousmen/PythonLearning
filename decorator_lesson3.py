def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello habr"
 
def yeah_it_works(func):
    def  decorated(*args, **kwargs):
        print('Yeah, it works')
        return func()
    return  decorated

def first_decorator(func):
    def wrapper1():
        """это декоратор first_decorator."""
        print(f'Докстринг декларируемой функции: {func.__doc__}')
        print(f'Декорируемая функция {func.__name__}')
        return func()
    return wrapper1

def second_decorator(func):
    def wrapper2():
        """Это  декоратор  second_decorator."""
        print(f'Докстринг декорируемой функции: {func.__doc__}')
        print(f'Декорируемая функция {func.__name__}')
        return func()
    return wrapper2


@first_decorator
@second_decorator
def do_nothing():
    """Я ничего не знаю. Я никуда не летаю."""

do_nothing()




@yeah_it_works
def  f1():
    print('f1() here')

@yeah_it_works
def f2():
    print('f2() here')

@yeah_it_works
def f3():
    print('f3() here')

f1()
f2()
f3()