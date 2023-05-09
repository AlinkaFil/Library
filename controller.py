from service import new_book, new_user, lend_a_book, turn_in_a_book, statistics


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
            author_book = input('Автор книги')
            lend_a_book(name_user, fullname_user, name_book, author_book)
        elif txt == 4:
            name_user = input('Имя пользователя\n')
            fullname_user = input('Фамилия пользователя\n')
            name_book = input('Название Книги\n')
            author_book = input('Автор книги')
            turn_in_a_book(name_user, fullname_user, name_book,author_book)
        elif txt == 5:
            duty = input('за какой срок проверить?(дней)')
            statistics(duty)
        elif txt == 6:
            print('ВЫХОД')
        else:
            print('Ошибка ввода. Выберете правильный пункт.')
            print_hi()
    except ValueError:
        print('Ошибка ввода. Выберете правильный пункт.')
        print_hi()


if __name__ == '__main__':
    print_hi()
