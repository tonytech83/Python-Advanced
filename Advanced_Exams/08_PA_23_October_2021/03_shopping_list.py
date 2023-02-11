# Exam: 03. Shopping List
# From: Python Advanced Exam - 23 October 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/3227#2
def shopping_list(budget, **products):
    if budget < 100:
        return 'You do not have enough budget.'

    current_budget = budget
    bought_products = []
    for product, data in products.items():
        total_price = data[0] * data[1]
        if total_price < current_budget:
            current_budget -= total_price
            bought_products.append(f'You bought {product} for {total_price:.2f} leva.')
            if len(bought_products) == 5:
                break

    return '\n'.join(bought_products)


# Test code 1
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

# Test code 2
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

# Test code 3
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
