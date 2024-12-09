from Board import Board
from Troop_Type import Troop_Type

"""Note: view is the information that is deducible without prior knowledge of the game to each player.
         This involves the player's troops and locations and the other player's locations
         This is stored in a Board object
         A computer player will have a probibility matrix that gets updated each time the view is updated
         and includes data that can be infered from previous turns
"""


class Player:
    def __init__(self, player_number: int) -> None:
        self.player_number = player_number
        self.view = Board()

    def update_view(self, new_view: Board) -> None:
        self.view = new_view

    def generate_valid_moves(self) -> list[tuple[tuple[int,int],tuple[int,int]]]:
        # generate a list of valid moves that the player can make based on their view
        # iterate over each of the players' troop locations
        pass

    def choose_move(self) -> tuple(tuple[int, int], tuple[int, int]):
        # define in the parent class, overwrite in child classes, makes it easier to call
        pass

class Human(Player): 
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
    
    def update_view(current_board: Board) -> Board:
        return super.view
    
    def chose_move(self) -> tuple(tuple[int, int], tuple[int, int]):
        # write the functionality for this later???
        return ((0,0),(0,1))
    

class Computer(Player):
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
        self.view = self.initialize_compuer_view()
    
    def initialize_compuer_view(self):
        # write later
        return [[]]
    
    def update_computer_view(self, start_loc: tuple[tuple], end_loc: tuple[tuple], start_troop_type: Troop_Type, end_troop_type: Troop_Type) -> bool:
        #write later
        return True
    