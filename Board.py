from enum import Enum
from Troop_Type import Troop_Type
from Player_Owner import Player_Owner

class Board:
    # define start position constants
    DEFAULT_P1_START_POS = []
    DEFAULT_P2_START_POS = []

    #separate inits for random/non-random starts
    def __init__(self) -> None:
        self.board = [[Tile]]
        self.board = self.get_empty_board()
        self.p1_troop_locations: list[tuple(int,int)] = []
        self.p2_troop_locations: list[tuple(int,int)] = []


    """
    def __init__(self, p_1_start_pos: list[list[Troop_Type]], p_2_start_pos: list[list[Troop_Type]]) -> None:
        self.board = self.get_empty_board()

        # maybe come back here later to do checks?
        for troop in p_1_start_pos:
            pass
    """
    
    def get_empty_board(self) -> list[list]:
        # empty board is easier to fill in
        board: list[list[Tile]] = []

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
                # use cases to append correct string to the 
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
                    case Troop_Type.unknown:
                        to_print += "??"
                    case _:
                        raise Exception("Error in printing board, row number: " + str(row_num) + " tile troop type: " + str(tile.troop_type))
                to_print += "|"
            print(to_print)            
            row_num = row_num - 1
        print(horizontal_line)
        print("  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |")   


    def return_view_boards(self) -> tuple:
        # init empty view boards
        p1_view = Board()
        p2_view = Board()
        # will also generate these because they are sometimes more useful and if we do all this iteration now
        # it will save us an iteration thru the board later
        p1_troop_locations: list[tuple[int,int]] = []
        p2_troop_locations: list[tuple[int,int]] = []

        # iterate through existing board, add information to each view
        for row_index in range(10):
            for col_index in range(10):
                curr_tile: Tile = self.board[row_index][col_index]
                match curr_tile.player_owner:
                    case Player_Owner.no_owner:
                        # p1 doesn't have troop there, but tile could be empty or water
                        p1_view.board[row_index][col_index].player_owner = Player_Owner.no_owner
                        p1_view.board[row_index][col_index].troop_type = curr_tile.troop_type
                        # p2 doesn't have troop there, but tile could be empty or water
                        p2_view.board[row_index][col_index].player_owner = Player_Owner.no_owner
                        p2_view.board[row_index][col_index].troop_type = curr_tile.troop_type

                    case Player_Owner.player_1:
                        # p1 has troop on square, gets to know what is on the tile
                        p1_view.board[row_index][col_index].player_owner = curr_tile.player_owner
                        p1_view.board[row_index][col_index].troop_type = curr_tile.troop_type
                        # p2 knows p1 is there, but not what troop is there
                        p2_view.board[row_index][col_index].player_owner = curr_tile.player_owner
                        p2_view.board[row_index][col_index].troop_type = Troop_Type.unknown

                        # add troop location to the list
                        p1_troop_locations.append((row_index, col_index))

                    case Player_Owner.player_2:
                        # p2 has troop on square, gets to know what is on the tile
                        p2_view.board[row_index][col_index].player_owner = curr_tile.player_owner
                        p2_view.board[row_index][col_index].troop_type = curr_tile.troop_type
                        # p1 knows p2 is there, but not what troop is there
                        p1_view.board[row_index][col_index].player_owner = curr_tile.player_owner
                        p1_view.board[row_index][col_index].troop_type = Troop_Type.unknown

                        # add troop location to the list
                        p2_troop_locations.append((row_index, col_index))

        # store the troop locations in each view board
        p1_view.p1_troop_locations = p1_troop_locations
        p2_view.p1_troop_locations = p1_troop_locations
        p1_view.p2_troop_locations = p2_troop_locations
        p2_view.p2_troop_locations = p2_troop_locations
        return (p1_view, p2_view)
    
    def move_troop(self, start_tuple, end_tuple) -> None:
        # this moves a troop from the start location to the end location (overwrites end location)
        # copy old location to new location
        self.board[end_tuple[0]][end_tuple[1]].player_owner = self.board[start_tuple[0]][start_tuple[1]].player_owner
        self.board[end_tuple[0]][end_tuple[1]].troop_type = self.board[start_tuple[0]][start_tuple[1]].troop_type
        # get rid of the troop from where it was
        self.kill_troop(start_tuple)


    def kill_troop(self, kill_location: tuple[int,int]) -> None:
        # this works to kill a troop essentially (when one player attacks another and loses)
        self.board[kill_location[0]][kill_location[1]].player_owner = Player_Owner.no_owner
        self.board[kill_location[0]][kill_location[1]].troop_type = Troop_Type.empty

    def get_adjacent_squares(self, target_coords: tuple[int,int]) -> list[tuple[int,int]]:
        target_row, target_col = target_coords  # unpack for easier processing
        # returns the coordinates of squares 
        adj_squares = []
        # add above square
        if target_row < 9:
            adj_squares.append((target_row + 1, target_col))
        # add below square
        if target_row > 0:
            adj_squares.append((target_row - 1, target_col))
        # add right square
        if target_col < 9:
            adj_squares.append((target_row, target_col + 1))
        # add left square
        if target_col > 0:
            adj_squares.append((target_row, target_col - 1))

        # remove any possible lake squares (a lot easier to do here than later)
        # left lake
        if (4,2) in adj_squares:
            adj_squares.remove((4,2))
        if (4,3) in adj_squares:
            adj_squares.remove((4,3))
        if (5,2) in adj_squares:
            adj_squares.remove((5,2))
        if (5,3) in adj_squares:
            adj_squares.remove((5,3))
        # right lake
        if (4,6) in adj_squares:
            adj_squares.remove((4,6))
        if (4,7) in adj_squares:
            adj_squares.remove((4,7))
        if (5,6) in adj_squares:
            adj_squares.remove((5,6))
        if (5,7) in adj_squares:
            adj_squares.remove((5,7))

        return adj_squares


class Tile:
    def __init__(self, troop_type: Troop_Type, player_owner: Player_Owner) -> None:
        self.troop_type = troop_type
        self.player_owner = player_owner
    
