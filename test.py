to_do_list = {"Go shopping": ["milk", "eggs", "bread"], "call hospital": "Ask about headaches and if next MRI will have contrast"}

print(to_do_list.keys())
print(to_do_list.items())

def create_item(to_do_list):
    new_item_key = input("What is the title of your new list item? ")
    are_notes_needed = input("Would you like to add notes to this to do list item? Y or N.")
    if are_notes_needed == "Y":
        new_item_value = input("Type the notes that you would like to include for this to do list item.")
        to_do_list[new_item_key] = new_item_value
    else:
        to_do_list[new_item_key] = ""

create_item(to_do_list)
print(to_do_list)

del to_do_list["call hospital"]
print(to_do_list)