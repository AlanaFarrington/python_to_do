# TO DO LIST
# print multistring list of actions that can be done within to do list
def print_content_manager():
    print("""

                        TO DO LIST OPTIONS
        ----------------------------------------------------
        | PLEASE SELECT AN ACTION                          |
        | 1. Add an item to your To Do List                |
        | 2. Read your To Do List                          |
        | 3. Update an item on your To Do List             |
        | 4. Delete and item from your To Do List          |
        | 5. Print all items on your To Do List            |
        | 6. Print all items and notes on your To Do List  |
        | 7. Exit To Do List                               |
        ----------------------------------------------------
          
          """)
    return input("Which action would you like to perform? Type the relevant number. \n")

def validate_action(action):
    return action.isnumeric() and (action > '0' and action < '8')
    
def convert_action_to_int(action):
    return int(action)

# create new item on to do list
def create_item(to_do_list):
    new_item_key = input("What is the title of your new list item? \n")
    are_notes_needed = input("Would you like to add notes to this to do list item? Y or N.\n")
    if (are_notes_needed == "Y") or (are_notes_needed == "y"):
        new_item_value = input("Type the notes that you would like to include for this to do list item.\n")
        to_do_list[new_item_key] = new_item_value
    else:
        to_do_list[new_item_key] = ""

# read an iten from to do list
def read_items(to_do_list):
    what_to_read = input("Would you like to read all of the associated notes for your list items?\n Y or N. \n")
    if (what_to_read == "Y") or (what_to_read == "y"):
        print(to_do_list.items())
    elif (what_to_read == "N") or (what_to_read == "n"):
        print(to_do_list.keys())
    else:
        print("invalid input")

# update item on to do list
def update_item(to_do_list):
    key = input("Which item would you like to update? ")
    new_value = input("update the notes for this item. ")
    to_do_list[key] = new_value

# delete item from to do list
def delete_item(to_do_list):
    key = input("which item do you want to delete from the list? ")
    del to_do_list[key]

# print entire to do list
def print_keys(to_do_list):
    print(to_do_list.keys())

def print_entire_list(to_do_list):
    print(to_do_list.items())

# exit to do list
def exit_to_do_list():
    print("""
Exiting...
          
To Do List Finished.
          
Goodbye!
          """)
    return True
    
# set up loop for continually printing content manager until exit function is executed
def run_to_do_list():
    to_do_list = {"Go shopping": ["milk", "eggs", "bread"]}
    exit = False
    while exit == False:
        user_action_str = print_content_manager()
        if validate_action(user_action_str) == False:
            print("invalid selection. Choose a number between 1 and 7. ")
            continue

        # convert user input to int
        action_selected = convert_action_to_int(user_action_str)

        # match case for given action
        if action_selected != 7:
            match action_selected:
                case 1:
                    create_item(to_do_list)
                case 2:
                    read_items(to_do_list)
                case 3:
                    print("you would like to update an item")
                    update_item(to_do_list)
                case 4:
                    print("you would like to delete")
                    delete_item(to_do_list)
                case 5:
                    print("you would like to print all items")
                    print_keys(to_do_list)
                case 6:
                    print("you would like to print items and notes")
                    print_entire_list(to_do_list)
                case _:
                    print("invalid choice")
        else:
            exit = exit_to_do_list()
            break

run_to_do_list()