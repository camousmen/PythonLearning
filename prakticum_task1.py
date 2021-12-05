from sys import getsizeof
import random


def arr_to_byte_discrete(arr):
    len_arr = 0b1 << len(arr)
    byte_arr = 0b0
    for i in range(0, len(my_arr) - 1):
        if not my_arr[i] | 0:
            byte_arr = byte_arr | 0
        else:
            byte_arr = byte_arr | 1
        byte_arr = byte_arr << 1
    byte_arr = len_arr + byte_arr
    return byte_arr


def file_read():
    result = ""
    with open('input.txt') as f:
        for i in f.read():
            result += i
        f.close()
    return result


def file_write_random_int():
    with open('input.txt', mode='w') as f:
        arr = [random.randint(0,5) for i in range(100)]
        buf = ""
        for a in arr:
            buf+= str(a)
        f.write(buf)
        f.close()

file_write_random_int()
arr = file_read()

byte2_arr = bin(0b1100100)
#print(byte_arr)
#print(byte2_arr)
#print(len(byte2_arr))

x = 0b0
print(x)
for i in range(10):
    x = (x << 1) | 1


my_arr = [0, 0, 3, 0, 2, 3, 0, 1, 3]
len_arr = 0b1 << len(my_arr)

print(bin(len_arr))

byte_arr = 0b0
for i in range(0, len(my_arr)-1):
    if my_arr[i] == 0:
        byte_arr = byte_arr | 0
    else:
        byte_arr = byte_arr | 1
    byte_arr = byte_arr << 1

byte_arr = len_arr + byte_arr
print(bin(byte_arr))

res_arr = arr_to_byte_discrete(my_arr)
print(bin(res_arr))

