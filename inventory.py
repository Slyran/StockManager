class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        Creates a new Shoe object.

        :param country: 
        :param code: The code of the shoe.
        :param product: The name of the shoe.
        :param cost: The cost of the shoe.
        :param quantity: The quantity of the shoe.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Returns the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Returns the quantity of the shoe.
        '''
        return self.quantity

    def __str__(self):
        '''
        Returns a string representation of a class.
        '''
        return f"\nProduct: {self.product}\nCountry: {self.country}\nCode: {self.code}\nCost: {self.cost}\nStock: {self.quantity}"



# The list will be used to store shoe objects.
shoe_list = []

def read_shoes_data():
    '''
    Reads the data from inventory.txt and creates a list of shoe objects.
    '''
    try:
        # inventory.txt format should be: Country,Code,Product,Cost,Quantity
        with open("inventory.txt", "r") as file:
            file_lines = file.readlines()
        for line in file_lines[1:]: # Skips the first line to ignore the header
            line = line.strip("\n")
            line = line.split(",")
            try:
                shoe_list.append(Shoe(line[0], line[1], line[2], float(line[3]), int(line[4])))
            except {IndexError, ValueError}:
                print("\n\33[31mError: Incompatible data format, shoe was not added to the list\33[0m\n")
    except FileNotFoundError:
        print("\n\33[31mError: Could not find file: 'inventory.txt'\33[0m\n")
        return
    
def save_to_file():
    '''
    Saves the current shoe list to inventory.txt
    '''
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity") # Adds header to beginning of file
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    except FileNotFoundError:
        print("\n\33[31mError: File not found. Could not update inventory.txt\33[0m\n")
        return


def capture_shoes():
    '''
    Gets the data from the user and creates a shoe object.
    '''
    try:
        country = input("Enter the country of origin: ")
        code = input("Enter the code of the shoe: ")
        product = input("Enter the name of the shoe: ")
        cost = float(input("Enter the cost of the shoe: "))
        quantity = int(input("Enter the quantity of the shoe: "))
    except ValueError:
        print("\n\33[31mError: Invalid input, shoe cost and quantity must both be numbers.\33[0m\n")
        return
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    save = input("Would you like to save this shoe to the inventory.txt file? y/n\n")
    if save == "y":
        save_to_file()
 

def view_all():
    '''
    Prints every object in the shoe list.
    '''

    for shoe in shoe_list:
        print(shoe)
 

def re_stock():
    '''
    Prints the lowest quantity shoe and prompts the user to restock.
    '''
    
    lowest_quantity = min(shoe_list, key=lambda x:x.quantity)
    print(f"The shoe with the lowest quantity is {lowest_quantity.product}, with a quantity of {lowest_quantity.quantity}\n")

    while True:
        # Gets the user to input how many shoes to restock
        try:
            user_choice = int(input("How many shoes would you like to add to the stock? "))
            if user_choice < 0:
                "\n\33[31mError: Number must be positive."
                continue
            break
        except ValueError:
            print("\n\33[31mError: Please enter a number. Enter 0 to continue without adding stock.\33[0m\n")

    # Stores the restocked shoe quantity in the inventory.txt file
    lowest_quantity.quantity += user_choice
    save_to_file()

def seach_shoe():
    '''
    Gets a product name from the user, then returns the matching shoe object.
    '''
    
    print("Enter the name of a product to display it's details. Product names are case sensitive.")
    shoe_selection = input("Search: ")

    for shoe in shoe_list:
        if shoe_selection == shoe.product:
            return shoe
    print("\n\33[31mError: Product not found.\33[0m\n")


def value_per_item():
    '''
    Displays the total stock value for each shoe.
    '''

    print("\33[4mTotal stock values\33[0m")
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: R{value}.")
 

def highest_qty():
    '''
    Finds and prints the highest quantity shoe, and announces that it is on sale.
    '''
    
    highest_quantity = max(shoe_list, key=lambda x:x.quantity)
    print(f"The shoe with the highest quantity is {highest_quantity.product}, with a quantity of {highest_quantity.quantity}")
    print(f"\33[32m{highest_quantity.product} are on sale!\33[0m")
    


menu = f"""
{"―"*20}Main Menu{"―"*20}
a - Add a shoe
v - View all shoes
r - View the lowest quantity shoe and restock it
s - Search for a shoe and display it's data
sv - View the total Stock Value for each shoe
h - Displays the highest quantity shoe
e - Exit program
{"―"*49}
"""

while True:
    print(menu)
    selection = input("Enter selection: ").strip().lower()
    print("")

    read_shoes_data()

    if selection == "a":
        capture_shoes()

    elif selection == "v":
        view_all()

    elif selection == "r":
        re_stock()

    elif selection == "s":
        print(seach_shoe())

    elif selection == "sv":
        value_per_item()

    elif selection == "h":
        highest_qty()

    elif selection == "e":
        break

    else:
        print("\n\33[31mError: Invalid input, please try again\33[0m\n")
