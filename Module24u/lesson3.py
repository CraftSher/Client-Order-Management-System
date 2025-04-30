# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     frends = []
#
#     def print_info(self):
#         print('Name: {}\nPassword: {}\nBan status: {}'.format(self.user_name, self.password, self.is_banned))
#
#     def add_frends(self, frend):
#         if isinstance(frend, User):
#             self.frends.append(frend.user_name)
#         else:
#             self.frends.append(frend)
#
# user_1 = User() #экземпляр класса User
# user_2 = User()
# user_2.user_name ='Alina'
# user_1.add_frends('Bob')
# user_1.add_frends(user_2)
# print(user_1.frends)

class Family:
    surname = 'Tagirov'
    money = 350000
    home_dubay = False
    def info(self):
        print(
            'Family name: {}\nFamily funds:{}\nHaving a house: {}'.format(
                self.surname, self.money, self.home_dubay
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value {}'.format(amount, self.money))

    def buy_home(self, home_price, discount=0):
        home_price -= home_price * discount / 100
        if self.money >= home_price:
            self.money -= home_price
            self.home_dubay = True
            print("Home purchased! Current money: {}\n".format(self.money))
        else:
            print('Not enough money!!!\n')


My_family = Family()
My_family.info()
print('Try to buy a home:')
My_family.buy_home(420000)

if not My_family.home_dubay:
    My_family.earn_money(50000)
    print('Try to buy a home again:')
    My_family.buy_home(420000, 10)

My_family.info()