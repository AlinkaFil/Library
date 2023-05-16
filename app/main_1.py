from app.service import new_book, new_user, lend_a_book, turn_in_a_book, statistics
from app.errors import BookIssuedError, BookError, UserError


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
            new_book_name = input('Название книги\n')
            new_book_author = input('Автор книги\n')
            new_book(new_book_name, new_book_author)
        elif txt == 2:
            new_user_name = input('Имя пользователя\n')
            new_user_fullname = input('Фамилия пользователя\n')
            new_user(new_user_name, new_user_fullname)
        elif txt == 3:
            name_user = input('Имя пользователя\n')
            fullname_user = input('Фамилия пользователя\n')
            name_book = input('Название Книги\n')
            author_book = input('Автор книги\n')
            try:
                lend_a_book(name_user, fullname_user, name_book, author_book)
            except BookIssuedError:
                print("Книга уже выдана. Подберите какую-нибудь другую")
            except UserError:
                print('пользователь не найден')
            except BookError:
                print('книга не нейдена')
        elif txt == 4:
            name_user = input('Имя пользователя\n')
            fullname_user = input('Фамилия пользователя\n')
            name_book = input('Название Книги\n')
            author_book = input('Автор книги\n')
            try:
                turn_in_a_book(name_user, fullname_user, name_book, author_book)
            except UserError:
                print('пользователь не найден')
            except BookError:
                print('книга не нейдена')
            except AttributeError:
                print('Эта книга уже на полке')
        elif txt == 5:
            duty = int(input('за какой срок проверить?(дней)\n'))
            statistics(duty)
        elif txt == 6:
            print('ВЫХОД')
        else:
            print('Ошибка ввода. Выберете правильный пункт.\n')
            print_hi()
    except ValueError:
        print('Ошибка ввода. Выберете правильный пункт.')
        print_hi()


if __name__ == '__main__':
    print_hi()
