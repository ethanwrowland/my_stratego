from Game_State import Game_State
from Board import Board
from Player import Human
from Player import Computer



class Game:
    def __init__(self, player_1_type: str, player_2_type: str, disp_board_input: str) -> None:
        match disp_board_input.upper():
            case "TRUE":
                self.disp_board_bool = True
            case "FALSE":
                self.disp_board_bool = False
            case _:
                raise Exception("display board boolean invalid")

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
        
        self.game_state = Game_State.setup
        # init board
        self.master_board = Board()

        # update board/get starting positions

        # play game
        while self.game_state != -3:  # no player has won 
            match self.game_state:
                case Game_State.player_1_to_move:
                    self.display_game_board()
                    if not self.detect_player_stuck(self.player_1):
                        # p1 is not stuck, allow p1 to move
                        self.execute_turn(self.player_1)

                case Game_State.player_2_to_move:
                    self.display_game_board()
                    if not self.detect_player_stuck(self.player_2):
                        # p2 is not stuck, allow p2 to move
                        self.execute_turn(self.player_2)
                
                case Game_State.player_1_victory:
                    self.display_game_board()
                    print("Player 1 wins!")
                    self.game_state = Game_State.game_finished

                case Game_State.player_2_victory:
                    self.display_game_board()
                    print("Player 2 wins!")
                    self.game_state = Game_State.game_finished

        
                

    def detect_player_stuck(self, player_to_check) -> bool:
        # detect if the given player is stuck (and update game state). If stuck, return true, false otw
        return False

    def execute_turn(self, moving_player, start_pos: tuple[int,int], end_pos: tuple[int,int]):
        pass

    def display_game_board(self):
        # this will handle displaying the board, given a variety of conditions/situations (more complicated later)
        if self.disp_board_bool:
            self.master_board.print_board()



    
