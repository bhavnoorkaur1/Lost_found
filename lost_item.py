def report_lost(lost_items):
    print("\n REPORT LOST ITEM")

    name = input("Enter your name: ")
    item = input("Enter lost item name: ")
    place = input("Where did you lose it? ")
    lost_when = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter item description: ")

    lost_item = {
        "name": name,
        "item": item,
        "location": place,
        "date": lost_when,
        "description": description
    }

    lost_items.append(lost_item)

    print("\Successfully reported lost item")
    print("Your item has been added to the list of lost")