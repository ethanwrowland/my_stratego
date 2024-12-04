import Tile
import Player

class Game:
    def __init__(self, player_1_type, player_2_type) -> None:
        # init players
        match player_1_type:
            case "human":
                self.player_1 = Human(1)
            case "computer":
                self.player_1 = Computer(1)
            case _:
                raise Exception("player_1_type invalid")
        match player_2_type:
            case "human":
                self.player_2 = Human(2)
            case "computer":
                self.player_2 = Computer(2)
            case _:
                raise Exception("player_2_type invalid")
            
        # init board
        self.master_board = Board()

        # update board

        # start game by having player make turn

    
