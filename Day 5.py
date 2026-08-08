class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add(self):
        try:
            id = int(input("Book ID: "))
            name = input("Book Name: ")
            author = input("Author: ")
            self.books.append(Book(id, name, author))
            print("Book added")
        except ValueError:
            print("Invalid ID")

    def show(self):
        if not self.books:
            print("No books")
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.id, b.name, b.author, status)

    def issue(self):
        try:
            id = int(input("Book ID: "))
            for b in self.books:
                if b.id == id:
                    if b.available:
                        b.available = False
                        print("Book issued")
                    else:
                        print("Already issued")
                    return
            print("Book not found")
        except ValueError:
            print("Invalid ID")

    def return_book(self):
        try:
            id = int(input("Book ID: "))
            for b in self.books:
                if b.id == id:
                    b.available = True
                    print("Book returned")
                    return
            print("Book not found")
        except ValueError:
            print("Invalid ID")


library = Library()

while True:
    print("\n1.Add  2.Show  3.Issue  4.Return  5.Exit")

    try:
        choice = int(input("Choice: "))

        if choice == 1:
            library.add()
        elif choice == 2:
            library.show()
        elif choice == 3:
            library.issue()
        elif choice == 4:
            library.return_book()
        elif choice == 5:
            print("Bye")
            break
        else:
            print("Wrong choice")

    except ValueError:
        print("Enter a number")
