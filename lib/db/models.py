from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///bookstore.db")
Session = sessionmaker(bind=engine)
session = Session()

# Models
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    sales = relationship("Sale", back_populates="book")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="sales")
