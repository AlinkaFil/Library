from datetime import datetime, timedelta
from app.errors import UserError, BookError, BookIssuedError, IssueLimitError
from app.Base import Books, Users, Receiving
from app.repository import save, find_book, find_user, lended_to_user, book_issued, new_receiving, book_user


def new_book(new_book_name, new_book_author):
    new_book1 = Books(new_book_name, new_book_author)
    return save(new_book1)


def new_user(new_user_name, new_user_fullname):
    new_user1 = Users(new_user_name, new_user_fullname)
    return save(new_user1)


def lend_a_book(name_user, fullname_user, name_book, author_book):
    user = find_user(name_user, fullname_user)
    book = find_book(name_book, author_book)
    if user is None:
        raise UserError
    elif book is None:
        raise BookError
    lended_to_user1 = lended_to_user(user)
    book_issued1 = book_issued(book)
    lended_to_user1 = int(lended_to_user1 or 0)
    book_issued1 = int(book_issued1 or 0)
    if lended_to_user1 < 3:
        if book_issued1 == 0 or book_issued1 is None:
            new_returned_1 = Receiving(user_id=user.id, book_id=book.id, returned=0)
            return save(new_returned_1)
        else:
            raise BookIssuedError
    else:
        raise IssueLimitError


def turn_in_a_book(name_user, fullname_user, name_book, author_book):
    user = find_user(name_user, fullname_user)
    book = find_book(name_book, author_book)
    if user is None:
        raise UserError
    if book is None:
        raise BookError
    return new_receiving(user, book)


def statistics(duty):
    today = datetime.today()
    duty_1 = timedelta(days=duty)
    date_of_issue = today - duty_1
    date_of_issue = datetime.date(date_of_issue)
    statistics1 = book_user(date_of_issue)
    print(statistics1)
    return statistics1
