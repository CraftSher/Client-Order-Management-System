import  random
list1 = [random.randint(-100, 100) for _ in range(10)]
print(list1)

list1.remove(list1[2])
print(list1)

list1.reverse()
print(list1)

count1 = list1.count(list1[5])
print(count1)

list2 = [random.randint(100, 300) for _ in range(10)]
print(list2)
list1.extend(list2)
print(list1)