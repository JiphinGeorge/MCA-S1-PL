# Book with optional publisher

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add_publisher(self, publisher):
        self.publisher = publisher

    def display(self):
        if hasattr(self, "publisher"):
            print(f"{self.title} written by {self.author} is published by {self.publisher}")
        else:
            print("Unknown Publisher")


title = input("Enter book title: ")
author = input("Enter book author: ")

b = Book(title, author)

if input("Add publisher? (y/n): ").lower() == "y":
    p = input("Enter publisher: ")
    b.add_publisher(p)

b.display()
