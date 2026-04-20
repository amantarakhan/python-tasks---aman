
from models import Book, User    
#-----------------------------Library class ----------------------------------------
class Library : 
    def __init__(self):
        self.books = []
        self.users = []


    def add_book (self , book ) :
        # Check if book title already exists (Case Insensitive)
        if self.find_book(book.title):
            print(f"Error: A book with the title '{book.title}' already exists.")
        else:
            self.books.append(book) 
            print(f"Book '{book.title}' added to library catalog.")


    def register_user (self , user) : 
        # Prevent duplicate usernames
        if self.find_user(user.name):
            print(f"Error: Username '{user.name}' is already taken.")
        else:
            self.users.append(user)
            print(f"User '{user.name}' registered successfully.")


    def display_all_books(self):
        if not self.books:
            print("The library is currently empty.")
            return
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")


    def display_all_users(self):
        if not self.users:
            print("No users registered yet.")
            return
        for user in self.users:
            titles = [book.title for book in user.borrowed_books]
            print(f"User: {user.name} | Borrowed: {titles if titles else 'None'}")
       

# helper functions for the case 3 
    def find_book(self, title) : 
        for book in self.books: 
            if book.title.lower() == title.lower() : 
                return book
            return None 
            
    def find_user(self, name) : 
        for user in self.users: 
            if user.name.lower() == name.lower() : 
                return user
            return None 




