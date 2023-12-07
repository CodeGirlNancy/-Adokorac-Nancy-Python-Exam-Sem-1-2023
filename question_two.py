#Defining a python class named "Book" with attributes:title,author,and pages.
#Providing a method in the class to display information about the book.
#Creating an instance of the class and display the information.
#Soln
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the Book class
book_instance = Book("Python programming in the Eye of a Beginner", "Nancy Adokorac Isimba", 300)

# Displaying information about the book
book_instance.display_info()


#Creating a derived class "Ebook" that inheritsfrom the "Book" class.
#Adding additional attribute "format" to the Ebook class.
#Displaying information for an instance of the EBook class.
#Soln
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format
    
    def display_info(self):  
        super().display_info()  
        print(f"Format: {self.format}")

# Creating an instance of the Ebook class
ebook_instance = Ebook("Python programming in the Eye of a Beginner", "Nancy Adokorac Isimba", 300, "Pdf")

# Displaying information about the Ebook 
ebook_instance.display_info()


#Create a function on the "Book" class that returns only the book title and its author.
#Soln
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    
    def get_title_author(self):
        return f"{self.title} by {self.author}"

# Creating an instance of the Book class
book_instance = Book("Python programming in the Eye of a Beginner", "Nancy Adokorac Isimba", 300)

# Displaying information about the book using the display_info method
book_instance.display_info()

# Getting and displaying only the title and author using the get_title_author method
title_author = book_instance.get_title_author()
print("Title and Author:", title_author)

#Define the following terms;
#Class
#Class refers to a template for creating objects or module for creating instance and object
#Object
#Object refers to a specific instance of a class.Objects are created based on the structure provided by the class