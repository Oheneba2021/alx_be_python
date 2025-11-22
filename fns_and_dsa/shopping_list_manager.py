def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        choice = str(choice).strip()
        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter the name of item to add:").strip()
            if not add_item.strip():
                print("Sorry! Space cannot be empty")
            else:    
                shopping_list.append(add_item)
                print(f"{add_item} successfully added to cart")
            # for item in shopping_list:
            #     print(f"- {item}")
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the name of item to remove:").strip()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} successfully removed from cart")
            else:
                print(f"{remove_item} not found in the shopping list.")
            # 
            pass
        elif choice == '3':
            # Display the shopping list
            print("Your Shopping List:")
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                for item in shopping_list:
                    print(f"- {item}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def new_func():
    pass

if __name__ == "__main__":
    main()