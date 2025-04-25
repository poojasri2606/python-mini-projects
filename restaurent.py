class restaurent:
    def __init__(self):
        self.menu={
    "Coffee":40,
    "Burger":60,
    "Noodles":80,
    "Cola":30,
    "Salad": 50
    }
        self.order = {}
    
    def show_menu(self):
        print("\nmenu")
        for item,price in self.menu.items():
            print(f"{item}: Rs {price}")

    def take_order(self):
        self.show_menu()

        print("\nEnter your order. Type 'done' when finished")

        while True:
            item=input("Item: ").strip().title()
            if item.lower()=="done":
                break
            if item in self.menu:
                quantity=int(input(f"Enter quantity for {item}: "))

                if item in self.order:
                    self.order[item]+=quantity
                else:
                    self.order[item]=quantity

                print(f"Added {quantity} X {item} to your order.")

            else:
                print("Item not found in the menu. Please try again")

    def view_bill(self):
            if not self.order:
                print("\nNo items ordered yet.")

                return
            print("\nYour Bill:")
            total=0
            for item,quantity in self.order.items():
                price=self.menu[item]*quantity
                print(f"{item} X {quantity} = Rs {price}")

                total += price

            print(f"Total amount: Rs {total}")

    def run(self):
            while True:
                print("\n--Welcome to the Restaurent--")
                print("1. Show Mneu")
                print("2. Place Order")
                print("3. View Bill")
                print("4. Exit")

                choice= input("Choose an option: ").strip()

                if choice=="1":
                    self.show_menu()
                elif choice=="2":
                    self.take_order()
                elif choice=="3":
                    self.view_bill()
                elif choice=="4":
                    print("Thank you for visiting. Goodbye!")

                    break
                else:
                    print("Invalid option. Please try again.")


if __name__=="__main__":
    app = restaurent()

    app.run()
