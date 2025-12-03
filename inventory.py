'''
Assignment 23
==========================================================
Create and Inventory Search program in Python.
Use object-oriented programming. 

'''

# --->> Step 1: Read the inventory
# ========================================================

inventory = open("inventory.txt", "r")


# --->> Step 2: Define the class
# ========================================================

# Create a class named Shoe

class Shoe:

    # Define attributes of Shoe

    def __init__(self, country, code, product, cost, quantity):

        # Initialize attributes of Shoe

        self.country = country 
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


# --->> Step 3: Set up methods
# ========================================================

    # METHOD 1: Return cost of a Shoe
    
    def get_cost(self):
        return self.cost
    
#---------------------------------------------------------
 
    # METHOD 2: Return quantity of a Shoe
   
    def get_quantity(self):
        return self.quantity
    
#---------------------------------------------------------

    # METHOD 3: Return a string representation of a Shoe

    def __str__(self):
        return f"""\n
            SHOE INFORMATION
            Code: {self.code}
            Country: {self.country}
            Product: {self.product}
            Cost: {self.cost}
            Quantity: {self.quantity}
                """
    
#---------------------------------------------------------

# --->> Step 4: Create list to store shoe objects
# ========================================================

shoes_list = []


# --->> Step 5: Define functions to get information on shoes
# ========================================================


# FUNCTION 1: Copy inventory to shoes_list and reads

def read_shoes_data(shoes_list):

    # Try to open and clean file
    try: 
        
        # Open inventory 
        with open("inventory.txt", "r") as inventory: 

            # Skip headings in list 
            next(inventory) 

            # Read each line after the headings 
            for index, line in enumerate(inventory, start=2): 

                # Remove whitespace to prevent code break
                line = line.strip()  

                # Continue past empty lines if found
                if not line: 
                    continue 

                # Try adding shoes to the list 
                try: 

                    # First, break each line into the correct parts
                    country, code, product, cost, quantity = line.split(",") 

                    # Second, add parts to the list as a Shoe object
                    shoes_list.append(Shoe(country, code, product, cost, quantity)) 

                # If a line is empty throw error
                except ValueError: 
                    print(f"""
            Skipped invalid line {index}: {line}
                        """) 

    # If file is not found throw error
    except FileNotFoundError: 
        print("""
            Could not find file
              """)

    # Return the updated shoes list 
    return shoes_list 

read_shoes_data(shoes_list)

#---------------------------------------------------------


# FUNCTION 2: Add new shoes to list

def capture_shoes(country, code, product, cost, quantity): 

    # Save shoe attributes as an object 
    new_shoe = Shoe(country, code, product, cost, quantity) 
    
    # Add new shoe object to list 
    shoes_list.append(new_shoe) 
    
    # Confirm new show was added to list 
    return print(f"""\n
            NEW SHOE ADDED:
            ------------------------- 
            {new_shoe}""") 

#---------------------------------------------------------


# FUNCTION 3: Print table of all shoes

from tabulate import tabulate # Import tabulate to make table

def view_all(shoes_list): # Input list     

    # Create empty table and identify headers
    table = [] 
    headers = ["Country", "Code", "Product", "Cost", "Quantity"] 

    # Loop through shoe list 
    for shoe in shoes_list: 

        # Identify components of each row
        row = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]

        # Add each row to the table 
        table.append(row) 

    # Use tabulate to format a table with the content from shoes_list    
    return print(tabulate(table, headers=headers, tablefmt="grid"))

#---------------------------------------------------------


# FUNCTION 4: Find lowest stock and restock 

def re_stock(shoes_list):

    # Find the lowest stock shoe 
    # Use lambda to tell min() to look only at index 4
    lowest_stock = min(shoes_list, key=lambda shoe: int(shoe.quantity))
    lowest_stock.quantity = int(lowest_stock.quantity)

    # Tell user which shoe has lowest stock
    print(f"""\n
            LOWEST STOCK ITEM:
            ------------------------- 
            Code: {lowest_stock.code}
            Product: {lowest_stock.product}
            Quantity: {lowest_stock.quantity}""")
    
    # Ask user if they would like to re-stock  
    try: 
        add_stock = int(input("""\n
            Do you want to add to stock?
            If yes, enter quantity, 
            If no, enter 0.
            Insert number here: """))

        # Update the stock amount in the shoes list (make sure to add integers together)
        if add_stock > 0:
            lowest_stock.quantity = int(lowest_stock.quantity) + add_stock

            # Show the user the updated stock amount
            print(f"""\n
            STOCK UPDATED:
            -------------------------
            Stock for {lowest_stock.code}, {lowest_stock.product} is now {lowest_stock.quantity}.""")

        # If user entered 0, tell them no changes made
        else: 
            print("""\n
            No changes made to stock.""")

    # If incorrect value entered, tell user to try again
    except ValueError:
        print("""
            Invalid input. Please try again.""")

    # Return the updated shoes_list
    return shoes_list 

