#Restaurant management system
# Menu items in the restro

menu = {
    "tea": 15,
    "coffee": 20,
    "biscuit": 10,
    "maggi": 40,
    "pizza": 90,
    "burger": 70,
    "pasta": 80
    }
print("--------------------")
print("Welcome to PyRestro\n--------------------\nHere is the menu details: ")
print("Tea: 10\nCoffee: 20\nMaggi: 40\nPizza: 70\nBurger: 60\nPasta: 80")
print("--------------------")

order_total = 0
#Taking the orders from customers
while True:
    item = input("\nSelect the items to order: ").lower()
    
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to cart")
    else: print("Sorry its unavailable, please select another item\n")
    
    item2 = input("\nDo u want to add more items? (YES/NO):").lower()
    if item2 != "yes": break
        
print("\n-----------------------------------")
print(f"Amount to be paid is: {order_total}")
print("--------------------------------------\nThanks for visiting US")  

    
    
