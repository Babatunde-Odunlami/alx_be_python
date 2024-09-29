# create a program that will manage a shopping list
# create a default function to display doaable actions
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """A function to manage/alter a shopping list"""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(item)
            pass
        elif choice == "2":
            item = input("Enter the item to remove: ").strip().lower()
            shopping_list.remove(item)
            pass
        elif choice == "3":
            print(f"The shopping list contains: {shopping_list}")
            pass
        elif choice == "4":
            print("Goodbye !")
            break
        else:
            print("Invalid choice. Please try again.")


main()
