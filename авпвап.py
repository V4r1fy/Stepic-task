list1 = []
n = int(input())
n2 = 1
for i in range(n):
    list1.append([])

for k in range(len(list1)):
    n2 = n2 + 1
    for e in range(1, n2):
        list1[k].append(e)

for g in list1:
    print(g)