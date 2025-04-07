# TODO здесь писать код
nums = (6, 3, -1, 8, 4, 10, -5)

def sort_tuple_of_integers(nums):
    for num in nums:
        if not isinstance(num, int):
            return nums
    new_list = list(nums)
    new_list.sort()
    return tuple(new_list)

result = sort_tuple_of_integers(nums)
print(result)