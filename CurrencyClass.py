# QUESTION:
# Create class Currency (amount, unit). Overload the '==' operator to determine if 2 currencies are equal.

class Currency:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return (self.amount == other.amount) and (self.unit == other.unit)

    def __repr__(self):
        return f"{self.amount} {self.unit}"


# Example
c1 = Currency(50, "USD")
c2 = Currency(50, "USD")
c3 = Currency(60, "USD")

print(c1 == c2)  # True
print(c1 == c3)  # False
