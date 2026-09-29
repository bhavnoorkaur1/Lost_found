def claim_item(found_items):
    print("\nCLAIM ITEM ")

    if len(found_items) == 0:
        print("There are no found items")
        return

    search = input("Enter the name of the item you want to claim: ").lower()

    found = False

    for item in found_items:
        if search in item["item"].lower():

            print("\nMatch found")
            print("Item:", item["item"])
            print("Place:", item["location"])
            print("Lost_when:", item["date"])
            print("Description:", item["description"])

            answer = input("\nIs this your item? (yes/no): ").lower()

            if answer == "yes":
                print("\nSuccessfully submitted claim")
                print("Contact the person who found the item")
            else:
                print("\nItem was not claimed")

            found = True
            break

    if not found:
        print("\nNo valid match found")