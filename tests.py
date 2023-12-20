import pytest as pytest

from main import BooksCollector

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

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_added_to_book(self, genre):
        """Добавить жанр к книге"""
        collector = BooksCollector()
        name = '1+1'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_not_in_genre(self):
        """Добавить жанр не из списка жанров"""
        collector = BooksCollector()
        name = '1+1'
        genre = 'Драма'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_book_has_no_genre(self):
        """У добавленной книги нет жанра"""
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre(self):
        """Получить книги с определенным жанром"""
        collector = BooksCollector()
        collector.add_new_book('The Green Mile')
        collector.add_new_book('The Mist')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        collector.set_book_genre('The Mist', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_for_children(self):
        """Книги с возрастным рейтингом отсутствуют в списке книг для детей"""
        collector = BooksCollector()
        collector.add_new_book('The Lion King')
        collector.add_new_book('The Mist')
        collector.set_book_genre('The Lion King', 'Мультфильмы')
        collector.set_book_genre('The Mist', 'Ужасы')
        for genre_age_rating in collector.genre_age_rating:
            assert collector.get_books_with_specific_genre(genre_age_rating) not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        """Добавить книгу в избранное и получить список избранного"""
        collector = BooksCollector()
        collector.add_new_book('The Lion King')
        collector.add_book_in_favorites('The Lion King')
        assert collector.get_list_of_favorites_books() == ['The Lion King']

    def test_add_book_in_favorites_readding_a_book(self):
        """Повторно добавить книгу в избранное"""
        collector = BooksCollector()
        collector.add_new_book('The Lion King')
        collector.add_book_in_favorites('The Lion King')
        collector.add_book_in_favorites('The Lion King')
        assert collector.get_list_of_favorites_books() == ['The Lion King']

    def test_add_book_in_favorites_book_not_in_books_genre(self):
        """Добавить в избранную книгу не из списка books_genre"""
        collector = BooksCollector()
        collector.add_book_in_favorites('The Lion King')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        """Удалить книгу из избранного"""
        collector = BooksCollector()
        collector.add_new_book('The Lion King')
        collector.add_book_in_favorites('The Lion King')
        collector.delete_book_from_favorites('The Lion King')
        assert collector.get_list_of_favorites_books() == []


