import random
from faker import Faker
from conf import MODEL
import json

faker_ru = Faker("ru_RU")

BOOKS = "books.txt"


def get_title() -> str:
    """
    Назначение функции: извлечение названия книги для параментра title.
    :return: одна случайная строка из файла books.txt.
    """
    with open(BOOKS, "r", encoding="utf-8") as file:
        data = file.readlines()
    return random.choice(data)


def get_year() -> int:
    """
    Назначение функции: получить значение для параметра year.
    :return: случайное целое число из указанного диапазона.
    """
    random_year = random.randint(1800, 2022)
    return random_year


def get_pages() -> int:
    """
    Назначение функции: получить значение для параметра pages.
    :return: случайное целое число из указанного диапазона.
    """
    random_pages = random.randint(120, 530)
    return random_pages


def get_isbn13() -> str:
    """
    Назаначение функции: получить значение для параметра isbn13.
    :return: возвращает случайную строку содержащую международный стандартный книжный номер.
    """
    isbn13 = faker_ru.isbn13()
    return isbn13


def get_rating() -> float:
    """
    Назначение функции: получить значение для параметра rating.
    :return: случайное число с плавающей запятой из указанного диапазона.
    """
    random_rating = random.uniform(0.0, 5.0)
    return random_rating


def get_price() -> float:
    """
    Назначение функции: получить значение для параметра price.
    :return: случайное число с плавающей запятой из указанного диапазона.
    """
    random_price = random.uniform(1500.0, 4500.0)
    return random_price


def get_author() -> list:
    """
    Назаначение функции: получить значение для параметра author.
    :return: возвращает список, содержащий от 1 до 3 авторов.
    """
    list_author = []
    for _ in range(1, 100):
        list_author.append(faker_ru.name())
    authors = random.randint(1, 3)
    list_random_authors = random.sample(list_author, authors)
    return list_random_authors


def get_fields() -> dict:
    """
    Назаначение функции: получить значения для параметра fields.
    :return: словарь
    """
    return {
        "title": get_title(),
        "year": get_year(),
        "pages": get_pages(),
        "isbn13": get_isbn13(),
        "rating": get_rating(),
        "price": get_price(),
        "author": get_author()
             }


def get_book(pk=1):
    """
    Назначение функции: генератор.
    :param pk: счетчик по умолчанию равный 1.
    :return: генератор, который перебирается в цикле for, для получения значений (словарей) "по запросу".
    """
    increment = pk
    while True:
        dict_ = {
            "model": MODEL,
            "pk": increment,
            "fields": get_fields()
            }
        yield dict_
        increment += 1


def get_json(data: list):
    """
    Назначение функции: преобразовать список словарей в строку формата JSON и записать его в файл.
    :param data: список словарей.
    :return: созданный файл, содержащий список словарей, формата JSON.
    """
    with open("books.json", "w", encoding="utf-8") as file_write:
        json.dump(data, file_write, indent=4, ensure_ascii=False)


def main():
    """
    Назначение функции: запуск функции "генератор". С помощью generate сформировать список словарей,
    содержащий 100 книг, и запустить функцию для записи этого списка словарей в файл формата JSON.
    """
    generate = get_book()
    data = [next(generate) for _ in range(100)]
    get_json(data)


if __name__ == "__main__":
    main()
