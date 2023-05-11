from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from Base import Receiving, Users, Books


def new_session():
    engine = create_engine('postgresql+psycopg2://admin:admin@192.168.56.106:5432/pg', echo=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def save(x):
    session = new_session()
    session.add(x)
    session.commit()


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
    lended_to_user1 = session.query(func.count(Receiving.user_id)).filter(Receiving.returned == 0,
                                                                          Receiving.user_id == user.id) \
        .group_by(Receiving.user_id).scalar()
    return lended_to_user1


def book_issued(book):
    session = new_session()
    book_issued1 = session.query(func.count(Receiving.book_id)).filter(Receiving.returned == 0,
                                                                       Receiving.book_id == book) \
        .group_by(Receiving.book_id).scalar()
    return book_issued1


def new_receiving(user, book):
    session = new_session()
    new_receiving = session.query(Receiving).filter_by(book_id=book.id, user_id=user.id, returned=0).first()
    new_receiving.returned = 1
    session.commit()


def book_user(date_of_issue):
    session = new_session()
    q = session.query(Receiving, Users, Books).filter(Users.id == Receiving.user_id,
                                                      Books.id == Receiving.book_id,
                                                      Receiving.returned == 0,
                                                      func.date_trunc('day',
                                                                      Receiving.received_date) <= date_of_issue).all()
    return q
