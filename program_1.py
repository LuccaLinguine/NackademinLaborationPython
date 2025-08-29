# Create a program that generates a list of 100 random numbers.
# Try to handle errors by using if-statements or try-except blocks.
# You can Google how this can be done.
# Show a menu for the user that gives the following choices:

# 1. Show all data in the list (NOTE: YOU SHOULD NOT JUST PRINT THE ENTIRE LIST, e.g., print(my_list) is wrong) DONE
# 2. Sort the list in ascending order DONE
# 3. Sort the list in descending order DONE
# 4. Add a number DONE
# 5. Remove a specific number DONE
# 6. Remove the last number DONE
# 7. Remove the first number DONE
# 8. Sum all numbers

# You should try to use separate functions for each functionality.

# Starting code
import random
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

random_numbers = []
# here i iterate over a range of 100 and generate 100 random numbers between 1 and 100
for i in range(100):
    random_numbers.append(random.randint(1, 100))

# here i create a function that prints the list of data
def show_data():
    # Implement
    for item in random_numbers:
        print(item)

# Here i sort the data in ascending order using pythons inbuilt sort function
def sort_dataascending():
    random_numbers.sort(reverse=False)
# Here i sort the data in descending order using pythons inbuilt sort function
def sort_datadescending():
    random_numbers.sort(reverse=True)
# Here i have a function that adds a new number to the list
def add_Number(new):
    new = input("Please enter a number you would like to add to the list.")
    random_numbers.append(new)
#Here i have a function that removes a specific number from the list
def remove_Number(random_numbers):
    remove = int(input("Please enter a number you would like to remove from the list."))
    #Íterates through the list and removes the number if it is found
    for r in random_numbers:
        if r == remove:
            random_numbers.remove(remove)
# Here i have a function that removes the first number from the list
def remove_First(random_numbers):
    random_numbers.pop(0)
# Here i have a function that removes the last number from the list
def remove_Last(random_numbers):
    random_numbers.pop(-1)
# Here i have a function that sums all the numbers in the list using an inbuilt python function
def sum_numbers(random_numbers):
    total = sum(random_numbers) 
    print(total)


# Add more functions below

# Logic for your menu
while True:
    # This prompts the user to enter a choice. It converts it to an integer.
    user_choice = int(
        input("""
    1. Show all data in the list
    2. Sort the list in ascending order
    3. Sort the list in descending order
    4. Add a number
    5. Remove a specific number
    6. Remove the last number
    7. Remove the first number
    8. Sum all numbers 
    """)
    )
# Here is my menu where i call the functions based on the user inputs.
    if user_choice == 1:
        # Call function here (and remove the pass keyword)
        print("Here is the list of all randomly generated numbers:")
        show_data()
    elif user_choice == 2:
        # Call function here (and remove the pass keyword)
        print("Here is the sorted version of your list in ascending order.")
        sort_dataascending()
        show_data()
        
    elif user_choice == 3:
        # Call function here (and remove the pass keyword)
        print("Here is the sorted version of your list in descending order.")
        sort_datadescending()
        show_data()
    elif user_choice == 4:
        # Call function here (and remove the pass keyword)
        add_Number(random_numbers)
    elif user_choice == 5:
        remove_Number(random_numbers)
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 6:
        # Call function here (and remove the pass keyword)
        remove_First(random_numbers)
        pass
    elif user_choice == 7:
        # Call function here (and remove the pass keyword)
        remove_Last(random_numbers)
        pass
    elif user_choice == 8:
        # Call function here (and remove the pass keyword)
        sum_numbers(random_numbers)
        pass
    
