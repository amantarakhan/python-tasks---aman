
from models import Book, User
from library import Library
#----------------------------  CLI library system  ----------------------------------------

def display_menu () : 
    user_choice = 0 
    print ("""
    Library manmagemnt system 
    1. Add Book
    2. Register User
    3. Borrow Book
    4. Return Book
    5. Display Everything
    6. Search 
    7. Exit
           """)
    try: 
        user_choice = int(input("Select an option: "))
    except ValueError: 
        print("Invalid input! Please enter a number from [1-7]")
        
    return user_choice


def add_book(): 
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    new_book = Book(title, author)
    my_library.add_book(new_book)
    print(f"Successfully added '{title}' to the library!")


def register_user() : 
    name = input("Enter Your name : ")
    new_user = User(name)
    my_library.register_user(new_user)
    print(f"User '{name}' has been registered successfully!")

def borrow_book(): 
    b_title = input("Enter book title you want to borrow : ")
    u_name = input("Enter your username : ")

    #Convert strings to objects using your Library helpers
    target_user = my_library.find_user(u_name)
    target_book = my_library.find_book(b_title)
    
    if target_user and target_book:
        target_user.Borrow_book(target_book) 
        print(f"{u_name} successfully borrowed {b_title}")
    else:
        print("Error: User or Book not found in system.")

def return_book() : 
    u_name = input("Enter your username: ")
    b_title = input("Enter the book title you are returning: ")

    target_user = my_library.find_user(u_name)
    target_book = my_library.find_book(b_title)

    if target_user and target_book:
        # This calls the method in your User class to update the list and book status
        target_user.return_book(target_book)
        print(f"Success: {u_name} returned '{b_title}'.")
    else:
        print("Error: Could not find that user or book in our records.")


def display_everything():
    print("\n--- Current Library Status ---")
    my_library.display_all_books() #this function us defined in the user class
    
    print("\n--- Registered Users ---")
    my_library.display_all_users() #this function us defined in the user class


def search():
    title = input("Enter the title you are looking for: ")
    book = my_library.find_book(title)
    
    if book:
        status = "Available" if book.is_available else "Borrowed"
        print(f"Found: '{book.title}' by {book.author} | Status: {status}")
    else:
        print(f"Sorry, '{title}' was not found in our collection.")


my_library = Library()
while (True) : 
    choice = display_menu()
    match choice : 
        case 7 : 
            break 
        case 1 : 
            add_book() 
        case 2 : 
            register_user()
        case 3 : 
            borrow_book()
        case 4 :
            return_book() 
        case 5 :
            display_everything()
        case 6 :
            search() 


