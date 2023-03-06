#!/usr/bin/env python3

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period
\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit():
    #"""Calculate deposit yield."""
    initial_sum = int(input("Secify sum: "))
    percent = int(input("Specify percent: "))
    fixed_period = int(input("Specify fixed period: "))
    set_period = int(input("Set period: "))
    per = percent / 100
    profit = (1 + per) ** (set_period / fixed_period)
    total = initial_sum * profit
    return total
#
def read_file():
    f = open("offers.txt", 'r')
    a = f.read()
    print(a)
    f.close

def write_file():
    data = str(deposit())
    f = open("offers.txt", "w")
    f.write(data)
    f.close

write_file()
read_file()