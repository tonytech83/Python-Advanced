# Exam: 03. Cupcake Shop
# From: Python Advanced Exam - 14 February 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2812#2
def stock_availability(*args):
    inventory, *orders = args

    if orders[0] == 'delivery':
        for item in orders[1:]:
            inventory.append(item)
    else:
        try:
            if isinstance(orders[1], int):
                for _ in range(int(orders[1])):
                    inventory.pop(0)
            else:
                for item in orders[1:]:
                    inventory = [x for x in inventory if x != item]
        except IndexError:
            inventory.pop(0)

    return inventory


# Test code
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
