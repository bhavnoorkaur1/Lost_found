def report_found(found_items):
    print("\n REPORT FOUND ITEM ")

    name = input("Enter your name: ")
    item = input("Enter found item name: ")
    place = input("Where did you find it? ")
    lost_when = input("Enter date when found(DD-MM-YYYY): ")
    description = input("Enter item description: ")

    found_item = {
        "name": name,
        "item": item,
        "location": place,
        "date": lost_when,
        "description": description
    }

    found_items.append(found_item)

    print("\nSuccessfully reported found item")
    print("Thank you for reporting")