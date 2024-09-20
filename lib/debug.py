from lib.db.models import initialize_database, session, Author, Book

# Initialize the database
initialize_database()

# Example: Fetch and print all authors
authors = session.query(Author).all()
for author in authors:
    print(author.name)
