class ShoppingList:
    def __init__(self):
        self.items = []

    def add(self,item_name):
        self.items.append(item_name)
        print(f'Added new item: {item_name}')

    def update(self,old_name,new_name):
            if old_name in self.items:
                index = self.items.index(old_name)
                self.items[index] = new_name
                print(f' New name for {old_name} is {new_name}')
            else:
                print(f'Not Found')
    
    def delete(self,item_name):
        for item in self.items:
            if item_name in item:
                self.items.remove(item_name)
                print(f'{item_name} is removed from the memory')
            else:
                print(f'Not Found')
    
    def showList(self):
        print('Shopping List')
        count = len(self.items)
        if count == 0:
            print('No items added')
        else:
            for item in self.items:
                print(f'{item} ')

myList = ShoppingList()

while True:  # Keep running forever until user exits
    print("\n===== SHOPPING LIST MENU =====")
    print("1. Add item")
    print("2. Update item")
    print("3. Delete item")
    print("4. View list")
    print("5. Exit")
     
    choice = input('Enter your choice: ')
    if choice == '1':
        item = input("Enter item name: ")
        myList.add(item)
    elif choice == '2':
        name = input("Enter you want to update: ")
        new_name = input("Enter the new name: ")
        myList.update(name,new_name)
    elif choice == '3':
        item = input('Enter the name to delete: ')
        myList.delete(item)
    elif choice == '4':
        myList.showList()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print('Invalid choice!!')
