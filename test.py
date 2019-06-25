list1 = [90, 78, 98, 88, 68, 38, 58, 38, 8, 28]

for j in range(len(list1) - 1):
    for i in range(len(list1) - 1 - j):
        # 循环一次，找到一个最大的，于是减少一次，就减j
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
print(list1)

list2 = ['a', 'b', 'c']
str2 = ''.join(list2)
print(str2)
