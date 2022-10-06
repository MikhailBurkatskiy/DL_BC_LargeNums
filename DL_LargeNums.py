import random as rd
import time

ALLOWED_VALUES = (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)

def get_value(x: int):
    return 2**x

def get_random_hex(x: int):
    return hex(rd.randint(0, get_value(x)))

def bruteforce(x: int):
    start_time = time.time()
    a = get_random_hex(x)
    for i in range(0x0, get_value(x)):
        if (hex(i) == a):
            print("К-сть часу (ms) -> ", (time.time() - start_time) * 1000)
            return

for i in ALLOWED_VALUES:
   print("Кількість варіантів ключів для ", i, " = ", get_value(i), "\n")

for i in ALLOWED_VALUES:
   print("Випадкове значення ключа для ", i, " = ", get_random_hex(i), "\n")

bruteforce(int(input("Введіть для якої n-бітної послідовності використати метод BruteForce -> ")))


