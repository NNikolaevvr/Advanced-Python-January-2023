class Shop:
    def __init__(self, name, items:list):
        self.name = name
        self.items = items

    def get_items_count(self):

        counted = len((self.items))

        return counted


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
