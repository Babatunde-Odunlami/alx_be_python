#OOP concept- library management
class Book:
    """Class to represent a book in the library."""
    
    def __init__(self, title, author):
        self.title = title              # Public attribute for the title
        self.author = author            # Public attribute for the author
        self._is_checked_out = False    # Private attribute to track availability

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Class to represent a library that manages books."""
    
    def __init__(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, title, author):
        """Add a new book to the library."""
        new_book = Book(title, author)
        self._books.append(new_book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"You have checked out '{title}'."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"You have returned '{title}'."
                else:
                    return f"'{title}' was not checked out."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books if available_books else "No available books."

