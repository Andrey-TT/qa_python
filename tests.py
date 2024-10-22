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

    @pytest.mark.parametrize('name', ['К', 'Кот', 'Кот гуляет по двору', 'Что делать, если ваш кот хочет вас убить', 'Что делать, если котя зомби хочет убить?'])
    def test_add_new_book_check_character_count(self, collector, name):
        collector.add_new_book(name)
        assert list(collector.books_genre.keys()) == [name]

    @pytest.mark.parametrize('name', ['', 'Что делать, если кот зомби хочет убить Ва', 'Что делать, если кот зомби хочет убить Вас?'])
    def test_not_add_new_book_check_character_count(self, collector, name):
        collector.add_new_book(name)
        assert not list(collector.books_genre.keys()) == [name]

    def test_set_book_genre (self, collector):
        collector.add_new_book('Индиана кот')
        collector.set_book_genre('Индиана кот', 'Фантастика')
        assert collector.books_genre['Индиана кот'] == 'Фантастика'

    def test_get_book_genre_name (self, collector):
        collector.add_new_book('Кот Леопольд')
        collector.set_book_genre('Кот Леопольд', 'Мультфильмы')
        assert collector.books_genre.get('Кот Леопольд') == 'Мультфильмы'

    def test_get_books_with_horrors_genre(self, collector):
        collector.add_new_book('Кот зомби')
        collector.set_book_genre('Кот зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кот зомби']

    def test_get_books_with_cartoons_genre(self, collector):
        collector.add_new_book('Кот Сникерс')
        collector.set_book_genre('Кот Сникерс', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Кот Сникерс']

    def test_get_books_genre_one_book(self, collector):
        collector.add_new_book('Кот волшебник')
        collector.set_book_genre('Кот волшебник', 'Фантастика')
        assert collector.get_books_genre() == {'Кот волшебник': 'Фантастика'}

    def test_get_books_genre_many_books(self, collector):
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.add_new_book('Ежики мутанты')
        collector.set_book_genre('Ежики мутанты', 'Ужасы')
        collector.add_new_book('Гарри в зазеркалье')
        collector.set_book_genre('Гарри в зазеркалье', 'Фантастика')
        assert collector.get_books_genre() == {'Колобок': 'Мультфильмы',
                                            'Ежики мутанты': 'Ужасы',
                                            'Гарри в зазеркалье': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Город сказка')
        collector.set_book_genre('Город сказка', 'Фантастика')
        collector.add_new_book('Кот в ночи')
        collector.set_book_genre('Кот в ночи', 'Ужасы')
        collector.add_new_book('Слоненок Фрай')
        collector.set_book_genre('Слоненок Фрай', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Город сказка', 'Слоненок Фрай']

    def test_age_rated_books_not_get_books_for_children(self, collector):
        collector.add_new_book('Кот в изумрудном городе')
        collector.set_book_genre('Кот в изумрудном городе', 'Фантастика')
        collector.add_new_book('Киборг маньяк')
        collector.set_book_genre('Киборг маньяк', 'Ужасы')
        collector.add_new_book('Леопольд в гостях у сказки')
        collector.set_book_genre('Леопольд в гостях у сказки', 'Мультфильмы')
        assert not collector.get_books_for_children() == ['Киборг маньяк']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Кот киборг')
        collector.add_book_in_favorites('Кот киборг')
        assert 'Кот киборг' in collector.favorites

    def test_repeated_add_book_in_favorites(self, collector):
        collector.add_new_book('Кот маньяк')
        collector.add_book_in_favorites('Кот маньяк')
        collector.add_book_in_favorites('Кот маньяк')
        assert not collector.favorites == ['Кот маньяк', 'Кот маньяк']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Приключение котика')
        collector.add_book_in_favorites('Приключение котика')
        collector.delete_book_from_favorites('Приключение котика')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Музыкальная шкатулка')
        collector.add_new_book('Шактулка Пандоры')
        collector.add_book_in_favorites('Музыкальная шкатулка')
        collector.add_book_in_favorites('Шактулка Пандоры')
        collector.delete_book_from_favorites('Музыкальная шкатулка')
        assert 'Шактулка Пандоры' in collector.favorites

