import main


shopping_list=[]
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")


def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else :
        print(f"{item} is not in the list.")


def view_list():
    print("Current Shopping List:")
    for item in shopping_list:
        print(item)

        
while True:
    display_menu()
    choise = input("Enter your choice (1-4): ")
    if choise == "1":
        add_item()
    elif choise =="2":
        remove_item()
    elif choise =="3":
        view_list()
    elif choise =="4":
        print("Exiting the Shopping List Manager. Goodbye!")
        break
    else :
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    'main.main(...)'