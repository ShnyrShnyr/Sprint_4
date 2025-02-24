from main import BooksCollector
import pytest

@pytest.fixture
def add_book():
    collection = BooksCollector()
    collection.add_new_book('Роза и червь')
    return collection.books_genre

@pytest.fixture
def set_book_and_genre():
    collection = BooksCollector()
    collection.add_new_book('Роза и червь')
    collection.set_book_genre('Роза и червь', 'Фантастика')
    return collection.books_genre

@pytest.fixture
def dict_books():
    collection = BooksCollector()
    book = ['Хоббит', 'Властелин Колец', 'Роза и червь']
    for item in book:
        collection.add_new_book(item)
        collection.set_book_genre(item, 'Фантастика')
    book = ['Челюсти']
    for item in book:
        collection.add_new_book(item)
        collection.set_book_genre(item, 'Ужасы')
    book = ['Декстер']
    for item in book:
        collection.add_new_book(item)
        collection.set_book_genre(item, 'Детективы')
    book = ['Король Лев']
    for item in book:
        collection.add_new_book(item)
        collection.set_book_genre(item, 'Мультфильмы')
    book = ['Один дома']
    for item in book:
        collection.add_new_book(item)
        collection.set_book_genre(item, 'Комедии')
    return collection
