class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self,quantity):
        if self.size >= self.quantity + quantity:
            self.quantity += quantity

        return self.size

    def status(self):
        free_space = abs(self.size - self.quantity)

        return free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
