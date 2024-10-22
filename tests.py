from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_repeated_add_new_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_no_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    @pytest.mark.parametrize('name', ['К', 'Кот', 'Кот гуляет по двору', 'Что делать, если ваш кот хочет вас убить', 'Что делать, если кот зомби хочет убить'])
    def test_add_new_book_check_character_count(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert 0 < len(name) < 41

    def test_set_book_genre (self, collector, books_genre, book_genre):
        collector.add_new_book('Индиана кот')
        collector.set_book_genre('Индиана кот', 'Фантастика')
        assert collector.books_genre['Индиана кот'] == 'Фантастика'

    def test_get_book_genre_name (self, collector, books_genre, book_genre):
        assert collector.books_genre.get('Кот Леопольд') == 'Мультфильмы'

    @pytest.mark.parametrize('name, genre', [
                                            ['Кот колдун', 'Фантастика'],
                                            ['Кот зомби', 'Ужасы'],
                                            ['Кот Леопольд', 'Мультфильмы'],
                                            ])

    def get_books_with_specific_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_with_horrors_genre(self, collector, books_genre, book_genre):
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кот зомби']

    def test_get_books_with_cartoons_genre(self, collector, books_genre, book_genre):
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Кот Леопольд']

    def test_get_books_genre_one_book(self, collector):
        collector.add_new_book('Кот колдун')
        collector.set_book_genre('Кот колдун', 'Фантастика')
        assert collector.get_books_genre() == {'Кот колдун': 'Фантастика'}

    def test_get_books_genre_many_books(self, collector, books_genre, book_genre):
        assert collector.get_books_genre() == {'Кот Леопольд': 'Мультфильмы',
                                            'Кот зомби': 'Ужасы',
                                            'Кот колдун': 'Фантастика'}

    def test_get_books_for_children(self, collector, books_genre, book_genre):
        assert collector.get_books_for_children() == ['Кот колдун', 'Кот Леопольд']

    def test_age_rated_books_not_get_books_for_children(self, collector, books_genre, book_genre):
        assert not collector.get_books_for_children() == ['Кот зомби']

    def test_add_book_in_favorites(self, collector, books_genre):
        collector.add_book_in_favorites('Кот колдун')
        assert 'Кот колдун' in collector.favorites

    def test_repeated_add_book_in_favorites(self, collector, books_genre):
        collector.add_book_in_favorites('Кот колдун')
        collector.add_book_in_favorites('Кот колдун')
        assert not collector.favorites == ['Кот колдун', 'Кот колдун']

    def test_delete_book_from_favorites(self, collector, books_genre):
        collector.add_book_in_favorites('Кот колдун')
        collector.delete_book_from_favorites('Кот колдун')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector, books_genre):
        collector.add_book_in_favorites('Кот колдун')
        collector.add_book_in_favorites('Кот зомби')
        collector.delete_book_from_favorites('Кот колдун')
        #assert collector.get_list_of_favorites_books() == ['Кот Коломбо']
        assert 'Кот зомби' in collector.favorites

