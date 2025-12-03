# QUESTION:
# Create a class FruitBasket (fruit_name, price per kg).
# Overload '+' operator that adds two fruit baskets with unique fruits having least price from both baskets.

class FruitBasket:
    def __init__(self, fruits=None):
        # fruits stored as {"apple": 120, "mango": 80}
        self.fruits = fruits if fruits else {}

    def __add__(self, other):
        new_fruits = self.fruits.copy()

        for fruit, price in other.fruits.items():
            if fruit in new_fruits:
                new_fruits[fruit] = min(new_fruits[fruit], price)
            else:
                new_fruits[fruit] = price

        return FruitBasket(new_fruits)

    def __repr__(self):
        return str(self.fruits)


# Example
b1 = FruitBasket({"apple": 120, "mango": 80})
b2 = FruitBasket({"apple": 100, "orange": 90})

print(b1 + b2)
# Output: {'apple': 100, 'mango': 80, 'orange': 90}
