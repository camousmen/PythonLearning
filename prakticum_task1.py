from sys import getsizeof
import random


def know_range(n):
    result = ""
    half = n // 2
    if n == 1:
        result = "1"
        return result
    for i in range(1, half+1):
        result += str(i) + " "
    reverse_half = result[::-1]
    reverse_half = reverse_half[1:]
    if n & 1: # если нечетный
        result += str(half+1) + " "
    result = result + reverse_half
    return result
    



def arr_to_byte_discrete(arr):
    len_arr = 0b1 << len(arr)
    byte_arr = 0b0
    for i in range(0, len(arr) - 1):
        if not arr[i] | 0:
            byte_arr = byte_arr | 0
        else:
            byte_arr = byte_arr | 1
        byte_arr = byte_arr << 1
    byte_arr = len_arr + byte_arr
    return byte_arr


def file_read_to_byte_discrete(f_path):
    res_arr = 0b0
    len_arr = 0b0
    n = 0
    with open(f_path) as f:
        n = int(f.readline()) + 1
        print(n)
        len_arr = 0b1 << n
        buf = ""
        #for i in f.read():
        i = " "
        while i != "":
            i = f.read(1)
            if i != " " and i != "":
                buf+= i
            else:
                if not int(buf) | 0:
                    res_arr = res_arr | 0
                else:
                    res_arr = res_arr | 1
                res_arr = res_arr << 1
                buf = ""
        f.close()
    #res_arr = res_arr >> 1
    print()
    res_arr = len_arr + res_arr
    res_arr = res_arr >> 1
    print(bin(res_arr))
    return res_arr


def file_write_random_int(dist, length):
    with open('input.txt', mode='w') as f:
        arr = [random.randint(0, dist) for i in range(length)]
        buf = ""
        f.write(str(len(arr)))
        f.write('\n')
        for a in arr:
            buf+= str(a)
            buf+= " "
        f.write(buf)
        f.close()



#file_write_random_int(3, 15)
print(know_range(2))

byte_arr = file_read_to_byte_discrete('input.txt')
result_arr = ""
n = len(bin(byte_arr)) - 3
print(n)
number = 0

# проверим левый край если там не ноль
left_null = 0
if ((byte_arr >> n-1) & 1):
    number = 0
    for i in range(n-2, -1, -1):
        if not ((byte_arr >> i) & 1): # если найдем нолик выходим
            if number != 0:
                left_null = number
            else:
                left_null = 1
            break
        else:
            number += 1
    if number != 0:
        for i in range(number, 0, -1):
            result_arr += str(i) + " "
number = 0
for i in range(n-left_null, -1, -1):
    if not ((byte_arr >> i) & 1):
        # найден нолик
        if number != 0:
            result_arr += know_range(number) + " "
        result_arr += "0 "
        number = 0
    else:
        number += 1
# проверим правый край если там не ноль просто печатаем номера
if (byte_arr & 1):
    for i in range(1, number+1):
        result_arr += str(i) + " "
print(result_arr)










byte2_arr = bin(0b1100100)
#print(byte_arr)
#print(byte2_arr)
#print(len(byte2_arr))

x = 0b0
print(x)
for i in range(10):
    x = (x << 1) | 1


my_arr = [0, 1, 4, 9, 0, 1, 2, 6, 0]
len_arr = 0b1 << len(my_arr)
n = len(my_arr)

print(bin(len_arr))

byte_arr = 0b0
for i in range(0, len(my_arr) - 1):
    if my_arr[i] == 0:
        byte_arr = byte_arr | 0
    else:
        byte_arr = byte_arr | 1
    byte_arr = byte_arr << 1

byte_arr = len_arr + byte_arr
print(bin(byte_arr))

result_arr = []


# левый проход
number = 0
for i in range(n-1, -1, -1):
    if not ((byte_arr >> i) & 1):
        # найден нолик
        result_arr.append(0)
        number = 1
    elif number != 0:
        result_arr.append(number)
        number += 1
    else:
        result_arr.append(0)

print(result_arr)
# правый проход
number = 0
res2_arr = []
for i in range(n):
    if not ((byte_arr >> i) & 1):
        res2_arr.append(0)
        number = 1
    elif number != 0:
        res2_arr.append(number)
        b = result_arr[n-i-1]
        result_arr[n-i] = (min(b, number))
        number += 1
    else:
        res2_arr.append(0)

print(res2_arr)
print(result_arr)
