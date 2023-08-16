# TO DO LIST
# print multistring list of actions that can be done within to do list
def print_content_manager(exit):
    if exit == False:
        print("""TO DO LIST OPTIONS
              PLEASE SELECT AN ACTION
              1. Add an item to your To Do List
              2. Read an item on your To Do List
              3. update an item on your To Do List
              4. Delete and item from your To Do List
              5. Print your entire To Do List
              6. Exit To Do List""")
        action = print("Which action would you like to perform? Type the relevant number.")
        return int(action)

# create new item on to do list
def create_item(to_do_list):
    new_item_key = input("What is the title of your new list item? ")
    are_notes_needed = input("Would you like to add notes to this to do list item? Y or N.")
    if are_notes_needed == "Y":
        new_item_value = input("Type the notes that you would like to include for this to do list item.")
    
    to_do_list[new_item_key] = new_item_value

# read an iten from to do list
def read_item(to_do_list, index):
    print(to_do_list(index))

# update item on to do list
def update_item(to_do_list, index):
    print()

# delete item from to do list
def delete_item(to_do_list):


# print entire to do list
def print_entire_list(to_do_list):
    print(to_do_list)

print_list()

# exit to do list
def exit_to_do_list(exit):
    exit = True
    print("""Exiting...
          To Do List Finished.""")
    
# set up loop for continually printing content manager until exit function is executed
def run_to_do_list():
    to_do_list = {"Go shopping": ["milk", "eggs", "bread"]}
    exit = False
    while exit == False:
        action_required = print_content_manager()
