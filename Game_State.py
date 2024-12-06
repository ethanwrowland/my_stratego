from enum import Enum

class Game_State(Enum):
    setup = 0
    player_1_to_move = 1
    player_2_to_move = 2
    player_1_victory = -1
    player_2_victory = -2
    game_finished = -3