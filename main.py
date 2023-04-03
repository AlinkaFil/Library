from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from errors import UserError, BookError
from Base import Books, Users, Receiving

engine = create_engine('postgresql+psycopg2://admin:admin@192.168.56.106:5432/pg', echo=True)
engine.connect()


def session_new():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def print_hi():
    try:
        txt = int(input('''Выберете пункт:
        1.добавить книгу
        2.добавить пользователя
        3.выдать книгу
        4.сдать книгу
        5.вывести список названий книг
        6.выход\n'''))
        if txt == 1:
            new_books()
        elif txt == 2:
            new_Users()
        elif txt == 3:
            lend_a_book()
        elif txt == 4:
            turn_in_a_book()
        elif txt == 5:
            books_users()
        elif txt == 6:
            print('ВЫХОД')
        else:
            print('Ошибка ввода. Выберете правильный пункт.')
            print_hi()
    except ValueError:
        print('Ошибка ввода. Выберете правильный пункт.')
        print_hi()


def new_books():
    session = session_new()
    new_books_name = input('Название книги\n')
    new_books_author = input('Автор книги\n')
    new_books1 = Books(new_books_name, new_books_author)
    session.add(new_books1)
    session.commit()


def new_Users():
    session = session_new()
    new_books_name = input('Имя пользователя\n')
    new_books_fullname = input('Фамилия пользователя\n')
    new_books1 = Users(new_books_name, new_books_fullname)
    session.add(new_books1)
    session.commit()


def lend_a_book():
    try:
        session = session_new()
        name_user = input('Имя пользователя\n')
        fullname_user = input('Фамилия пользователя\n')
        name_books = input('Название Книги\n')
        author_book = input('Автор книги')
        user = session.query(Users).filter_by(name=name_user, fullname=fullname_user).first()
        if user == None:
            raise UserError
        book = session.query(Books).filter_by(name_string=name_books, author_string=author_book).first()
        if book == None:
            raise BookError
        user_returned = session.query(func.count(Receiving.user_id)).filter(Receiving.returned == 0,
                                                                            Receiving.user_id == user.id) \
            .group_by(Receiving.book_id, Receiving.returned).scalar()
        books_returned = session.query(func.count(Receiving.book_id)).filter(Receiving.returned == 0,
                                                                             Receiving.book_id == book.id) \
            .group_by(Receiving.book_id, Receiving.returned).scalar()

        user_returned = int(user_returned or 0)
        books_returned = int(books_returned or 0)
        if user_returned < 3:
            if books_returned == 0:
                new_returned_1 = Receiving(user_id=user.id, book_id=book.id, returned=0)
                session.add(new_returned_1)
                session.commit()
            else:
                print("Книга уже выдана. Подберите какую-нибудь другую")
        else:
            print('У читателя слишком много книг')
        print(user_returned, books_returned)
    except UserError:
        print('aregqhrwynh')
    except BookError:
        print('qqqqqq')


def turn_in_a_book():
    try:
        session = session_new()
        name_user = input('Имя пользователя\n')
        fullname_user = input('Фамилия пользователя\n')
        name_books = input('Название Книги\n')
        user = session.query(Users).filter_by(name=name_user, fullname=fullname_user).first()
        if user == None:
            raise UserError
        books = session.query(Books).filter_by(name_string=name_books).first()
        if books == None:
            raise BookError
        receiving_string = session.query(Receiving).filter_by(book_id=books.id, user_id=user.id,
                                                              returned=0).first()
        receiving_string.returned = 1
        session.commit()
    except UserError:
        print('Ошибка в данных пользователя или пользователь не записан')
    except BookError:
        print('Ошибка в названии книги или книга не занесена в каталог')
    except AttributeError:
        print('Эта книга уже на полке')


def books_users():
    session = session_new()
    duty = input('за какой срок проверить?(дней)')
    today = datetime.today()
    duty_1 = timedelta(days=int(duty))
    date_of_issue = today - duty_1
    date_of_issue = datetime.date(date_of_issue)
    print(type(date_of_issue))
    q = session.query(Receiving, Users
                      , Books).filter(Users.id == Receiving.user_id,
                                      Books.id == Receiving.book_id,
                                      Receiving.returned == 0,
                                      func.date_trunc('day', Receiving.received_date) <= date_of_issue).all()
    if len(q) > 0:
        for i in q:
            print(f"Книга {i.Books.name_string} автора {i.Books.author_string}"
                  f" выдана читателю {i.Users.name} {i.Users.name} {i.Receiving.received_date}")
    else:
        print('Нет долгов')


if __name__ == '__main__':
    print_hi()
