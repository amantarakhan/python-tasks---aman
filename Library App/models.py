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
        if (book.is_available == True) : 
            self.borrowed_books.append(book) 
            book.mark_as_borrowed()
        else : print ("the book is already out")
        
    def return_book (self , book ) : 
        if book in self.borrowed_books  :
            self.borrowed_books.remove(book)
            book.mark_as_returned()