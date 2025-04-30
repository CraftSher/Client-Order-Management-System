import os

for path in os.listdir('..'):
    print(os.path.join(os.path.abspath('..'), path))