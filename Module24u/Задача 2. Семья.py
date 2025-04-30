
class Family:
    name = ""
    money = 0
    house = False

    def print_info(self):
        print("Family name: " + self.name, "Family funds: " + str(self.money), "Having a house: " + str(self.house), sep='\n')

    def get_money(self, count):
        self.money += count
        print(f"Earned {count} money! Current value: {self.money}")

    def buy_a_house(self, price, discount=0):
        house_price = (price - price * (discount / 100))
        if self.money >= house_price:
            self.money -= house_price
            print(f"House purchased! Current money: {self.money}")
            self.house = True
        else:
            print("Not enough money!")


human = Family()
human.name = "Common family"
human.money = 100000

human.print_info()
house_price = 900000
human.buy_a_house(house_price)
human.get_money(house_price - human.money)
human.buy_a_house(house_price)
human.print_info()
