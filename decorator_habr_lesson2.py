""" Передача аргументов в декорируемую функцию """

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2): # аргументы прибывают сюда
        print("Смотри, что я получил", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_full_name("Питер", "Венкман")

""" Максимально общий  декоратор через список *args и словарь **kwargs """

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # данная обёртка принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("PYthon is cool, no argument here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)