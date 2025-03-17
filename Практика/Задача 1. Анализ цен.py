import random

original_prices = [random.randint(-100, 100) for _ in range(5)]
#print(original_prices)
new_prices = original_prices[:]

for i in range(len(original_prices)):

    if new_prices[i] < 0:
        new_prices[i] = 0
print(original_prices)
print(new_prices)

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))