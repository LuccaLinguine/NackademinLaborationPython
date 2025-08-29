# Inventory Management Exercise
# Create a program that manages a list of product dictionaries for a store inventory.
# Each product dictionary should contain the following keys: 'id', 'name', 'price', 'quantity', 'category'.
# Initialize the list with at least 10 sample products.
# Implement separate functions for each functionality.
# Handling errors is optional, try your best!
# """
# Show a menu for the user with the following options:

# 1. Display all products
# 2. Add a new product
# 3. Update a product's information
# 4. Remove a product
# 5. Search for a product by name
# 6. Calculate total inventory value
# 7. Find the most expensive product
# 8. Find products with low stock (quantity < 5)
# 9. Generate a report of products by category
# 10. Update quantities (simulate a sale)
# 11. Exit the program
# """

import random

# Sample categories
categories = ["Electronics", "Clothing", "Food", "Books", "Home"]

# Initialize inventory with sample products
# here is my inventory list with 10 sample products
inventory = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "quantity": 10,
        "category": "Electronics",
    },
    {
        "id": 2,
        "name": "T-shirt",
        "price": 19.99,
        "quantity": 50,
        "category": "Clothing",
    },
    {   
        "id": 3, 
        "name": "Apple",
        "price": 0.99, 
        "quantity": 100, 
        "category": "Food"
    },
    {   
        "id": 4, 
        "name": "Crayon",
        "price": 0.69,
        "quantity": 11, 
        "category": "Home"
    },
    {   
        "id": 5, 
        "name": "Chair",
        "price": 11.10, 
        "quantity": 21, 
        "category": "Home"
    },
    {   
        "id": 6, 
        "name": "Mug",
        "price": 12.50, 
        "quantity": 71, 
        "category": "Home"
    },
    {   
        "id": 7, 
        "name": "iPhone",
        "price": 1200.00, 
        "quantity": 3, 
        "category": "Electronics"
    },
    {   
        "id": 8, 
        "name": "Harry Potter 1",
        "price": 9.90,
        "quantity": 50, 
        "category": "Books"
    },
    {   
        "id": 9, 
        "name": "Pripps Blå",
        "price": 1.20, 
        "quantity": 1000, 
        "category": "Food"
    },
    {   
        "id": 10, 
        "name": "Jeans",
        "price": 11.20, 
        "quantity": 40, 
        "category": "Clothing"
    }

]


    # Implement displaying all products in a formatted way
    # Here i display all the products in the inventory
def display_products():
    print(inventory)
    pass

# here the user can add a new product to the inventory
def add_product(inventory):
    # if statement that checks if the inventory is empty or not
    if inventory:
        new_id = inventory[-1]["id"] + 1
    # else statement that sets the id to 1 if the inventory is empty (in this case this will never happen)
    else:
        new_id = 1
    # here are my variables that take user input for the new product
    name = input("Enter new product name:")
    price = input("Enter price name:")
    quantity = input("Enter quantity name:")
    category = input("Enter category name:")
# here i assign a dictionary to the new item with the user inputs.
    new_item = {
        "id": new_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
        
    }
    # append the new item to the inventory list
    inventory.append(new_item)
    #confirmation
    print(f"New item added: {new_item}")

    # function that updates a products information
def update_product(inventory):
    # try to catch invalid inputs
    try:
        item_id = int(input("Enter the ID of the item you would like to update"))
    # if the input is invalid, print an error message and return to the main menu
    except ValueError:
       print("Invalid Input, please try again")
       return
    # for loop that searches for the item with the given id, assigns item to variable item and breaks the loop
    item = None
    for i in inventory :
        if i["id"] == item_id:
            item = i
            print(item)
            break
    # if item is None, print an error message and return to the main menu
    if not item:
        print("Please enter a valid itemID")
        return
    # if item is found, print the item and ask the user for new values for each key
    print(f"You have selected this item id: {item}, you can now proceed to update the item:")
    new_name = input(f"Enter new product name: (leave blank if you want to keep original)")
    new_price = input(f"Enter price name: (leave blank if you want to keep original)")
    new_quantity = input(f"Enter quantity name: (leave blank if you want to keep original)")
    new_category = input("Enter category name: (leave blank if you want to keep original)")
    # if the user input is not blank, update the corresponding key in the item dictionary    
    if new_name:
        item["name"] = new_name
    if new_price:
        item["price"] = float(new_price)
    if new_quantity:
        item["quantity"] = int(new_quantity)
    if new_category:
        item["category"] = new_category

