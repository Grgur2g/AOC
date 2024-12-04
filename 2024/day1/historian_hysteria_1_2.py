
with open("input/input_day1.txt", "r") as file:
    content = file.readlines()

# with open("day1/input.txt", "r") as file:
#     content = file.readlines()

l1, l2 = [], []

for line in content:
    line = line.strip().split("   ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))

print("rezultat 1: \t",sum(abs(a-b) for a, b in zip(sorted(l1),sorted(l2))))

from collections import Counter
mapa = Counter(l2)

print("rezultat 2: \t",sum(n * mapa[n] for n in l1))