#---------------------------------------------------------


# FUNCTION 5: Search shoes and print result 

def search_shoe(shoes_list, code):
    
     # Loop through shoe list 
    for shoe in shoes_list:

        # If the input code matches the shoe code
        if shoe.code == code:

            # Return details about the shoe
            return print(f"""\n
            SHOE FOUND:
            -------------------------
            {shoe}""")
        
    # If shoe not found, print error    
    print("""\n
            No shoe found. Try again. """)
            
#---------------------------------------------------------


# FUNCTION 6: Print total value of a shoe  

def value_per_item(shoes_list, code):
    
     # Loop through shoe list 
    for shoe in shoes_list: 

        # If the input code matches the shoe code
        if shoe.code == code:

            # Calculate the value
            cost = int(shoe.cost)
            quantity = int(shoe.quantity)
            value = cost * quantity

            # Return shoe value
            return print(f"""\n
            TOTAL STOCK VALUE for {shoe.product}:
            -------------------------
            ${value}""")
    
    # If shoe not found, print error
    print("""\n
            No shoe found. Try again.""")

#---------------------------------------------------------


# FUNCTION 7: Determine highest quantity and print for sale  

def highest_qty(shoes_list):

    # Find the highest stock shoe 
    # Use lambda to tell max() to look only at index 4
    highest_stock = max(shoes_list, key=lambda shoe: int(shoe.quantity))
    highest_stock.quantity = int(highest_stock.quantity)

    # Tell user the highest stock shoe is on sale
    print(f"""
            SHOE ON **SALE**
            -------------------------
            {highest_stock.product} is on sale.
            There are {highest_stock.quantity} in stock.""")

#---------------------------------------------------------


#--->> Step 6: Create main menu
# ========================================================


# ==========Main Menu=============

def view_menu(shoes_list):

    while True:
        print("""\n
              ==========Shoe Inventory Menu=============
              1. View all shoes in inventory 
              2. Add new shoes to inventory 
              3. Restock lowest stock shoe
              4. Search for a shoe
              5. Find the total value of a shoe 
              6. See which shoe is on sale 
              7. Exit menu""")
        
        choice = input("""\n
            -----Hello! What would you like to do? 
            -----Choose number from 1-7.
            -----Insert here: """)

        if choice == "1":
            print("""\n
            -----You want to see the inventory! 
            -----Here it is:""")
            view_all(shoes_list)

        elif choice == "2":
            new_shoe = input("""\n
            -----You want to add a shoe!
            -----Please provide country, code, product, cost, quantity of shoe (comma separated).
            -----Insert here:  """)

            country, code, product, cost, quantity = [element.strip() for element in new_shoe.split(",")]
            
            capture_shoes(country, code, product, cost, quantity)

        elif choice == "3": 
            print("""\n
            -----You want to see the lowest stock!""")
            
            re_stock(shoes_list)

        elif choice == "4": 
            code = input("""\n
            -----You want to find a shoe!
            -----To find shoe, enter shoe code here: """)
            
            search_shoe(shoes_list, code)

        elif choice == "5": 
            code = input("""\n
            -----You want to find a value! 
            -----To find value of shoe, enter shoe code here: """)
            
            value_per_item(shoes_list, code)

        elif choice == "6":
             print("""\n
            -----You want to see what's on sale!""")
             
             highest_qty(shoes_list)
        
        elif choice == "7":
            print("""\n
            -----Leaving menu. Goodbye!""")
            
            break
        
        else: 
            print("""\n
            *****Invalid input. Please try again.""")


view_menu(shoes_list)
