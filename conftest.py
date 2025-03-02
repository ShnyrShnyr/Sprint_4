from main import BooksCollector
import pytest

@pytest.fixture
def add_book():
    collection = BooksCollector()
    collection.add_new_book('Роза и червь')
    return collection

@pytest.fixture
def set_book_and_genre():
    collection = BooksCollector()
    collection.add_new_book('Роза и червь')
    collection.set_book_genre('Роза и червь', 'Фантастика')
    return collection

@pytest.fixture
def dict_books():
    collection = BooksCollector()
    books = [['Хоббит', 'Фантастика'], ['Властелин Колец', 'Фантастика'],['Роза и червь', 'Фантастика'], ['Челюсти', 'Ужасы'],['Декстер', 'Детективы'], ['Король Лев', 'Мультфильмы'],['Один дома', 'Комедии']]
    for item in books:
        collection.add_new_book(item[0])
        collection.set_book_genre(item[0], item[1])
    return collection
