from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from app.Base import Receiving, Users, Books, new_connect, create_database


def repo_create_database():
    create_database()


def new_session():
    engine = new_connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def save(x):
    session = new_session()
    session.add(x)
    session.commit()
    session.refresh(x)
    return x


def find_user(name_user, fullname_user):
    session = new_session()
    user = session.query(Users).filter_by(name=name_user, fullname=fullname_user).first()
    return user


def find_book(name_book, author_book):
    session = new_session()
    book = session.query(Books).filter_by(name_string=name_book, author_string=author_book).first()
    return book


def lended_to_user(user):
    session = new_session()
    lent_to_user1 = session.query(func.count(Receiving.user_id)).filter(Receiving.returned == 0,
                                                                        Receiving.user_id == user.id) \
        .group_by(Receiving.user_id).scalar()
    return lent_to_user1


def book_issued(book):
    session = new_session()
    book_issued1 = session.query(func.count(Receiving.book_id)).filter(Receiving.returned == 0,
                                                                       Receiving.book_id == book.id) \
        .group_by(Receiving.book_id).scalar()
    return book_issued1


def new_receiving(user, book):
    session = new_session()
    new_receiving = session.query(Receiving).filter_by(book_id=book.id, user_id=user.id, returned=0).first()
    new_receiving.returned = 1
    session.commit()
    session.refresh(new_receiving)
    return new_receiving


def book_user(date_of_issue):
    result = []
    session = new_session()
    q = session.query(Users.name, Users.fullname, Books.name_string, Books.author_string,
                      Receiving.received_date).filter(Users.id == Receiving.user_id,
                                                      Books.id == Receiving.book_id,
                                                      Receiving.returned == 0,
                                                      func.date_trunc('day',
                                                                      Receiving.received_date) <= date_of_issue).all()
    for row in q:
        result.append(row._asdict())

    return result
