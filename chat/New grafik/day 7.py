# def user_report(data, raiting_limit):
#     repot_list = []
#     for key, value in data.items():
#         name = value["name"]
#         feedbacks = value["feedbacks"]
#         for feedback in feedbacks:
#             if feedback['rating'] > raiting_limit:
#                 result = (name, feedback["text"], feedback["rating"])
#                 repot_list.append(result)
#     return repot_list
#
#
# feedbacks = {"user1": {"name": "Alice", "feedbacks": [{"text": "Loved the service!", "rating": 5}, {"text": "Will come again.", "rating": 4}]},
#     "user2": {"name": "Bob", "feedbacks": [{"text": "Not bad.", "rating": 3}, {"text": "Could be better.", "rating": 2}]},
#     "user3": {"name": "Charlie", "feedbacks": [{"text": "Terrible experience.", "rating": 1}]}}
#
# report = user_report(feedbacks, 3)
# for name, text, raiting_limit in report:
#     print(f'Отзыв пользователя {name}: {text} ({raiting_limit})')

#=====================================================================================

# def filter_orders_by_price(order, price_limit):
#     report_list = []
#     for key, value in order.items():
#         name = value["name"]
#         orders = value["orders"]
#         for order in orders:
#             if order["price"] > price_limit:
#                 result = (name, order["product"], order["price"])
#                 report_list.append(result)
#
#     return report_list
#
# orders = {"client1": {"name": "Alice", "orders": [{"product": "Laptop", "price": 1200}, {"product": "Mouse", "price": 25}]},
#     "client2": {"name": "Bob", "orders": [{"product": "Desk", "price": 300}, {"product": "Chair", "price": 150}]},
#     "client3": {"name": "Charlie", "orders": [{"product": "Monitor", "price": 250}]}}
#
# report = filter_orders_by_price(orders,200)
# for name, product, price in report:
#     print((f'Товары выше лимита от клиента {name}: {product} ({price})'))

#=====================================================================================
# def count_price_up_limit(data, price_limit):
#     count = 0
#     if isinstance(data, dict):
#         for value in data.values():
#             count += count_price_up_limit(value, price_limit)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict):
#                 if "price" in item:
#                     if item['price'] > price_limit:
#                         count += 1
#                 else:
#                     count += count_price_up_limit(item, price_limit)
#             elif isinstance(item, list):
#                 count += count_price_up_limit(item, price_limit)
#     return count
#
# catalog = {"Electronics": {"Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500},],
#                            "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200},]},
#     "Home Appliances": {"Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250},],
#                         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150},]
#     }
# }
#
# report = count_price_up_limit(catalog, 100)
# print(report)

#=====================================================================================
# def find_most_expensive(data):
#     max_value = float('-inf')
#     max_name = ''
#     if isinstance(data, dict):
#         if "price" in data and "name" in data:
#             return data["name"], data["price"]
#         for key, value in data.items():
#             name, price = find_most_expensive(value)
#             if price > max_value:
#                 max_value = price
#                 max_name = name
#     elif isinstance(data, list):
#         for item in data:
#             name, price = find_most_expensive(item)
#             if price > max_value:
#                 max_value = price
#                 max_name = name
#
#     return max_name, max_value
#
# catalog = {"Electronics": {"Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500},],
#                            "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200},]},
#     "Home Appliances": {"Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250},],
#                         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150},]
#     }
# }
#
# name, price = find_most_expensive(catalog)
# print(f'Самый дорогой товар {name}: {price}')

#=====================================================================================

