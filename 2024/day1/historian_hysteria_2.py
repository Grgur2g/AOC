
with open("input/input_day1.txt", "r") as file:
    content = file.readlines()

# with open("day1/input.txt", "r") as file:
#     content = file.readlines()

l1 = []
l2 = []
for line in content:
    line = line.strip()
    line = line.split("   ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))
    
from collections import Counter

mapa = Counter(l2)
suma = 0
for n in l1:
    suma+=mapa[n]*n

print(suma)












