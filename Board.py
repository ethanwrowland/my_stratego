from enum import Enum
from Troop_Type import Troop_Type
from Player_Owner import Player_Owner

class Board:
    # define start position constants
    DEFAULT_P1_START_POS = []
    DEFAULT_P2_START_POS = []

    #separate inits for random/non-random starts
    def __init__(self) -> None:
        self.board = self.get_empty_board()


    """
    def __init__(self, p_1_start_pos: list[list[Troop_Type]], p_2_start_pos: list[list[Troop_Type]]) -> None:
        self.board = self.get_empty_board()

        # maybe come back here later to do checks?
        for troop in p_1_start_pos:
            pass
    """
    
    def get_empty_board(self) -> list[list]:
        # empty board is easier to fill in
        board = []

        for row in range(10):
            to_append = []
            for _ in range(10):
                to_append.append(Tile(Troop_Type.empty, Player_Owner.no_owner))
            board.append(to_append)

        # water cells
        # left lake
        board[4][2].troop_type = Troop_Type.water
        board[5][2].troop_type = Troop_Type.water
        board[4][3].troop_type = Troop_Type.water
        board[5][3].troop_type = Troop_Type.water
        # right lake
        board[4][6].troop_type = Troop_Type.water
        board[5][6].troop_type = Troop_Type.water
        board[4][7].troop_type = Troop_Type.water
        board[5][7].troop_type = Troop_Type.water

        return board
    
    def print_board(self) -> None:
        # print rows in reverse order
        row_num = 9
        horizontal_line = "--------------------------------------------------------------"
        while row_num >= 0:
            print(horizontal_line)
            to_print = ''
            to_print += str(row_num) + " |"
            for tile in self.board[row_num]:
                match tile.player_owner:
                    case Player_Owner.player_1:
                        to_print += "P1 "
                    case Player_Owner.player_2:
                        to_print += "P2 "
                    case Player_Owner.no_owner:
                        to_print += "   "
                    case _:
                        raise Exception("error in print_board: no valid player owner in row " + str(row_num) + "row so far: " + to_print)
                match tile.troop_type:
                    case Troop_Type.spy:
                        to_print += "1 "
                    case Troop_Type.scout:
                        to_print += "2 "
                    case Troop_Type.miner:
                        to_print += "3 "
                    case Troop_Type.sergeant:
                        to_print += "4 "
                    case Troop_Type.lieutenant:
                        to_print += "5 "
                    case Troop_Type.captain:
                        to_print += "6 "
                    case Troop_Type.major:
                        to_print += "7 "
                    case Troop_Type.colonel:
                        to_print += "8 "
                    case Troop_Type.general:
                        to_print += "9 "
                    case Troop_Type.marshal:
                        to_print += "10"
                    case Troop_Type.empty:
                        to_print += "  "
                    case Troop_Type.bomb:
                        to_print += "B "
                    case Troop_Type.flag:
                        to_print += "F "
                    case Troop_Type.water:
                        to_print += "WW"
                    case _:
                        raise Exception("Error in printing board, row number: " + str(row_num))
                to_print += "|"
            print(to_print)            
            row_num = row_num - 1
        print(horizontal_line)
        print("  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |")   


class Tile:
    def __init__(self, troop_type: Troop_Type, player_owner: Player_Owner) -> None:
        self.troop_type = troop_type
        self.player_owner = player_owner
    
