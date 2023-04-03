from sqlalchemy import Column, Integer, String, create_engine, ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import psycopg2


Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name_string = Column(String)
    author_string = Column(String)

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

    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id,self.name, self.fullname)


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
    engine = create_engine('postgresql+psycopg2://admin:admin@192.168.56.106:5432/pg', echo=True)
    engine.connect()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    qa()
