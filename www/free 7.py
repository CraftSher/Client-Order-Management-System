# import random
# nums = [random.randint(1, 10) for _ in range(5)]
# print(nums)
# nums.remove(nums[2])
# print(nums)
# nums.reverse()
# print(nums)
# count = nums.count(nums[1])
# print(nums[1],count)
# nums1 = [random.randint(1, 10) for _ in range(3)]
# print(nums1)
# nums.extend(nums1)
# print(nums)

nums = [3, 1, 2, 3, 2, 4, 1, 5]
unique_nums = []
seen = set()

for num in nums:
    if num not in seen:
        unique_nums.append(num)
        seen.add(num)

print("Исходный список:", nums)
print("Уникальные элементы:", unique_nums)

# import random
# nums = [random.randint(1, 10) for _ in range(7)]
# k = int(input('Введите число сдвига: '))  # число позиций для сдвига
# # Если k больше длины списка, можно взять остаток от деления
# k = k % len(nums)
# rotated = nums[-k:] + nums[:-k]
# print(nums[-k:])
#
# print("Исходный список:", nums)
# print("Список после ротации:", rotated)
