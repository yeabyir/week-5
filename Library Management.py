class Book:
    def __init__(self,title,author,ISBN,availability_status):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.availability_status=availability_status
        print(f"Title: {self.title}\n Author: {self.author}\nISBN: {self.ISBN}\nAvailability_Status:{self.availability_status}")
    def book_details(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"ISBN:{self.ISBN}")
    def update_availability_status(self):
        print(f"Availability_Status:{self.availability_status}")
        
class User:
    def __init__(self,name,user_id,books_borrowed):
        self.name=name
        self.user_id=user_id
        self.books_borrowed=books_borrowed
        print(f"Name:{self.name}\nuser_id:{self.user_id}\nBooks_borrowed:{self.books_borrowed}")
    def display_user_details(self):
        print(f"Name:{self.name}")
        print(f"User_id:{self.user_id}")
    def borrowing_books(self):
        print(f"Book_borrowed:{self.books_borrowed}")
    def returning_books(self):    
        print(f"Book_returned:{self.returning_books}") 

class Library:
    def __init__(self,new_book,new_user,handling_book):
        self.new_book=new_book
        self.new_user=new_user
        self.handling_book=handling_book
        print(f"New_book:{self.new_book}\nNew_user:{self.new_user}\nHandling_book:{self.handling_book}")
    def adding_books(self):
        print(f"New_books:{self.new_book}")
        print(f"Handling book:{self.handling_book}")
    def registering_new_users(self):    
        print(f"New Users:{self.new_user}")
class Transaction:
    def __init__(self,borrowing,returning):
        self.borrowing=borrowing
        self.returning=returning
        print(f"Borrowing:{self.borrowing}\nReturning:{self.returning}")
    def recording_transactions(self, borrowing, returning):
        self.borrowing = borrowing
        self.returning = returning
    def generate_transaction_report(self):
        print(f"Recording Transaction: Borrowing: {self.borrowing}, Returning: {self.returning}")

    