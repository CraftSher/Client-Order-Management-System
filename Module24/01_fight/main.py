import random

class Warrior:
    def __init__(self, name):
        self.warrior_name = name
        self.warrior_health = 100

    def striking(self, warrior):
        warrior_hit = 20
        warrior.warrior_health -= warrior_hit

    def live_or_dead(self):
        if self.warrior_health > 0:
            return True
        else:
            return False

    def info_warrior(self):
        print('Warrior {}: health {}\n'.format(self.warrior_name, self.warrior_health))


warrior_1 = Warrior('Воин 1')
warrior_2 = Warrior('Воин 2')
while True:
    attack = random.randint(1, 2)
    if attack == 1:
        warrior_1.striking(warrior_2)
        print('{} атаковал {}'.format(warrior_1.warrior_name, warrior_2.warrior_name))
        print('Здоровье {} осталось {}'.format(warrior_2.warrior_name, warrior_2.warrior_health))
        if warrior_2.warrior_health <= 0:
            print('{} погиб'.format(warrior_2.warrior_name))
            break
    else:
        warrior_2.striking(warrior_1)
        print('{} атаковал {}'.format(warrior_2.warrior_name, warrior_1.warrior_name))
        print('Здоровье {} осталось {}'.format(warrior_1.warrior_name, warrior_1.warrior_health))
        if warrior_1.warrior_health <= 0:
            print('{} погиб'.format(warrior_1.warrior_name))
            break
if warrior_1.live_or_dead()  and not warrior_2.live_or_dead():
    print('Победил {}'.format(warrior_1.warrior_name))
else:
    print('Победил {}'.format(warrior_2.warrior_name))