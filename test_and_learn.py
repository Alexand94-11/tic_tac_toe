# Использование импорта пакета
from gameparts import Board
# Из модуля inspect импортировать функцию getsource.
from inspect import getsource, isfunction, ismethod
# Импорт модуля для работы с исключениями
from gameparts.exceptions import FieldIndexError

# Интроспекция
game = Board()
print(type(game))

# Выведется:
# <class 'gameparts.parts.Board'>
# Функция определила, что это объект класса Board,
# который описан в модуле parts пакета gameparts.

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется:
# True
# True
# False

# Определить, принадлежит ли экземпляр к определённому классу,
# можно и через функцию isinstance() (считается лучшей практикой):

print(isinstance(game, Board))
print(isinstance(game, str))

# Выведется:
# True
# False

# Интроспекция с помощью атрибута __class__:
print(game.__class__)

# Выведется:
# <class 'gameparts.parts.Board'>

# Функция dir() возвращает список
# атрибутов и методов, доступных для объекта:
print(dir(game))

# Можно проверить, есть ли у объекта game метод __str__:
print('__str__' in dir(game))

# Выведется:
# True

# Ещё такую проверку можно выполнить при помощи функции hasattr():
print(hasattr(game, '__str__'))

# Выведется:
# True

# Через словарь __dict__, доступный атрибуту __class__,
# можно получить атрибуты и методы,
# определённые только при создании объекта:
print(game.__class__.__dict__)

# Функция inspect.getsource(object)
# Функция getsource() модуля inspect позволяет получить код объекта,
# например, функции или метода.

# Функция getsource() в работе.
print(getsource(Board))
# display() - это функция?
print(isfunction(game.display))
# display() - это метод?
print(ismethod(game.display))

# Docstring:
print(Board.__doc__)


'''
# Стандартная логика работы программы:
# Создать игровое поле - объект класса Board.
game = Board()
# Отрисовать поле в терминале.
game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
game.make_move(1, 1, 'X')
print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
game.display()
game.make_move(0, 0, 'O')
print('Ход сделан!')
game.display()
game.make_move(0, 1, 'X')
print('Ход сделан!')
game.display()
game.make_move(2, 1, 'O')
print('Ход сделан!')
game.display()
'''
'''
# Использование конструкции if __name__ == '__main__'
# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
if __name__ == '__main__':
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()
'''

# Тот же код с использованием функции main()

'''
# Отработка программы с исключениями
def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError.
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    # Аналогичная проверка по номеру столбца:
    if column < 0 or column >= game.field_size:
        raise FieldIndexError
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()
'''


# Отработка программы с исключениями с учетом "укрощения"
def main():
    game = Board()
    game.display()

    # Запускается бесконечный цикл.
    while True:
        # В этом блоке содержатся операции, которые могут вызвать исключение.
        try:
            # Пользователь вводит значение номера строки.
            row = int(input('Введите номер строки: '))
            # Если введённое число меньше 0 или больше
            # или равно game.field_size...
            if row < 0 or row >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            # Если введённое число меньше 0 или больше
            # или равно game.field_size...
            if column < 0 or column >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
        # Если возникает исключение FieldIndexError...
        except FieldIndexError:
            # ...выводятся сообщения...
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
            continue
        # Если возникает исключение ValueError...
        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue
        except Exception as e:
            print(f'Возникла ошибка: {e}')
        # Если в блоке try исключения не возникло...
        else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


# А вот вызов этой функции.
if __name__ == '__main__':
    main()
