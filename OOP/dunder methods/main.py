# Magic methods = Dunder methods(double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author} has {self.num_pages}"

    def __eq__(self, book):
        return self.title == book.title and self.author == book.author

    def __lt__(self, book):
        return self.num_pages < book.num_pages

    def __lt__(self, book):
        return self.num_pages > book.num_pages

    def __add__(self, book):
        return self.num_pages + book.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title

        if key == 'author':
            return self.author


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion", "C.S. Lewis", 128)

# __str__ - it returns a string representation of the object
print(book1)
print(book2)
print(book3)

# __eq__ - it returns boolean value if the properties of object are the same
print(book1 == book2)
print(book1 == book4)

# __lt__ - it returns boolean value if the properties of object that are less
print(book1 < book2)

# __gt__ - it returns boolean value if the properties of object that are greater
print(book1 > book2)

# __add__ - adds the num of pages
print(book1 + book2)

# __contains__
print("Lion" in book1)

# __getiem__
print(book1['title'])
print(book1['author'])