# def find_3rd_expensive(data):
#     more_expensive_goods = []
#     if isinstance(data, dict):
#         if "price" in data and "name" in data:
#             result = (data["name"], data["price"])
#             more_expensive_goods.append(result)
#         else:
#             for key, value in data.items():
#                 more_expensive_goods.extend(find_3rd_expensive(value))
#     elif isinstance(data, list):
#         for item in data:
#             more_expensive_goods.extend(find_3rd_expensive(item))
#     return more_expensive_goods
#
# catalog = {"Electronics": {"Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500},],
#                            "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200},]},
#     "Home Appliances": {"Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250},],
#                         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150},]
#     }
# }
#
# total = find_3rd_expensive(catalog)
# sorted_goods = sorted(total, key=lambda x: x[1], reverse=True)
#
# if len(sorted_goods) >= 3:
#     third = sorted_goods[2]
#     print(f'3-й по цене товар: {third[0]} ({third[1]})')
# else:
#     print(f'недостаточно товаров для определения 3-го по цене')
#=====================================================================================
# def find_all_products(data):
#     products = []
#     if isinstance(data, dict):
#         for key, value in data.items():
#             products += find_all_products(value)
#     if isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "name" in item and "price" in item:
#                 result = (item["name"], item["price"])
#                 products.append(result)
#             else:
#                 products += find_all_products(item)
#     return products
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# report = find_all_products(catalog)
# for name, price in report:
#     print(f'Список товаров {name}: {price}')
#=====================================================================================
# def count_all_products(data):
#     count = 0
#     if isinstance(data, dict):
#         for key, value in data.items():
#             count += count_all_products(value)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "name" in item and "price" in item:
#                 count += 1
#             else:
#                 count += count_all_products(item)
#     return count
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# report = count_all_products(catalog)
# print(report)
#=====================================================================================
# def count_all_products(data):
#     total_price = 0
#     if isinstance(data, dict):
#         for key, value in data.items():
#             total_price += count_all_products(value)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "price" in item:
#                 total_price += item["price"]
#             else:
#                 total_price += count_all_products(item)
#     return total_price
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# report = count_all_products(catalog)
# print(report)
#=====================================================================================
# def average_price(data):
#     count = 0
#     total_price = 0
#     if isinstance(data, dict):
#         for value in data.values():
#             sub_count, sub_total_price = average_price(value)
#             count += sub_count
#             total_price += sub_total_price
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "name" in item and "price" in item:
#                 count += 1
#                 total_price += item["price"]
#             else:
#                 sub_count, sub_total_price = average_price(item)
#                 count += sub_count
#                 total_price += sub_total_price
#     return count, total_price
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# count, total_price = average_price(catalog)
# average = total_price / count if count > 0 else 0
# print(f"Количество товаров: {count}, Общая цена: {total_price}, Средняя цена: {average}")
#=====================================================================================
# def price_up_1000(data, limit_price):
#     price_up = []
#     if isinstance(data, dict):
#         for value in data.values():
#             price_up += price_up_1000(value, limit_price)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "name" in item and "price" in item:
#                 if item["price"] > limit_price:
#                     result = (item['name'], item['price'])
#                     price_up.append(result)
#             else:
#                 price_up += price_up_1000(item, limit_price)
#     return price_up
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# report = price_up_1000(catalog, 900)
# for name, price in report:
#     print(f'Наименование товара {name}: {price}')
#=====================================================================================
# def max_price_product(data):
#     max_price = float('-inf')
#     max_name = ''
#     if isinstance(data, dict):
#         for value in data.values():
#             name, price = max_price_product(value)
#             if price > max_price:
#                 max_price = price
#                 max_name = name
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and "name" in item and "price" in item:
#                 if item["price"] > max_price:
#                     max_price = item["price"]
#                     max_name = item["name"]
#             else:
#                 name, price = max_price_product(item)
#                 if price > max_price:
#                     max_price = price
#                     max_name = name
#     return max_name, max_price
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
#         "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
#         "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
#     }
# }
#
# name, price = max_price_product(catalog)
# print(f'Самый дорогой товар {name}: {price}')
#=====================================================================================
def get_max_price(data):
    max_price = float('-inf')
    if isinstance(data, dict):
        for value in data.values():
            price = get_max_price(value)
            if price > max_price:
                max_price = price
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "name" in item and "price" in item:
                if item["price"] > max_price:
                    max_price = item["price"]
            else:
                price = get_max_price(item)
                if price > max_price:
                    max_price = price
    return max_price

def find_products_with_price(data, target_price):
    result = []
    if isinstance(data, dict):
        for value in data.values():
            result += find_products_with_price(value, target_price)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "name" in item and "price" in item:
                if item["price"] == target_price:
                    result.append((item["name"], item["price"]))
                else:
                    result += find_products_with_price(item, target_price)
    return result

catalog = {
    "Electronics": {
        "Laptops": [{"name": "Laptop A", "price": 1000}, {"name": "Laptop B", "price": 1500}],
        "Phones": [{"name": "Phone A", "price": 800}, {"name": "Phone B", "price": 1200}]
    },
    "Home Appliances": {
        "Vacuum Cleaners": [{"name": "Vacuum A", "price": 200}, {"name": "Vacuum B", "price": 250}],
        "Microwaves": [{"name": "Microwave A", "price": 100}, {"name": "Microwave B", "price": 150}]
    }
}

price = get_max_price(catalog)
products = find_products_with_price(catalog, price)
print(f'Максимальная цена: {price}')
print('Товары с этой ценой:')
for name, price in products:
    print(f'{name}: {price}')