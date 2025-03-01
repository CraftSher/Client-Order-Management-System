numbers = int(input('Сколько будет чисел? '))
nums = []

for i in range(1, numbers + 1):
    num = int(input(f'Введите {i} число: '))
    nums.append(num)

print()
print('Изначальный список:', nums)
N = len(nums)
for _ in range(N - 1):
    for i in range(N - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print()
print('Отсортированный список:', nums)



