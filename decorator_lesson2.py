import time

def check_print():
    print("Ne robit")

# Функция для измерения быстродействия функции-аргумента
def time_of_function(func):
    def wrapper():
        print('Добыр Бобыр')
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')
        return result
    return wrapper

def sleep_one_sec():
    time.sleep(1)

def uppercase(func):
    def  wrapper():
        original_result = func()
        return f'Большие {original_result.upper()}'
    return wrapper


@uppercase
def greet():
    return 'маленькие буквы'


print(greet())