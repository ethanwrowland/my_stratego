from Board import Board
from Troop_Type import Troop_Type
from Player_Owner import Player_Owner

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

        for troop_loc in this_player_locations:
            # figure out what troop type is at this location (scouts will be weird)
            curr_troop_type: Troop_Type = self.view.board[troop_loc[0]][troop_loc[1]].troop_type
            
            if curr_troop_type == Troop_Type.scout:  # deal with scouts
                valid_moves.append(self.generate_valid_scout_moves(troop_loc))

            elif curr_troop_type.value < 11 and curr_troop_type.value > 0: # normal troop (not flag/bomb)
                curr_adj = self.view.get_adjacent_squares(troop_loc) # doesn't include "over the edge" or water locations
                for possible_end_square in curr_adj:
                    if possible_end_square not in this_player_locations:
                        # add to list if not already occupied by a troop the player controls
                        valid_moves.append((troop_loc, possible_end_square))

        return valid_moves
    
    def generate_valid_scout_moves(self, scout_location: tuple[int,int])-> list[tuple[tuple[int, int], tuple[int, int]]]:
        valid_scout_moves: list[tuple: int,int] = []  # init list to return

        curr_row = scout_location[0]
        curr_col = scout_location[1]

        # figure out valid moves above
        still_valid = True
        while still_valid and curr_row <= 8:
            curr_row += 1
            candidate_square_type: Troop_Type = self.view.board[curr_row][curr_col].troop_type
            if candidate_square_type == Troop_Type.empty:
                # if next above square is empty, can move there, and can try for another square up
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
            elif candidate_square_type == Troop_Type.unknown:
                # next square above is occupied by enemy troop. Can attack it but can't move past
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
                still_valid = False
            else:
                # next square is water or occupied by this player's troop. Can't move to square or past it
                still_valid = False

        # figure out valid moves below
        curr_row = scout_location[0]
        curr_col = scout_location[1]
        still_valid = True
        while still_valid and curr_row >= 1:
            curr_row -= 1
            candidate_square_type: Troop_Type = self.view.board[curr_row][curr_col].troop_type
            if candidate_square_type == Troop_Type.empty:
                # if next above square is empty, can move there, and can try for another square up
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
            elif candidate_square_type == Troop_Type.unknown:
                # next square above is occupied by enemy troop. Can attack it but can't move past
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
                still_valid = False
            else:
                # next square is water or occupied by this player's troop. Can't move to square or past it
                still_valid = False
        
        # figure out valid moves to the left
        curr_row = scout_location[0]
        curr_col = scout_location[1]
        still_valid = True
        while still_valid and curr_col >= 1:
            curr_col -= 1
            candidate_square_type: Troop_Type = self.view.board[curr_row][curr_col].troop_type
            if candidate_square_type == Troop_Type.empty:
                # if next above square is empty, can move there, and can try for another square up
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
            elif candidate_square_type == Troop_Type.unknown:
                # next square above is occupied by enemy troop. Can attack it but can't move past
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
                still_valid = False
            else:
                # next square is water or occupied by this player's troop. Can't move to square or past it
                still_valid = False

        # figure out valid moves to the right
        curr_row = scout_location[0]
        curr_col = scout_location[1]
        still_valid = True
        while still_valid and curr_col <= 8:
            curr_col += 1
            #print('ln 113', str(curr_row), str(curr_col))
            candidate_square_type: Troop_Type = self.view.board[curr_row][curr_col].troop_type
            if candidate_square_type == Troop_Type.empty:
                # if next above square is empty, can move there, and can try for another square up
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
            elif candidate_square_type == Troop_Type.unknown:
                # next square above is occupied by enemy troop. Can attack it but can't move past
                valid_scout_moves.append((scout_location, (curr_row, curr_col)))
                still_valid = False
            else:
                # next square is water or occupied by this player's troop. Can't move to square or past it
                still_valid = False

        return valid_scout_moves

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
        print('Player', str(self.player_number), 'to move')
        while True: ##### messsssyyyyyy but also way easier to just do this way (only way out to input a valid move)
            # start square input and validation
            valid_input_format = False
            while not valid_input_format:
                start_square_str = input('enter start square in form \'row, col\'')
                valid_input_format = True  # track if input is good
                try:
                    start_sq_row = int(start_square_str[0])
                    assert start_square_str[1] == ','
                    start_sq_col = int(start_square_str[2])
                    assert len(start_square_str) == 3
                except:
                    print('invalid format')
                    valid_input_format = False

            valid_input_format = False
            while not valid_input_format:
                end_square_str = input('enter end square in form \'row, col\'')
                valid_input_format = True  # track if input is good
                try:
                    end_sq_row = int(end_square_str[0])
                    assert end_square_str[1] == ','
                    end_sq_col = int(end_square_str[2])
                    assert len(end_square_str) == 3
                except:
                    print('invalid format')
                    valid_input_format = False
            
            full_move_candidate = ((start_sq_row, start_sq_col), (end_sq_row, end_sq_col))
            print('this is the selected move:', full_move_candidate)
            # okay now have good input. Check to see if the move is valid!
            valid_move_list = self.generate_valid_moves()
            print('here is a list of valid moves:', valid_move_list)

            if full_move_candidate in valid_move_list:
                print('selected move was valid')
                return full_move_candidate
            print('selected move was invalid')
        
    

