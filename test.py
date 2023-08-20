to_do_list = {"go shopping": ["milk", "eggs", "bread"], "call hospital": "MRI", "order birthday present": "book or tray"}

# for key in to_do_list.keys():
#     print(key)
    
# print(to_do_list.keys())

key = input("Which item would you like to update? ")
new_value = input("update the notes for this item. ")
to_do_list[key].append(new_value)

for key,value in to_do_list.items():
    print(key, ":", value)
