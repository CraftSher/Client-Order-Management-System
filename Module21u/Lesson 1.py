def shortest_seg_range(str, tpl):
    return min(len(str), len(tpl))

str = 'abc'
tpl = (10, 20, 30, 40)

pairs = ((str[i_sym], tpl[i_sym]) for i_sym in range(shortest_seg_range(str, tpl)))
print(pairs)

for i_sym in pairs:
    print(i_sym)
print(zip(str, tpl))