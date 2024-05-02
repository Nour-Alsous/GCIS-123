"""
Students: Syed Iftesam, Bacher Al Tajer, Bechir Ben Zaied
contribution of Syed: 50%
contribution of Bacher: 25%
contribution of Bechir: 25%
Description: 

Repository Links:
Syed : https://github.com/LagSpikeee/GCIS-123/blob/main/group8-activity4.py
Bechir : 
Bachar : 
"""

import csv

INVENTORY = {}

""" This function is responsible for reading the .csv file and use the information in it to populate the dictionary INVENTORY"""
def read_data(file_path):
    
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                name, price, quantity = row
                INVENTORY[name] = Article(name, float(price), int(quantity))

    except FileNotFoundError:
        print("The File could not be found")

""" This class is used for representing the articles in the cart. It contains 3 attributes inside: name, price and quantity"""
class Article:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return "Article: " + str(self.name) + " Quantity: " + str(self.quantity) + " Price: " + str(self.price)
    
""" This Class is used for representing the shopping cart and has the attribute list_of_purchased. It includes 4 functions that simulates 
    the functioning of the cart"""
class Cart:
    def __init__(self):
        self.list_of_purchased = []

    """ This function is responsible to check inside the INVENTORY and see if the product named is available or not, it then checks if the user
    inputed value exceeds the number of stock available or not, and also updates the cart with the updated products once its added to it."""
    def addProduct(self, name, quantity):

        if name in INVENTORY:
            article = INVENTORY[name]
            available_quantity = article.getQuantity()
            
            
            if quantity > available_quantity:
                quantity = available_quantity
            
            article.setQuantity(available_quantity - quantity)
            
            for purchased_article in self.list_of_purchased:
                if purchased_article.getName() == name:
                    purchased_article.setQuantity(purchased_article.getQuantity() + quantity)
                    return
            
            new_article = Article(name, article.getPrice(), quantity)
            self.list_of_purchased.append(new_article)
    
    """This function works similarly to the last as well, it checks if the input by the user exceeds the actual available amount and 
    carries forward. After the user inputs which item to remove and how many it then updates the cart with this information"""
    def removeProduct(self, name, quantity):
        for purchased_article in self.list_of_purchased:
            if purchased_article.getName() == name:
                
                if quantity >= purchased_article.getQuantity():
            
                    INVENTORY[name].setQuantity(INVENTORY[name].getQuantity() + purchased_article.getQuantity())
                    self.list_of_purchased.remove(purchased_article)
                else:
                  
                    purchased_article.setQuantity(purchased_article.getQuantity() - quantity)
                    INVENTORY[name].setQuantity(INVENTORY[name].getQuantity() + quantity)
                return
    
    """A simple function that is responsible to output the cart information if it has any items added to it or not"""
    def displayCart(self):
        if not self.list_of_purchased:
            print("There are no item listed in the cart")
        else:
            for article in self.list_of_purchased:
                print(article)
    
    """This function is responsible for calculating the prices of the product. If the user has added from then 3 items it will apply a 
    discount fo 10%, and by default the total amount will have a VAT amount applied for 7%"""
    def checkout(self):

        total_bill = 0

        for article in self.list_of_purchased:
            price = article.getPrice()
            quantity = article.getQuantity()
        
            if quantity > 3:
                price *= 0.10
            
            total_bill += quantity * price
        
        total_bill *= 1.07
        
        print("Total bill (applying VAT): $" , total_bill)

"""This provoides a visual disply of choices for the users to pick from"""
def menu():
    print("1. List all items, inventory, and prices")
    print("2. List cart shopping items")
    print("3. Add an item to the shopping cart")
    print("4. Remove an item from the shopping cart")
    print("5. Checkout")
    print("6. Exit")

"""The main function that initalizes the calling of the functions and is looped"""
def main():

    read_data('products.csv')
    
    cart = Cart()
    
    while True:
       
        menu()
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            for article in INVENTORY.values():
                print(article)
        
        elif choice == "2":
            name = input("Please input the products name: ").strip()
            quantity = int(input("Please Input the amount: "))
            cart.addProduct(name, quantity)
        
        elif choice == "3":
            name = input("Please input the products name: ").strip()
            quantity = int(input("Please Input the amount: "))
            cart.removeProduct(name, quantity)
        
        elif choice == "4":
            cart.displayCart()
        
        elif choice == "5":
            cart.checkout()
        
        elif choice == "6":
            print("Closing the Program...")
            break
        
        else:
            print("Please select an option from the given choices")


if __name__ == "__main__":
    main()
