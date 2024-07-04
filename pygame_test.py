# game.py

import pygame
# Запускать нужно через консоль, предварительно установив pygame

# Здесь нужно импортировать класс Board. Импорт исключений для игры
# с графическим интерфейсом не понадобится.
from gameparts import Board

pygame.init()

# Здесь определены разные константы, например
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Задать размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)


# Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий.
def draw_lines():
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )

# Функция, которая отвечает за отрисовку фигур
# (крестиков и ноликов) на доске.
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


# Сюда нужно добавить функцию save_result().
def save_result(result):
    # Работа с файлами с контекстным менеджером:
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


# В этой функции описана логика игры. Вам нужно её дополнить. По структуре
# тут всё то же самое, что было в вашем коде раньше.
# Но есть отличие - вместо метода display() используется
# новая функция draw_figures().
def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    # В цикле обрабатываются такие события, как
    # нажатие кнопок мыши и закрытие окна.
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                # Сюда нужно дописать код:
                # если ячейка свободна,
                if game.board[clicked_row][clicked_col] == ' ':
                    # то сделать ход,
                    game.make_move(clicked_row, clicked_col, current_player)
                    # проверить на победу,
                    if game.check_win(current_player):
                        result = f'Победили {current_player}'
                        print(result)
                        save_result(result)
                        running = False
                    # проверить на ничью,
                    elif game.is_board_full():
                        result = 'Ничья!'
                        print(result)
                        save_result(result)
                        running = False
                    # сменить игрока.
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)

        # Обновить окно игры.
        pygame.display.update()

    # Деинициализирует все модули pygame, которые были инициализированы ранее.
    pygame.quit()


if __name__ == '__main__':
    main()

'''
# Тестирование методов для отрисовки
# pygame_test.py

# Импортировать библиотеку Pygame.
import pygame

# Инициализировать библиотеку Pygame.
pygame.init()

# Создать окно размером 800x600 точек (или пикселей).
screen = pygame.display.set_mode((800, 600))
# Задать окну заголовок.
pygame.display.set_caption('Пример графического окна Pygame')


running = True

# Описание главного цикла игры.
# Этот цикл работает до тех пор, пока пользователь не закроет окно.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Рисование линии.
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (700, 500), 5)

    # Рисование квадрата.
    # Квадрат с верхним левым углом в точке (300, 200) и размерами 200x200 
    # будет нарисован зелёным цветом.
    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(300, 200, 200, 200))

    # Отобразить нарисованные элементы в окне.
    pygame.display.update()

# Деинициализирует все модули pygame, которые были инициализированы ранее.
pygame.quit()
'''
