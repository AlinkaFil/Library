from datetime import datetime, timedelta
from errors import UserError, BookError
from Base import Books, Users, Receiving
import repository


def new_book(new_book_name, new_book_author):
    new_book = Books(new_book_name, new_book_author)
    repository.save(new_book)


def new_user(new_user_name, new_user_fullname):
    new_user = Users(new_user_name, new_user_fullname)
    repository.save(new_user)


def lend_a_book(name_user, fullname_user, name_book, author_book):
    try:
        user=repository.find_user(name_user, fullname_user)
        book=repository.find_book(name_book, author_book)
        lended_to_user = repository.lended_to_user(user)
        book_issued = repository.book_issued(book)
        if user is None:
            raise UserError
        elif book is None:
            raise BookError
        lended_to_user = int(lended_to_user or 0)
        book_issued = int(book_issued or 0)
        if lended_to_user < 3:
            if book_issued == 0:
                new_returned_1 = Receiving(user_id=user.id, book_id=book.id, returned=0)
                repository.save(new_returned_1)
            else:
                print("Книга уже выдана. Подберите какую-нибудь другую")
        else:
            print('У читателя слишком много книг')
    except UserError:
        print('пользователь не найден')
    except BookError:
        print('книга не нейдена')

def turn_in_a_book(name_user, fullname_user, name_book,author_book):
    try:
        user = repository.find_user(name_user, fullname_user)
        book = repository.find_book(name_book, author_book)
        if user is None:
            raise UserError
        if book is None:
            raise BookError
        receiving = repository.new_receiving(user, book)
        receiving.returned = 1
        repository.save(receiving)
    except UserError:
        print('Ошибка в данных пользователя или пользователь не записан')
    except BookError:
        print('Ошибка в названии книги или книга не занесена в каталог')
    except AttributeError:
        print('Эта книга уже на полке')

def statistics(duty):
    today = datetime.today()
    duty_1 = timedelta(days=int(duty))
    date_of_issue = today - duty_1
    date_of_issue = datetime.date(date_of_issue)
    statistics=repository.book_user(date_of_issue)

    if len(statistics) > 0:
        for i in statistics:
            print(f"Книга {i.Books.name_string} автора {i.Books.author_string}"
                  f" выдана читателю {i.Users.name} {i.Users.name} {i.Receiving.received_date}")
    else:
        print('Нет долгов')


