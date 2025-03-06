def merge_sorted_lists(list1, list2):
    merged_list = sorted(list1 + list2)
    unique_list = []
    for num in merged_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list



list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)