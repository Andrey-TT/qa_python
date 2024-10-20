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
    collector.add_new_book('Кот Коломбо')
    collector.add_new_book('Кот Леопольд')
    collector.add_new_book('Кот играет на баяне')
    collector.add_new_book('Убить всех котов')
    return collector

@pytest.fixture
def book_genre(collector, books_genre):
    collector.set_book_genre('Кот колдун', 'Фантастика')
    collector.set_book_genre('Кот зомби', 'Ужасы')
    collector.set_book_genre('Кот Коломбо', 'Детективы')
    collector.set_book_genre('Кот Леопольд', 'Мультфильмы')
    collector.set_book_genre('Кот играет на баяне', 'Комедии')
    collector.set_book_genre('Убить всех котов', 'Ужасы')
    return collector