# function to remove a product from the inventory    
def remove_product(inventory):
    # try to catch invalid inputs
    try:
        item_id = int(input("Enter the ID of the item you would like to remove"))
    except ValueError:
       print("Invalid Input, please try again")
       return
    # for loop that searches for the item with the given id, assigns item to variable item and breaks the loop
    item = None
    for i in inventory :
        if i["id"] == item_id:
            item = i
        else:
            print("Please enter a valid itemID")
    # removes item if found
    inventory.remove(item)
    print(f"Item removed: {item}")
# function to search for a product by name
def search_product(inventory):
    # Implement searching for a product by name
    search_name = input("Enter the product name to search for: ").lower()
    # another for loop that searches for the item with the given name, assigns item to variable found_items and breaks the loop
    found_items = None 
    for item in inventory:
        if search_name in item["name"].lower():
            found_items = item
            print(f"These items match your search: {found_items}")
    # catch to print if no items are found
    if found_items is None:
        print("No products found with that name.") 

# function to calculate the total inventory value
def calculate_total_value(inventory):
    # Implement calculating the total inventory value
    #creating an emptyy variable to store the total value
    total_value = 0
    # for loop to iterate through the inventory and calculate the total value
    for item in inventory:
        if item["price"] is None:
            item["price"] = 0
        total_value += item["price"] * item["quantity"]
    print(f"Total inventory value: ${total_value:.2f}")


# function to find the most expensive product
def find_most_expensive(inventory):
    # itterate through the inventory and find the product with the highest price
    for item in inventory:
        max_price = max(item["price"] for item in inventory)
        print(f"The most expensive product is: {max_price}")
        return item
    

# function to find products with low stock (quantity < 5)
def find_low_stock(inventory):
    # iterates through the inventory and finds products with quantity less than 5
    lowstockitems = None
    for item in inventory:
        if item["quantity"] < 5:
            lowstockitems = item
            print(f"These items are low in stock: {lowstockitems}")
    return lowstockitems
    

# function to generate a report of products by category
def generate_category_report(inventory):
    # assigns user input to variable categoryinput
    categoryinput = input("Enter the category you would like a report on:")
    # iterates through the inventory and finds products in the given category
    for item in inventory:
        if item["category"].lower() == categoryinput.lower():
            print(f"These items are in the {categoryinput} category: {item}")
    return item

 # function to update quantities (simulate a sale)
def update_quantities(inventory):
    # try to catch invalid inputs
    try:
        item_id = int(input("Enter the ID of the item you would like to update"))
    except ValueError:
       print("Invalid Input, please try again")
       return
    # for loop that searches for the item with the given id, assigns item to variable item and breaks the loop
    item = None
    for i in inventory :
        if i["id"] == item_id:
            item = i  
            new_quantity = input(f"Enter quantity name: (leave blank if you want to keep original)")
            i["quantity"] = int(new_quantity)
    if not item:
        print("Please enter a valid itemID")
        return

# Main menu logic
while True:
    choice = int(
        input("""
    1. Display all products
    2. Add a new product
    3. Update a product's information
    4. Remove a product
    5. Search for a product by name
    6. Calculate total inventory value
    7. Find the most expensive product
    8. Find products with low stock
    9. Generate a report of products by category
    10. Update quantities (simulate a sale)
    11. Exit program
    Enter your choice: """)
    )
    if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        print("Invalid choice. Please enter a number between 1 and 11.")
        continue

    if choice == 1:
        display_products()
    elif choice == 2:
        add_product(inventory)
    elif choice == 3:
        update_product(inventory)
    elif choice == 4:
        remove_product(inventory)
    elif choice == 5:
        search_product(inventory)
    elif choice == 6:
        calculate_total_value(inventory)
    elif choice == 7:
        find_most_expensive(inventory)
    elif choice == 8:
        find_low_stock(inventory)
    elif choice == 9:
        generate_category_report(inventory)
    elif choice == 10:
        update_quantities(inventory)
    elif choice == 11:
        print("Exiting program. Goodbye!")
        break
    
