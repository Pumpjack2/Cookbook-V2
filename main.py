# Importing packages. 
from time import sleep
import os

# Creating a variable so that when mentioned in the code it clears the terminal.
clear = lambda: os.system('cls')

# Defines what happens when CREATE is selected.
def create():
    # Defines the folder name for the entries to be stored.
    path = './cookBookRecipes'

    # When the code starts up.
    # Creates a folder for the recipes if a folder doesn't already exist. 
    try:
        # Makes a folder based of the path string.
        os.mkdir(path)

        # Print to the terminal that the path was created.
        print("Folder created!" + path)

    # Sends a message that a folder already exists to the terminal.
    except FileExistsError:

        # Prints to the terminal that the folder already exists.
        print(path + " already exists!")

    print("NOTE! Type 'done' when you have entered everything you've wanted for ingredients or instructions.")
    print("Enter a file name.")
    created_file = input()
    # Creates a file with the name the user gave.
    f=open("./cookBookRecipes/" + created_file + ".txt", "w")
    print("Congrats, you've created", (created_file), "!")
    print("Now let's add the needed ingredients.")
    ingredients = []
    while True:
        # Making each user input fall into add.
        add = input()
        # If the user types 'done' than the loop breaks
        if add.lower() == 'done':
            break
        # Appends each add to the ingredients string.
        ingredients.append(add)
    
    # Displays the current information of the recipe.
    print("""
|-------Ingredients-------|
""")

    print("\n".join(ingredients))
    print("This will be added to your", (created_file), "recipe.")
    clear()

    print("Now please write instructions to making", (created_file))
    instructions = []
    # Making each user input fall into instruction.
    while True:
        instruction = input()
        # If the user types clear than the loop breaks
        if instruction.lower() == 'done':
            break
        instructions.append(instruction)
    
    # Prints the Instructions for the user.
    print("""

|------Instructions------|
          
""")
    print("\n".join(instructions))
    print("This will be added to your", (created_file), "recipe.")
    clear()
    
    # Prints the final version of the recipe
    print("This is the final version")
    print("|-----",(created_file), "Recipe-----|")
    print("\n")
    print("Ingredients:")
    print("\n".join(ingredients))
    print("\n")
    print("Instructions:")
    print("\n".join(instructions))
    print("\n")
    sleep(3)
    # Converts the ingredents list to a string.
    convertedingred = map(str, ingredients)
    finalingred = '\n'.join(convertedingred)

    # Converts the instructions list to a string.
    convertedinstruc = map(str, instructions)
    finalinstruc = '\n'.join(convertedinstruc)

    # Writes everything to the recipe file.
    f.write("|----ingredients----|")
    f.write("\n")
    f.write(finalingred)
    f.write("\n")
    f.write("|----Instructions----|")
    f.write("\n")
    f.write(finalinstruc)
    f.close()

# Defines what happens when SEARCH is selected.
def search():

    print("What recipe would you like to search?")
    # Collects the search query from the user.
    searchQuery = input()
    clear()
    # Finds the recipe the user is looking for and displays it in the terminal.
    f = open("./cookBookRecipes/" + searchQuery + ".txt", "r")
    print(f.read())
    #Waits for user to type done.
    response = input()
    while True:
        # If the user enters done then the file closes and the loop breaks.
        if response.lower() == 'done':
            break
    f.close()
    sleep(1)

# Defines what happens when DELETE is selected.
def delete():

    print("what recipe would you like to remove?")
    # Collects the name of the file the user wants to delete.
    answer = input()
    # Prompts the user to confirm that they want to delete the file.
    print(f"Are you sure you want to delete {answer}?")
    # Collects the users decision.
    decision = input()
    if decision.lower() == 'yes':

        # If the file exist then the file is delete.
        if os.path.exists("./cookBookRecipes/" + answer + ".txt"):
            os.remove("./cookBookRecipes/" + answer + ".txt")
            return False
        # Otherwise prompts the user that the file doesn't exist.
        else:
            print("The file does not exist.")
    # If the decision is 'no' then the user is brought back to the menu page.
    if decision.lower() == 'no':
        sleep(1)
    
    # Informs the user that their is an error.
    else:
        print("""
              ERROR
              INVALID OPTION
              """)
        sleep(1)
        # Restarts the delete file process.
        delete()

# Creates a while loop that the user lands on once they have finished creating,searching or deleting a file.
while True:
    clear()
    print("Select what you wish to do.")
    print("[1] Create")
    print("[2] Search")
    print("[3] Delete")

    resp = input(">>> ")

    if resp == "1": create()
    if resp == "2": search()
    if resp == "3": delete()
