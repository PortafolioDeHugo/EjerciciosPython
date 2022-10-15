class pizza1:
    def __init__(self, type, price, size):
        self.type = type
        self.price = price
        self.size = size


from Pizza1 import pizza1

pizzaV = pizza1("vegetariana",5,"small")

print(pizzaV.size)



