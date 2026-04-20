
#-----------------------------book class ----------------------------------------
class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        self.is_available = True 
    
    def mark_as_borrowed(self): 
         self.is_available = False
    
    def mark_as_returned(self): 
       self.is_available = True

#-----------------------------User class ----------------------------------------
class User:
    def __init__(self, name):
        self.name = name 
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_available:
            return False, f"'{book.title}' is already borrowed."

        if book in self.borrowed_books:
            return False, f"You already have '{book.title}'."

        self.borrowed_books.append(book) 
        book.mark_as_borrowed()
        return True, f"Successfully borrowed '{book.title}'."
        
    def return_book(self, book): 
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.mark_as_returned()
            return True, f"'{book.title}' has been returned."
        return False, f"User does not have '{book.title}'."