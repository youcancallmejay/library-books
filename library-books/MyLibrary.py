import csv

def main():

    class Book:
        def __init__(self, book_name, author) -> None:
            self.book_name = book_name
            self.author = author
            self.ISBN = 0
            self.book_status = False
            

        def is_available(self, status):
            if status.lower() == 'y':
                self.book_status = True
            else: 
                self.book_status = False
                

#    class Library: 
#       def __init__(self) -> None:
            
    books = []
    #breakpoint()
    with open("short_list_books.csv") as booklist: 
        file_reader = csv.DictReader(booklist)
        for book in file_reader: 
            new_book = Book(book.get('title', ''), book.get('author', '')) 
            books.append(new_book)
            availability = input(f"Is {new_book.book_name} available? Y/N? " )
            new_book.is_available(availability)

    for book in books: 
        print(book.book_name)
        print(book.book_status)


main()