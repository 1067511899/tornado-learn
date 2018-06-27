import math
from threading import Thread
from time import sleep


def calc_fact(num):
    sleep(0.001)
    math.factorial(num)


num = 600000
t = Thread(target=calc_fact, daemon=True, args=[num])
print("About to calculate: {}!".format(num))
t.start()
print("Calculating...")
t.join()
print("Calculated")
