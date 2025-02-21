"""
Create a class for a book with attributes like title and author.
"""

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def to_string(self):
        print(f"Book Title: {self.title}\nAuthor: {self.author}")


if __name__ == "__main__":
    book = Book("Hunger Games", "Suzanne Collins")
    print(book.get_title())
    print(book.get_author())
