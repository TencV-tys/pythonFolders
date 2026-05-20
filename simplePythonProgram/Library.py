class Book:
    def __init__(self, title, author, isbn):
        self.info = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True,
        }
    def show(self):
        print(f"Title: {self.info['title']}")
        print(f"Author: {self.info['author']}")
        print(f"isbn: {self.info['isbn']}")
        status = "Available" if self.info['available']  else "Borrowed"
        print(f"Availability: {status}")
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title, author, isbn):
        new_books = Book(title,author,isbn)
        self.books[isbn] = new_books
        print(f'Added {title} by {author}')
    def find_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            print(f'Found: {book.info['title']}')
            return book
        else:
            print(f"❌ Book with ISBN {isbn} not found")
            return None
    def borrow_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.info["available"]:
                book.info["available"] = False
                print(f"✅ Borrowed: {book.info['title']}")
            else:
                print(f"❌ {book.info['title']} is already borrowed")
        else:
            print(f"❌ Book not found")
    def return_book(self,isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.info['available']:
                book.info['available'] = True
                print(f"✅ Returned: {book.info['title']}")
            else:
                print(f"Borrowed")
        else:
            print(f'Book not found')


library = Library()
library.add_book('Dexters','Dexter','010')
library.borrow_book('010')
found = library.find_book('011')

if found:
    found.show()
else:
    print('Book not Found')

    