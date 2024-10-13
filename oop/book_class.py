#creating the class called book
class Book:
    def __init__(self, title: str, author: str, year: int):
        '''initialize the attributes of class instance'''
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        '''invoke the del method to remove book_obj from book'''
        print(f"Deleting {self.title}")

    def __str__(self):
        '''invoke a book_obj to print in desired format from book'''
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        '''invoke the book_obj to print from book'''
        return f"Book('{self.title}', '{self.author}', {self.year})"

