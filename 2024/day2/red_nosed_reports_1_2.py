
with open("input/input_day2.txt", "r") as file:
    content = file.readlines()

# with open("day2/input.txt", "r") as file:
#     content = file.readlines()

def calc_diff(arr):
    start = arr[0]
    for a in arr[1:]:
        curr = abs(start-a)
        start = a
        if curr > 3 or curr == 0: return 0
    return 1

suma, suma2 = 0, 0

for line in content:
    arr = [int(x) for x in line.strip().split(" ")]

    if sum(arr[:2]) / 2 > sum(arr[-2:]) / 2: arr = arr[::-1] ### from smallest to higest always

    if calc_diff(arr) and arr == sorted(arr): suma+=1 #### first sum if it is sorted and within magnitude 1 - 3

    for i in range(len(arr)):
        a = arr[:]
        a.pop(i)

        if calc_diff(a) and a == sorted(a):
            suma2+=1 #### second sum, same as previous minus 1 faulty number per array
            break

print("rezultat 1: \t",suma, "\nrezultat 2: \t",suma2)











