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
        valid_moves: list[tuple[tuple[int,int], tuple[int,int]]] = []  # init empty list

        # figure out where own and other troops are
        if self.player_number == 1:
            this_player_locations = self.view.p1_troop_locations
            other_player_locations = self.view.p2_troop_locations
        else:
            this_player_locations = self.view.p2_troop_locations
            other_player_locations = self.view.p1_troop_locations

        # address everything but the weird scout moves
        for troop_loc in this_player_locations:
            curr_adj = self.view.get_adjacent_squares(troop_loc) # doesn't include "over the edge" or water locations
            for possible_end_square in curr_adj:
                if possible_end_square not in this_player_locations:
                    # add to list if not already occupied by a troop the player controls
                    valid_moves.append(troop_loc, possible_end_square)

        return valid_moves

    def choose_move(self) -> tuple[tuple[int, int], tuple[int, int]]:
        # define in the parent class, overwrite in child classes, makes it easier to call
        print('chose move player')
        pass

class Human(Player): 
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
    
    def update_view(current_board: Board) -> Board:
        return super.view
    
    def choose_move(self) -> tuple[tuple[int, int], tuple[int, int]]:
        # start_row = int(input('start row: '))
        # start_col = int(input('start_col'))
        # end_row = int(input('end row: '))
        # end_col = int(input('end col: '))
        # return ((start_row, start_col),(end_row, end_col))
        print('chose move human!')

        return ((4,4), (5,4))
    

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
    