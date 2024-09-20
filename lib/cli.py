from db.models import Author, Book, Sale, session

def add_author():
    name = input("Enter the author's name: ").strip()
    if not name:
        print("1. Error: Author name cannot be empty.")
    else:
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f"1. Author '{name}' added successfully!")

def list_authors():
    authors = session.query(Author).all()
    if not authors:
        print("2. No authors found.")
    else:
        print("2. List of authors:")
        for author in authors:
            print(f"    {author.id}: {author.name}")

def add_book():
    title = input("Enter the book title: ").strip()
    author_id = input("Enter the author ID: ").strip()

    if not title:
        print("3. Error: Book title cannot be empty.")
    elif not author_id.isdigit():
        print("3. Error: Author ID must be a valid integer.")
    else:
        author = session.query(Author).get(int(author_id))
        if author:
            book = Book(title=title, author=author)
            session.add(book)
            session.commit()
            print(f"3. Book '{title}' by {author.name} added successfully!")
        else:
            print(f"3. Error: Author with ID {author_id} not found.")

def list_books():
    books = session.query(Book).all()
    if not books:
        print("4. No books found.")
    else:
        print("4. List of books:")
        for book in books:
            print(f"    {book.id}: '{book.title}' by {book.author.name}")

def add_sale():
    book_id = input("Enter the book ID: ").strip()
    quantity = input("Enter the quantity sold: ").strip()

    if not quantity.isdigit() or int(quantity) <= 0:
        print("5. Error: Quantity must be a positive number.")
    elif not book_id.isdigit():
        print("5. Error: Book ID must be a valid integer.")
    else:
        book = session.query(Book).get(int(book_id))
        if book:
            sale = Sale(quantity=int(quantity), book=book)
            session.add(sale)
            session.commit()
            print(f"5. Sale of {quantity} units of '{book.title}' added successfully!")
        else:
            print(f"5. Error: Book with ID {book_id} not found.")

def list_sales():
    sales = session.query(Sale).all()
    if not sales:
        print("6. No sales found.")
    else:
        print("6. List of sales:")
        for sale in sales:
            print(f"    Sale ID {sale.id}: {sale.quantity} units of '{sale.book.title}'")

def main():
    while True:
        print("\nBook Store Management CLI")
        print("1. Add Author")
        print("2. List Authors")
        print("3. Add Book")
        print("4. List Books")
        print("5. Add Sale")
        print("6. List Sales")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == '1':
            add_author()
        elif choice == '2':
            list_authors()
        elif choice == '3':
            add_book()
        elif choice == '4':
            list_books()
        elif choice == '5':
            add_sale()
        elif choice == '6':
            list_sales()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
