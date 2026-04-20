#-----------------------------book class ----------------------------------------

class Book : 
    # a constructor 
    def __init__(self, title, author  ):
        self.title = title
        self.author = author 
        self.is_available = True # defult state 
    

     
    def mark_as_borrowed(self): 
         self.is_available = False
    
    def mark_as_returned(self): 
       self.is_available = True

#-----------------------------User class ----------------------------------------

class User : 
    def __init__ (self , name) : 
        self.name = name 
        self.borrowed_books = []

    def Borrow_book (self , book ):
        # Validation 1: Check if the book is physically available
        if not book.is_available:
            print(f"Error: '{book.title}' is already borrowed by someone else.")
            return

        # Validation 2: Check if this specific user already has a reference to this book
        if book in self.borrowed_books:
            print(f"Error: You already have '{book.title}' in your collection.")
            return

        # If passed, add the reference and update the book object
        self.borrowed_books.append(book) 
        book.mark_as_borrowed()
        print(f"Success: {self.name} has borrowed '{book.title}'.")
        
    def return_book (self , book ) : 
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.mark_as_returned()
            print(f"Success: '{book.title}' has been returned.")
        else:
            print(f"Error: {self.name} does not have '{book.title}' in their borrowed list.")