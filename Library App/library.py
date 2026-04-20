
from models import Book, User    

class Library: 
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        if self.find_book(book.title):
            return False, f"Error: A book with the title '{book.title}' already exists."
        
        self.books.append(book) 
        return True, f"Book '{book.title}' added to library catalog."
    
    def register_user(self, user):
        if self.find_user(user.name):
            return False, f"Error: Username '{user.name}' is already taken."
        
        self.users.append(user)
        return True, f"User '{user.name}' registered successfully."

    def display_all_books(self):
        if not self.books:
            return "The library is currently empty."
        
        output = []
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            output.append(f"Title: {book.title} | Author: {book.author} | Status: {status}")
        return "\n".join(output)

    def display_all_users(self):
        if not self.users:
            return "No users registered yet."
        
        output = []
        for user in self.users:
            titles = [book.title for book in user.borrowed_books]
            borrowed_str = ", ".join(titles) if titles else "None"
            output.append(f"User: {user.name} | Borrowed: {borrowed_str}")
        return "\n".join(output)

    # Fixed Helper Functions (Loops now finish before returning None)
    def find_book(self, title): 
        for book in self.books: 
            if book.title.lower() == title.lower(): 
                return book
        return None 
            
    def find_user(self, name): 
        for user in self.users: 
            if user.name.lower() == name.lower(): 
                return user
        return None