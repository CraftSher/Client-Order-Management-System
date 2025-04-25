class Cell:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.value = None


class Board:
    def __init__(self):
        self.cells = [Cell(i + 1) for i in range(9)]

    def show(self):
        line = []
        for index, cell in enumerate(self.cells):
            if cell.value in ['X', 'O']:
                line.append(cell.value)
            else:
                line.append(str(cell.number))

            if (index + 1) % 3 == 0:
                print(' | '.join(line))
                line = []


class Player:
    def __init__(self, name, symbol):
        self.player_name = name
        self.player_symbol = symbol

    def make_move(self, board):
        board.show()
        num = int(input(f'Ходит игрок {self.player_name} символ {self.player_symbol}. Введите номер клетки (1-9): '))
        if 1 <= num <= 9:
            cell = board.cells[num - 1]
            if not cell.is_busy:
                cell.value = self.player_symbol
                cell.is_busy = True
            else:
                print('Эта ячейка занята!')


class Game:
    def __init__(self, player1, player2, board):
        self.players = [player1, player2]
        self.board = board
        self.current_player = 0  # Начнёт первый игрок
        self.game_over = False

    def check_win(self):
        # Проверяем строки, колонки и диагонали на победу
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]

        for combination in winning_combinations:
            values = [self.board.cells[i].value for i in combination]
            if values[0] == values[1] == values[2] and values[0] is not None:
                print(f"Игрок {self.players[self.current_player].player_name} победил!")
                return True
        return False

    def check_draw(self):
        for cell in self.board.cells:
            if cell.value is None:  # Если есть хотя бы одна пустая клетка, ничьи нет
                return False
        print("Ничья!")
        return True

    def start_game(self):
        while not self.game_over:
            current_player = self.players[self.current_player]
            print(f"\nХод игрока {current_player.player_name} (символ {current_player.player_symbol}):")
            current_player.make_move(self.board)

            if self.check_win():  # Проверяем, победил ли текущий игрок
                self.game_over = True
            elif self.check_draw():  # Проверяем ничью
                self.game_over = True
            else:
                # Переключаем игрока
                self.current_player = 1 - self.current_player  # Меняем игрока


# Пример создания игры:

# Создаем игроков
player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")

# Создаем поле
board = Board()

# Создаем игру
game = Game(player1, player2, board)

# Запускаем игру
game.start_game()