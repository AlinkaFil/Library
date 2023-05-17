from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app.settings import settings

Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name_string = Column(String)
    author_string = Column(String)
    __table_args__ = tuple(UniqueConstraint(name_string, author_string, name='book_name'))

    def __init__(self, name_string, author_string):
        self.name_string = name_string
        self.author_string = author_string

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.name_string, self.author_string)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    __table_args__ = tuple(UniqueConstraint(name, fullname, name='user_name'))

    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.name, self.fullname)


class Receiving(Base):
    __tablename__ = 'receiving'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey('books.id'))
    received_date = Column(DateTime(), default=datetime.now)
    returned = Column(Integer)

    def __init__(self, user_id, book_id, returned):
        self.user_id = user_id
        self.book_id = book_id
        self.returned = returned

    def __repr__(self):
        return "<User('%s','%s','%s','%s','%s')>" % (self.id, self.user_id, self.book_id,
                                                     self.received_date, self.returned)


def qa():
    engine = new_connect()
    Base.metadata.create_all(engine)


def new_connect():
    engine = create_engine(
        f"postgresql+psycopg2://{settings.user_name}:{settings.password}@{settings.host}:{settings.port}/{settings.db_name}",
        echo=True)
    engine.connect()
    return engine


if __name__ == '__main__':
    qa()
