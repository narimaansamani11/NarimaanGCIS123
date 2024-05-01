"""
Group number: 4

Student 1: Ala'a Al Zein
Student 2: Sama Ahmad
Student 3: Narimaan Samani

Github link (1): https://github.com/narimaansamani11/NarimaanGCIS123/blob/main/Activity4.py
Github link (2): https://github.com/Samanimerr/gcis123.git
"""
import csv  # Importing the CSV module for reading CSV files

class Article:  # Class representing an article
    # Represents an article with name, price, and quantity.
    __slots__ = ["__name", "__price", "__quantity"]

    def __init__(self, name, price, quantity):
        # Initializes an Article object with a name, price, and quantity.
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def getName(self):
        # Returns the name of the article.
        return self.__name

    def getPrice(self):
        # Returns the price of the article.
        return self.__price

    def setPrice(self, price):
        # Sets the price of the article.
        self.__price = price

    def getQuantity(self):
        # Returns the quantity of the article.
        return self.__quantity

    def setQuantity(self, quantity):
        # Sets the quantity of the article.
        self.__quantity = quantity

    def __str__(self):
        # Returns a string representation of the article.
        return f'Article: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price}'

def Inventory():
    # Reads inventory data from a CSV file and returns it as a dictionary.
    inventory = {}

    # Open the CSV file
    with open("D:\RIT\RIT Courses\Spring 2024\GCIS\Activity 4\products.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)

        # Read each row in the CSV file
        for row in csv_reader:
            name = row[0]
            quantity = int(row[1])
            price = float(row[2])
            inventory[name] = (quantity, price)
        
    return inventory

class Cart:
    # Represents a shopping cart.
    __slots__ = ["__Purchased_List"]

    def __init__(self, Purchased_list = []):
        # Initializes a Cart object with a list of purchased articles.
        self.__Purchased_List = Purchased_list

    def Add_Product(self, name, quantity):
        # Adds a product to the shopping cart.
        inventory = Inventory()
        New_Price = 0

        # Check if the product is available in inventory
        if name in inventory:
            Item_Price = inventory[name][1]
            Available_Quantity = int(inventory[name][0])

            # Check if the requested quantity is available
            if Available_Quantity >= quantity:
                if quantity == 1:
                    New_Price += Item_Price
                else:
                    New_Price = (New_Price + Item_Price) * quantity
                # Check if the article is already in the cart
                for article in self.__Purchased_List:
                    if article.getName() == name:
                        article.setQuantity(article.getQuantity() + quantity)
                        article.setPrice(article.getPrice() * quantity)
                        break
                else:
                    # If article not in cart, add it
                    self.__Purchased_List.append(Article(name, New_Price, quantity))
                inventory[name] = (Available_Quantity - quantity, Item_Price)
            else:
                print("Sorry, the quantity you entered is not available!")

        else:
            print("Sorry, the item you entered is not available!")

    def Remove_Product(self, name, quantity):
        # Removes a product from the shopping cart.
        inventory = Inventory()
        New_Price = 0 

        if name in inventory:
            Item_Price = inventory[name][1]
            Available_Quantity = int(inventory[name][0])

            if Available_Quantity >= quantity:
                if quantity == 1:
                    New_Price += Item_Price
                else:
                    New_Price = (New_Price + Item_Price) * quantity
                
                for article in self.__Purchased_List:
                    if article.getName() == name:
                        article.setQuantity(article.getQuantity() - quantity)
                        article.setPrice(article.getPrice() - New_Price)

                        # If quantity becomes zero or less, remove the article from cart
                        if article.getQuantity() <= 0:
                            self.__Purchased_List.remove(article)
                        break
                else:
                    print("The item is not in your cart")
                
                inventory[name] = (Available_Quantity + quantity, Item_Price)
            else:
                print("Sorry, the quantity you entered isn't available")
        else:
            print("Sorry, Your shopping cart is empty")

    def DisplayCart(self):
        # Displays the contents of the shopping cart.
        if len(self.__Purchased_List) == 0:
            print("Sorry, your shopping cart is empty")
        else:
            for item in self.__Purchased_List:
                print(item)

def main():
    # Main function to manage the shopping application.
    while True: 
        try:
            while True: 
                print("1. List all items, inventory and price")
                print("2. List cart shopping items")
                print("3. Add an item to the shopping cart")
                print("4. Remove an item from the shopping cart")
                print("5. Checkout")
                print("6. Exit") 

                Choice = int(input("Enter your choice: "))

                if Choice == 1:
                    # Display inventory
                    inventory = Inventory()
                    print(inventory)
                    print()
                    continue_option = input("Do you want to continue? (y/n): ")
                    if continue_option != 'y' and continue_option != 'Y':
                        print("Bye bye")
                        return

                elif Choice == 2:
                    # Display shopping cart items
                    shopping_cart = Cart()
                    shopping_cart.DisplayCart()

                elif Choice == 3:
                    # Add item to shopping cart
                    name = input("Enter the name of the item you want to add: ")
                    quantity = int(input("Enter the quantity of the item you want to add: "))
                    shopping_cart = Cart()
                    shopping_cart.Add_Product(name, quantity)

                elif Choice == 4:
                    # Remove item from shopping cart
                    name = input("Enter the name of the item you want to remove: ")
                    quantity = int(input("Enter the quantity of the item you want to remove: "))
                    shopping_cart = Cart()
                    shopping_cart.Remove_Product(name, quantity)

                elif Choice == 5:
                    # Checkout
                    shopping_cart = Cart()
                    shopping_cart.DisplayCart()
                    total_price = 0
                    for price in shopping_cart._Cart__Purchased_List:
                        total_price = total_price + price.getPrice()
                    tax = 0.07 * total_price
                    total_price_with_tax = total_price + tax
                    print(f"Total Price: {total_price}")
                    print(f"Tax (7%): {tax}")
                    print(f"Total Price with Tax: {total_price_with_tax}")
                    return

                elif Choice == 6:
                    print("Thank you! Have a great day!")
                    return
                break

        except ValueError:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
