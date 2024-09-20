from models import Author, Book, Sale, session

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create seed data
author_1 = Author(name="J.K. Rowling")
book_1 = Book(title="Harry Potter", author=author_1)
sale_1 = Sale(quantity=50, book=book_1)

author_2 = Author(name="George R.R. Martin")
book_2 = Book(title="Game of Thrones", author=author_2)
sale_2 = Sale(quantity=30, book=book_2)

# Add data to session
session.add_all([author_1, book_1, sale_1, author_2, book_2, sale_2])
session.commit()

print("Database seeded successfully!")