class Computer(Player):
    INITAL_PROB_DICT = {Troop_Type.flag: .025, 
                        Troop_Type.bomb: .15,
                        Troop_Type.marshal: .025,
                        Troop_Type.general: .025,
                        Troop_Type.colonel: .05,
                        Troop_Type.major: .075,
                        Troop_Type.captain: .1,
                        Troop_Type.lieutenant: .1,
                        Troop_Type.sergeant: .1,
                        Troop_Type.miner: .125,
                        Troop_Type.scout: .2,
                        Troop_Type.spy: .025,
                        Troop_Type.empty: 0,
                        Player_Owner.player_1: 0,
                        Player_Owner.player_2: 0}
    INITAL_PROB_DICT_EMPTY = {Troop_Type.flag: 0, 
                              Troop_Type.bomb: 0,
                              Troop_Type.marshal: 0,
                              Troop_Type.general: 0,
                              Troop_Type.colonel: 0,
                              Troop_Type.major: 0,
                              Troop_Type.captain: 0,
                              Troop_Type.lieutenant: 0,
                              Troop_Type.sergeant: 0,
                              Troop_Type.miner: 0,
                              Troop_Type.scout: 0,
                              Troop_Type.spy: 0,
                              Troop_Type.empty: 1,
                              Player_Owner.player_1: 0,
                              Player_Owner.player_2: 0}
    
    def __init__(self, player_number: int) -> None:
        super().__init__(player_number)
        self.initial_position = self.computer_select_initial_position()
        self.prob_dict = {}
        self.view = self.initialize_compuer_view()
        self.seen_dict: dict[Troop_Type:int] = {}
        self.killed_dict: dict[Troop_Type:int] = {}

    
    def initialize_comp_dicts(self):
        for troop_int_val in range(0,12):
            # troop types have a value from 0 to 11
            self.seen_dict[Troop_Type(troop_int_val)] = 0  # no enemy troops seen
            self.killed_dict[Troop_Type(troop_int_val)] = 0  # no enemy troops killed
    
    def initialize_compuer_view(self):
        # set up dictionary structure
        for row in range(10):
            for col in range(10):
                # create keys and empty dicts for all cells on the board
                self.prob_dict[(row, col)] = self.INITAL_PROB_DICT_EMPTY.copy()
                # TODO: maybe come back here and get rid of the lakes, shouldn't actually be an issue tho
                # those neurons should die p quick

        # init prob dict for enemy troop locations
        if self.player_number == 1:
            # own troops are on bottom four rows, enemy on top four
            for row in range(6, 10):
                for col in range(10):
                    self.prob_dict[(row, col)] = self.INITAL_PROB_DICT.copy()
                    self.prob_dict[(row, col)][Player_Owner.player_2] = 1  # need to set the enemy player owner right
        else:
            # own troops are on top 4 rows, enemy on bottom 4
            for row in range(4):
                for col in range(10):
                    self.prob_dict[(row, col)] = self.INITAL_PROB_DICT.copy()
                    self.prob_dict[(row, col)][Player_Owner.player_1] = 1  # need to set the enemy player owner right
        
        # fix prob dict for all own troop locations
        if self.player_number == 1:  # troops start on bottom 4
            for row in range(4):
                for col in range(10):  # iterate thru the list of troops
                    init_troop_type_val = self.initial_position[row][col].value
                    #print('(', row , ',', col, '): ', init_troop_type_val, Troop_Type(init_troop_type_val))
                    self.prob_dict[(row,col)][Troop_Type(init_troop_type_val)] = 1
                    self.prob_dict[(row,col)][Troop_Type.empty] = 0
                    self.prob_dict[(row,col)][Player_Owner.player_1] = 1
        else:  # troops start on top 4
            for row in range(9, 5, -1):
                for col in range(10):
                    init_pos_row = 0  # adjust for diff index stuff
                    init_troop_type = self.initial_position[init_pos_row][col]  # extract troop type
                    self.prob_dict[(row,col)][init_troop_type] = 1  # correctly set troop type
                    self.prob_dict[(row,col)][Troop_Type.empty] = 0  # tile is not empty
                    self.prob_dict[(row,col)][Player_Owner.player_2] = 1  # set player owner
                    init_pos_row += 1

        return [[]]
    
    def update_computer_view(self, start_loc: tuple[tuple], end_loc: tuple[tuple], start_troop_type: Troop_Type, end_troop_type: Troop_Type) -> bool:
        #write later
        return True
    
    def computer_select_initial_position(self) -> list[list[Troop_Type]]:
        init_pos_list = []
        init_pos_list.append([Troop_Type.flag, Troop_Type.bomb, Troop_Type.bomb, Troop_Type.bomb, Troop_Type.bomb, Troop_Type.bomb, Troop_Type.bomb, Troop_Type.marshal, Troop_Type.general, Troop_Type.colonel])
        init_pos_list.append([Troop_Type.colonel, Troop_Type.major, Troop_Type.major, Troop_Type.major, Troop_Type.captain, Troop_Type.captain, Troop_Type.captain, Troop_Type.captain, Troop_Type.lieutenant, Troop_Type.lieutenant])
        init_pos_list.append([Troop_Type.lieutenant, Troop_Type.lieutenant, Troop_Type.sergeant, Troop_Type.sergeant, Troop_Type.sergeant, Troop_Type.sergeant, Troop_Type.miner, Troop_Type.miner, Troop_Type.miner, Troop_Type.miner])
        init_pos_list.append([Troop_Type.miner, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.scout, Troop_Type.spy])
        return init_pos_list
    