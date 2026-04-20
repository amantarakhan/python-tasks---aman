# main.py
from models import Book, User
from library import Library

my_library = Library()

def display_menu(): 
    print ("""
    --- Library Management System ---
    1. Add Book
    2. Register User
    3. Borrow Book
    4. Return Book
    5. Display Everything
    6. Search 
    7. Exit
    """)
    try: 
        return int(input("Select an option: "))
    except ValueError: 
        return 0

def add_book(): 
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    if not title or not author:
        print("❌ Error: Title and Author cannot be empty!")
        return
    
    success, message = my_library.add_book(Book(title, author))
    print(f"✅ {message}" if success else f"❌ {message}")

def register_user(): 
    name = input("Enter your name: ").strip()
    if not name:
        print("❌ Error: Name cannot be empty!")
        return
    
    success, message = my_library.register_user(User(name))
    print(f"✅ {message}" if success else f"❌ {message}")

def borrow_book(): 
    u_name = input("Enter your username: ").strip()
    b_title = input("Enter book title: ").strip()

    target_user = my_library.find_user(u_name)
    target_book = my_library.find_book(b_title)
    
    if target_user and target_book:
        # Fixed case-sensitivity: borrow_book instead of Borrow_book
        success, message = target_user.borrow_book(target_book)
        print(f"✅ {message}" if success else f"⚠️ {message}")
    else:
        print("❌ Error: User or Book not found.")

def return_book(): 
    u_name = input("Enter your username: ").strip()
    b_title = input("Enter the book title you are returning: ").strip()

    target_user = my_library.find_user(u_name)
    target_book = my_library.find_book(b_title)

    if target_user and target_book:
        success, message = target_user.return_book(target_book)
        print(f"✅ {message}" if success else f"⚠️ {message}")
    else:
        print("❌ Error: Could not find that user or book.")

def display_everything():
    print("\n--- Current Library Status ---")
    print(my_library.display_all_books())
    
    print("\n--- Registered Users ---")
    print(my_library.display_all_users())

def search():
    title = input("Enter the title you are looking for: ").strip()
    book = my_library.find_book(title)
    
    if book:
        status = "Available" if book.is_available else "Borrowed"
        print(f"🔍 Found: '{book.title}' by {book.author} | Status: {status}")
    else:
        print(f"❌ Sorry, '{title}' was not found.")

# Main Loop
while True: 
    choice = display_menu()
    match choice:
        case 1: add_book()
        case 2: register_user()
        case 3: borrow_book()
        case 4: return_book()
        case 5:
            print("\n--- Books ---")
            print(my_library.display_all_books())
            print("\n--- Users ---")
            print(my_library.display_all_users())
        case 6:
            title = input("Search Title: ").strip()
            book = my_library.find_book(title)
            print(f"Found: {book.title} ({'Available' if book.is_available else 'Borrowed'})" if book else "❌ Not found.")
        case 7:
            print("Goodbye!")
            break
        case _:
            print("Invalid selection. Try again.")