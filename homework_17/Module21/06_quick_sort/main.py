def partition(numbers):
    pivot = numbers[-1]
    less = []
    equal = []
    greater = []
    for number in numbers[:-1]:
        if number < pivot:
            less.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)
    equal.append(pivot)
    return less, equal, greater

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    less, equal, greater = partition(numbers)
    return quick_sort(less) + equal + quick_sort(greater)


nums = [5, 8, 9, 4, 2, 9, 1, 8]

result = partition(nums)
result1 = quick_sort(nums)
print(result)
print(result1)
