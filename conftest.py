import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def books_genre(collector):
    collector.add_new_book('Кот колдун')
    collector.add_new_book('Кот зомби')
    collector.add_new_book('Кот Леопольд')
    return collector

@pytest.fixture
def book_genre(collector, books_genre):
    collector.set_book_genre('Кот колдун', 'Фантастика')
    collector.set_book_genre('Кот зомби', 'Ужасы')
    collector.set_book_genre('Кот Леопольд', 'Мультфильмы')
    return collector