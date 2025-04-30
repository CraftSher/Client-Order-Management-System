class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 0

class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = True

monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False
