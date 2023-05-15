import json

from fastapi import FastAPI, Body, HTTPException

import service
from errors import BookIssuedError, BookError, UserError, NoPublishedBooksError

app = FastAPI()


@app.post("/new-book")
def new_book(new_book_name=Body(embed=True), new_book_author=Body(embed=True)):
    return service.new_book(new_book_name, new_book_author)


@app.post("/new-user")
def new_user(new_user_name=Body(embed=True), new_user_fullname=Body(embed=True)):
    return service.new_user(new_user_name, new_user_fullname)


@app.post("/lend-a-book")
def lend_a_book(name_user=Body(embed=True), fullname_user=Body(embed=True), name_book=Body(embed=True),
                author_book=Body(embed=True)):
    try:
        return service.lend_a_book(name_user, fullname_user, name_book, author_book)
    except BookIssuedError:
        raise HTTPException(status_code=403, detail='книга выдана')
    except UserError:
        raise HTTPException(status_code=404, detail='пользователь не найден')
    except BookError:
        raise HTTPException(status_code=404, detail='книга не нейдена')


@app.post("/turn-in-a-book")
def turn_in_a_book(name_user=Body(embed=True), fullname_user=Body(embed=True), name_book=Body(embed=True),
                   author_book=Body(embed=True)):
    try:
        return service.turn_in_a_book(name_user, fullname_user, name_book, author_book)
    except UserError:
        raise HTTPException(status_code=404, detail='пользователь не найден')
    except BookError:
        raise HTTPException(status_code=404, detail='книга не нейдена')
    except AttributeError:
        raise HTTPException(status_code=403, detail='Эта книга уже на полке')


@app.get("/statistics")
def statistics(duty: int):
    return service.statistics(duty)
