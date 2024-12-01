
with open("input/input_day1.txt", "r") as file:
    content = file.readlines()

# with open("day1/input.txt", "r") as file:
#     content = file.readlines()


# print(content)
l1 = []
l2 = []
for line in content:
    line = line.strip()
    line = line.split("   ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))
    
l1.sort()
l2.sort()
l3 = []

for i in range(len(l1)):
    l3.append(abs(l1[i]-l2[i]))

print(sum(l3))











