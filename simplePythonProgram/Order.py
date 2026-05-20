class MenuItem:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        print(f'{self.name} (${self.price}) - {self.category}')
        
class Order:
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total = 0
    def add_item(self,menu_item):
        self.items.append(menu_item)
        self.total += menu_item.price
        print(f'Addee {menu_item.name} to {self.customer_name}s order')
    def show_order(self):
        count = len(self.items)
        if count == 0:
            print(f'No added order')
        else:
            print(f' Order for {self.customer_name}')
            for item in self.items:
                item.display()
            print(f'Total : ${self.total}')
    def pay(self):
        print(f"${self.total} paid. Thank you {self.customer_name}!")
        self.items = []
        self.total = 0
    def remove_item(self,menu_item):
        if menu_item in self.items:
            self.items.remove(menu_item)
            self.total -= menu_item.price
            print(f'Removed')
        else:
            print(f"{menu_item.name} not found in order!")


burger = MenuItem('Burger', 6.00, 'Main')
fries = MenuItem('Fries',5.00,'Side')
soda = MenuItem('Soda',2.00,'Drink')

order1 = Order('Vincent')
order1.show_order()
order1.add_item(burger)
order1.show_order()
order1.add_item(fries)
order1.show_order()
order1.remove_item(burger)
order1.show_order()