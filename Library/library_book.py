#Design a Library Book Tracker to add, issue, return, and view books.

library = []
issued_book = []
def add_book():
    book_name = str(input("Enter book name: "))
    author_name = str(input("Enter the author name: "))
    library_book = {
        "BookName" : book_name,
        "AuthorName" : author_name
    }
    library.append(library_book)
    print("Book Added*")
def issue_book():
    if not library:
        print("Sorry!! No books available to issue!!!")
        return
    num = int(input("Book number you want to issue: "))-1
    view_book()
    if 0 <= num < len(library):
        book = library.pop(num)
        issued_book.append(book)
        print(f"{book['BookName']} - {book['AuthorName']} Issued **")
    else:
        print("Invalid Book Number!!")
def return_book():
    if not issued_book:
        print("No books are issued")
        return
    print("\nIssued Books: ")
    for i in range(len(issued_book)):
        print(f"{i+1}.{issued_book[i]['BookName']} - {issued_book[i]['AuthorName']}")
    num = int(input("Book number you want to return: "))-1
    if 0 <= num < len(issued_book):
        book_return = issued_book.pop(num)
        library.append(book_return)
        print(f"{book_return['BookName']} - {book_return['AuthorName']} Book Returned**")
    else:
        print("Invalid Book number!")
def view_book():
    if not library :
        print("Sorry! No books are here!!!")
    else:
        for i in range(len(library)):
            print(f"{i+1}.{library[i]['BookName']} - {library[i]['AuthorName']}")
def libraryBook():
    while True:
        print("\n__Library Book Tracker__")
        print("1.Add Book")
        print("2.View Book")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Exit")        
        choice = int(input("Enter the choice: "))        
        if choice == 1:
            add_book()
        elif choice == 2:
            view_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Exiting from Library")
            break
        else:
            print("Invalid Choice")
libraryBook()