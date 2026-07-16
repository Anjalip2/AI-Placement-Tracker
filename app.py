from modules.menu import show_menu

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Student feature coming soon...")

    elif choice == "2":
        print("View Students feature coming soon...")

    elif choice == "3":
        print("Search Student feature coming soon...")

    elif choice == "4":
        print("Update Student feature coming soon...")

    elif choice == "5":
        print("Delete Student feature coming soon...")

    elif choice == "6":
        print("Thank you for using AI-Powered Student Placement Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")