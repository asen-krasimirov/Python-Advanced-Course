

class GameLogic:
    __possible_moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    def __init__(self, territory):
        self.territory = territory
        self.territory_size = len(territory)
        self.snake_position = self.find_element("S")
        self.game_over = False
        self.food_quantity = 0

    def find_element(self, element):
        for r in range(self.territory_size):
            for y in range(self.territory_size):

                if self.territory[r][y] == element:
                    return r, y

    def snake_position_delta(self, direction):
        cur_row, cur_column = self.snake_position
        self.territory[cur_row][cur_column] = "."
        new_row, new_column = cur_row+self.__possible_moves[direction][0],\
                              cur_column+self.__possible_moves[direction][1]
        self.snake_position = new_row, new_column
        return new_row, new_column

    def snake_move(self):
        cur_row, cur_column = self.snake_position
        new_elem = self.territory[cur_row][cur_column]
        if new_elem == "*":
            self.food_quantity += 1
            if self.food_quantity >= 10:
                self.game_over = True

        if new_elem == "B":
            self.territory[cur_row][cur_column] = "."
            cur_row, cur_column = self.find_element("B")

        self.snake_position = cur_row, cur_column

    def place_snake(self):
        cur_row, cur_column = self.snake_position
        self.territory[cur_row][cur_column] = "S"

    def print_territory(self):
        for row in self.territory:
            print("".join(row))


def validate_index(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


field_size = int(input())
field = [list(input()) for _ in range(field_size)]
game = GameLogic(field)

while not game.game_over:
    command = input()
    new_position = game.snake_position_delta(command)

    if not validate_index(field_size, new_position[0]) or not validate_index(field_size, new_position[1]):
        game.game_over = True
        continue

    game.snake_move()
    game.place_snake()


if game.game_over and game.food_quantity < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {game.food_quantity}")
game.print_territory()
