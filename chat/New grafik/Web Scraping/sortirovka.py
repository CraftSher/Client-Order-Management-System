sales = {
    "Ali": 120,
    "Zarina": 85,
    "Bekzod": 150,
    "Dilshod": 95
}
sorted_sales = sorted(sales.items(), key=lambda item: item[1], reverse=True)

print(sorted_sales)

new_list = list(sales.items())

n = len(new_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if new_list[j][1] > new_list[j + 1][1]:
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

print(new_list)