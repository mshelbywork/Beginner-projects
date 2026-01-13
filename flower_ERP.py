#item lookup
#add item
#add batch
#search
    #flower type, color, expiration, reorder threshhold
#view
    #flower type (metadata), color, expiration, reorder threshhold, batch info, loss info,
    #order info,
#create reports
inventory = {}

def add_item():
    num_items = int(input("How many new entries?"))
    type = input ('Enter item type: ')
    for items in range (num_items):
        print (f'enter info for item {items+1}')
        item_id = input("Item ID: ")
        name = input("Name: ")

        tags = input("Tags (comma separated): ").split(",")  # convert string to list
        low_inventory_threshold = int(input("Low inventory threshold: "))

        item = {
            "item_id": item_id,
            "name": name,
            "category": type,
            "tags": [tag.strip() for tag in tags],  # clean spaces
            "low_inventory_threshold": low_inventory_threshold
         }
        inventory[item_id] = item  # store inventory by item id
    return
add_item()
for item_id, item in inventory.items():
    print(f"""
Item ID: {item["item_id"]}
Name: {item["name"]}
Category: {item["category"]}
Tags: {", ".join(item["tags"])}
Low Inventory Threshold: {item["low_inventory_threshold"]}
""")
