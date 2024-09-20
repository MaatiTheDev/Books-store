from lib.db.models import Author, Book, session

def add_author_helper(name):
    """Helper function to add an author"""
    author = Author(name=name)
    session.add(author)
    session.commit()

def add_book_helper(title, author_name):
    """Helper function to add a book with an existing author"""
    author = session.query(Author).filter_by(name=author_name).first()
    if author:
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
    else:
        print(f"Author {author_name} not found.")

def list_books_helper():
    """Helper function to list all books"""
    books = session.query(Book).all()
    return books
