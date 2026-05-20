class Drink:
    def __init__(self, name, price,in_stock):
        self.data = {
            "name": name,
            "price": price,
            "is_stock": in_stock
        }
    def display(self):
        print(f'Name: {self.data["name"]}')
        print(f'Price: {self.data["price"]}')
        status = "Available" if self.data["is_stock"] else "Out of Stock"
        print(f"Stock: {status}")

class CoffeeShop:
    def __init__(self):
        self.data = {}
    def add_drink(self, name, price, in_stock):
        new_drink = Drink(name,price,in_stock)
        self.data[name] = new_drink
        print('New drink added in data')
    def order(self,drink_name):
        if drink_name in self.data:
            drink = self.data[drink_name]
            if drink.data['is_stock']:
                print(f'Enjoy your {drink.data['name']}')
            else:
                print(f"Sorry you're {drink.data['name']} is out of stock")
        else:
            print('Drink is not on menu')
    def show_menu(self):
        print("\n=== COFFEE SHOP MENU ===")
        for name, drink in self.data.items():
            drink.display()
            print("---")


cof = CoffeeShop()

cof.add_drink('Dexter',8.99,True)
cof.show_menu()
cof.order('Dexter')