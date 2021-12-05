def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        a_function_to_decorate()
        print("А я - код, срабатывающий после")

    return  the_wrapper_around_the_original_function

@my_shiny_new_decorator
def a_stand_alone_function():
    print ("Я просто одинокая функция")


a_stand_alone_function()

#  теперь  мы изменим поведение функции stand_alone, декорируем ее

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")
# это все равно что означает another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)

"""Вкладывание декораторов друг в друга """
def bread(func):
    def wrapper(): 
        print("</----\>")
        func()
        print("<\____/>")
    
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()
# sandwich  =  bread(ingredients(sandwich))

