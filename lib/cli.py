import click
from db.models import Author, Book, Sale, session

@click.group()
def cli():
    pass

# Add a new author
@click.command()
@click.argument('name')
def add_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    click.echo(f"Author '{name}' added successfully!")

# List all authors
@click.command()
def list_authors():
    authors = session.query(Author).all()
    for author in authors:
        click.echo(f"{author.id}: {author.name}")

# Add a new book
@click.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add_book(title, author_id):
    author = session.query(Author).get(author_id)
    if author:
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        click.echo(f"Book '{title}' by {author.name} added successfully!")
    else:
        click.echo(f"Author with ID {author_id} not found.")

# List all books
@click.command()
def list_books():
    books = session.query(Book).all()
    for book in books:
        click.echo(f"{book.id}: {book.title} by {book.author.name}")

# Add a new sale
@click.command()
@click.argument('book_id', type=int)
@click.argument('quantity', type=int)
def add_sale(book_id, quantity):
    book = session.query(Book).get(book_id)
    if book:
        sale = Sale(quantity=quantity, book=book)
        session.add(sale)
        session.commit()
        click.echo(f"Sale of {quantity} units of '{book.title}' added successfully!")
    else:
        click.echo(f"Book with ID {book_id} not found.")

# List all sales
@click.command()
def list_sales():
    sales = session.query(Sale).all()
    for sale in sales:
        click.echo(f"Sale ID {sale.id}: {sale.quantity} units of {sale.book.title}")

# Register commands
cli.add_command(add_author)
cli.add_command(list_authors)
cli.add_command(add_book)
cli.add_command(list_books)
cli.add_command(add_sale)
cli.add_command(list_sales)

if __name__ == '__main__':
    cli()
