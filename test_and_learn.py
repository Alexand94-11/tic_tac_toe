# Использование импорта пакета
from gameparts import Board

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

# Из модуля inspect импортировать функцию getsource.
from inspect import getsource, isfunction, ismethod

# Функция getsource() в работе.
print(getsource(Board))
# display() - это функция?
print(isfunction(game.display))
# display() - это метод?
print(ismethod(game.display))

# Docstring:
print(Board.__doc__)
