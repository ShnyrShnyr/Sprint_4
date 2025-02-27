from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги в словарь
        assert len(collector.get_books_genre()) == 2 # я тут поправил, чтобы он не падал

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Тест 1. Проверить, что у добавленной книги жанр пустая строка

    def test_add_new_book_books_genre_is_empty(self, add_book):
        assert add_book.get('Роза и червь') == ''

    # Тест 2. Проверить, что жанр добавился к книге
    def test_set_book_genre_was_appeared(self, set_book_and_genre):
        assert set_book_and_genre.get('Роза и червь') == 'Фантастика'

    # Тест 3. Проверить, что жанр можно найти по названию книги
    def test_get_book_genre_for_name(self, dict_books):
        assert dict_books.get_book_genre('Челюсти') == 'Ужасы'

    # Tecт 4. Проверить, что выводится список книг по жанру Фантастика
    def test_get_books_with_specific_genre_fantastic(self, dict_books):
        assert 'Хоббит' and 'Властелин Колец' and 'Роза и червь' in dict_books.get_books_with_specific_genre('Фантастика')

    # Тест 5. Проверить, что в запросе всей коллекции есть фильмы Один дома, Челюсти, Декстер
    def test_get_books_genre_some_books_in_dict(self, dict_books):
        assert 'Один дома' and 'Челюсти' and 'Декстер' in dict_books.get_books_genre()

    # Тест 6. Проверить, что книги жанра Ужасы и Детективы не в списке книг для детей
    def test_get_books_for_children_without_horrors_detective(self, dict_books):
        assert 'Декстер' and 'Челюсти' not in dict_books.get_books_for_children()

    # Тест 7. Проверить, что книга добавилась в избранное
    def test_add_book_in_favorites_done(self, dict_books):
        dict_books.add_book_in_favorites('Роза и червь')
        assert 'Роза и червь' in dict_books.favorites

    # Тест 8. Проверить, что книга удалилась из избранного
    def test_delete_book_from_favorites_done(self, dict_books):
        dict_books.add_book_in_favorites('Роза и червь')
        dict_books.delete_book_from_favorites('Роза и червь')
        assert 'Роза и червь' not in dict_books.favorites

    # Тест 9. Проверить, что все добавленные в избранное книги есть в списке
    @pytest.mark.parametrize('favor_book',['Роза и червь','Декстер','Один дома'])
    def test_get_list_of_favorites_books_each_book_in_favor(self, dict_books, favor_book):
        dict_books.add_book_in_favorites(favor_book)
        assert favor_book in dict_books.favorites