from lost_item import report_lost
from found_item import report_found
from search import search_item
from claim import claim_item


lost_items = []
found_items = []


def display_menu():
    print("\n")
    print("LOST AND FOUND SYSTEM")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. Search Item")
    print("4. Claim Item")
    print("5. Exit")



while True:

    display_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        report_lost(lost_items)

    elif choice == "2":
        report_found(found_items)

    elif choice == "3":
        search_item(lost_items, found_items)

    elif choice == "4":
        claim_item(found_items)

    elif choice == "5":
        print("\nThank you for using this model")
        break

    else:
        print("\nInvalid")
        print("Please enter a number between 1 and 5")