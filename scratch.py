list1 = [1, 1]
list2 = []
n = int(input())
k = 0
h = n - 2
while h > k:
    for i in range(len(list1) + 1):
        if i - 1 == -1:
            list2.append(1)
        elif i + 1 > len(list1):
            list2.append(1)
        else:
            list2.append(list1[i - 1] + list1[i])
    k = k + 1
    list1 = list2
    list2 = []
print(list1)