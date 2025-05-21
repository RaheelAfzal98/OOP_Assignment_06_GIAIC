# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0    # Class variable
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.increment_book_count()   # Increment the book 
    

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("Jinnah Of Pakistan","Stanley Wolpert")
print("Book Title:", book1.title, "Book Author:", book1.author)
print("Total book added:", Book.total_books)
