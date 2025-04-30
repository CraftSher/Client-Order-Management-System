file_1 = open('task/group_1.txt', 'r', encoding= 'utf-8')
summa = 0
diff = 0
for i_line in file_1:
    info = i_line.split()
    score = int(info[2])
    summa += score
    diff -= score
file_1.close()
file_2 = open('Additional_info/group_2.txt', 'r', encoding= 'utf-8')
compose = 1
for i_line in file_2:
    info = i_line.split()
    score = int(info[2])
    compose *= score
file_2.close()
print(summa)
print(diff)
print(compose)