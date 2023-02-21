list1 = []
n = int(input())

for i in range(n):
    list1.append([])

for k in range(len(list1)):
    for e in range(1, n + 1):
        list1[k].append(e)

for i in list1:
    print(i)