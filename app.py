from modules.menu import show_menu
from modules.student import add_student, view_students, search_student, update_student, delete_student

while True:
    choice=show_menu()
    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        print("Thank you.")
        break
    else:
        print("Invalid choice")