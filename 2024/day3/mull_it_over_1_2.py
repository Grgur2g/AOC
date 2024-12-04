
with open("input/input_day3.txt", "r") as file:
    content = file.readline()

# with open("day3/input.txt", "r") as file:
#     content = file.readlines()

import re

def calc(line):
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    sumo = 0
    for match in matches:
        numbers = match[4:-1].split(",")
        sumo+= (int(numbers[0])*int(numbers[1]))
    return sumo

print("rezultat 1: \t",calc(content.strip()))



suma = 0
niz = re.split(r"don't\(\)",content.strip())
suma += (calc(niz[0])) #### always starts with do()
for part in niz[1:]:
    arr = re.split(r"do\(\)",part)
    suma += sum(calc(line) for line in arr[1:] if len(arr) > 1)

print("rezultat 2: \t",suma)



