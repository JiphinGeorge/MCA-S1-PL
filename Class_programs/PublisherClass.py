class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f" Publisher Name is {self.name}")


class Book(Publisher):
    def __init__(self, name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        
    def display(self):
        super().display()
        print(f"Title is {self.title}")
        print(f"Author is {self.author}")


class Python(Book):
    def __init__(self, name, title, author,price,no_of_pages):
        super().__init__(name, title, author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        super().display()
        print(f"The Price of the Book is {self.price}")
        print(f"Number of Pages : {self.no_of_pages}")

a=Python("American Readers" ,"It Ends With Us","Collen Hoover",999.99,1500)
a.display()




    
    
    
    
    
    
    
    
    
    
    
    