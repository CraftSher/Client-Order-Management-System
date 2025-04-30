def add_num(seq, number):
    seq = list(seq)
    for i_num in range(len(seq)):
        seq[i_num] += number
    return seq


origin_tuple = (3, 1, 4, 1, 5)
changed_list = add_num(origin_tuple, 5)
print(origin_tuple)
print(changed_list)