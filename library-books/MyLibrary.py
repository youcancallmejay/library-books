import csv

def main():

    class Book:
        def __init__(self, book_name, author) -> None:
            self.book_name = book_name
            self.author = author
            self.book_status = True           
    
        def borrow(self):
            if self.book_status == True:
                self.set_status(); 
                return True
            else:
                print("Book is unavailable")

        def return_book(self):
            self.book_status = True

        def is_available(self):
            if self.book_status != True:
                print("Book not available")
                return False
            else: 
                print("Book available")
        
        def set_status(self):
            self.book_status = False

            
    books = []
    #breakpoint()
    with open("short_list_books.csv") as booklist: 
        file_reader = csv.DictReader(booklist)
        for book in file_reader: 
            new_book = Book(book.get('title'.lower(), ''), book.get('author', '')) 
            books.append(new_book)

    print("Welcome to the library!")
    your_selection = ""
    while your_selection != 'exit':
        your_selection = input("Would you like to '1' View Book list, '2' Borrow a book, '3' Return a book, or 'exit'? ") 

        if your_selection == '1':
            for book in books: 
                print(book.book_name, "by", book.author, end=", ")
                if book.book_status == True:
                    print("Available")
                else:
                    print("Unavailable")

        elif your_selection == '2':    
            your_request = input("What book would you like to checkout?: ")
            for book in books:
                if book.book_name.lower() == your_request.lower():
                    book.borrow()
                

        elif your_selection == '3':
            your_return = input("What book are you returning?: ")
            for book in books: 
                if book.book_name.lower() == your_return.lower():
                    book.return_book()
                
        elif your_selection == 'exit':
            print("Thank you and goodbye")
        
        else:
            print("Please enter a valid response: 1, 2, 3, or exit: ")        


main()
