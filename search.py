def search_item(lost_items, found_items):
    print("\n SEARCH ITEM ")

    search = input("Enter item name: ").lower()

    found = False

    for item in lost_items:
        if item[1].lower() == search:
            print("\nLost Item Found:")
            print("Reported by:", item[0])
            print("Place:", item[2])
            print("Lost_when:", item[3])
            print("Description:", item[4])
            found = True

    for item in found_items:
        if item[1].lower() == search:
            print("\nFound Item:")
            print("Reported by:", item[0])
            print("Place:", item[2])
            print("Lost_when:", item[3])
            print("Description:", item[4])
            found = True

    if found == False:
        print("No item found")