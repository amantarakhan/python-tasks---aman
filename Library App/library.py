
from models import Book, User    
#-----------------------------Library class ----------------------------------------
class Library : 
    def __init__(self):
        self.books = []
        self.users = []

    def add_book (self , book ) :
        self.books.append(book) 

    def register_user (self , user) : 
        self.users.append(user)

    def display_all_books(self):
        for book in self.books:
        # Check the status of the book object
            status = "Available" if book.is_available else "Borrowed"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

    def display_all_users(self):
        for user in self.users:
        #  create a simple list of titles so it's readable for humans
            titles = [book.title for book in user.borrowed_books] # grab only the borrowed books titiles 
            print(f"Name: {user.name} | Borrowed Books: {titles}")


# helper functions for the case 3 
    def find_book(self, title) : 
        for book in self.books: 
            if book.title.lower() == title.lower() : 
                return book
            
    def find_user(self, name) : 
        for user in self.users: 
            if user.name.lower() == name.lower() : 
                return user




