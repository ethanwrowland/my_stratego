from Game_State import Game_State
from Troop_Type import Troop_Type
from Board import Board
from Board import Tile
from Player import Player
from Player import Human
from Player import Computer

from Player_Owner import Player_Owner



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

        # # play game
        # while self.game_state != -3:  # no player has won 
        #     match self.game_state:
        #         case Game_State.player_1_to_move:
        #             self.display_game_board()
        #             if not self.detect_player_stuck(self.player_1):
        #                 # p1 is not stuck, allow p1 to move
        #                 self.execute_turn(self.player_1)

        #         case Game_State.player_2_to_move:
        #             self.display_game_board()
        #             if not self.detect_player_stuck(self.player_2):
        #                 # p2 is not stuck, allow p2 to move
        #                 self.execute_turn(self.player_2)
                
        #         case Game_State.player_1_victory:
        #             self.display_game_board()
        #             print("Player 1 wins!")
        #             self.game_state = Game_State.game_finished

        #         case Game_State.player_2_victory:
        #             self.display_game_board()
        #             print("Player 2 wins!")
        #             self.game_state = Game_State.game_finished
        

    def testing_functions(self):
        p1_miner = Tile(Troop_Type.miner, Player_Owner.player_1)
        p1_miner_1 = Tile(Troop_Type.miner, Player_Owner.player_1)
        p2_scout = Tile(Troop_Type.scout, Player_Owner.player_2)

        self.display_game_board()

        self.master_board.board[4][4] = p1_miner
        self.master_board.board[4][5] = p1_miner
        self.master_board.board[5][4] = p2_scout

        self.display_game_board()

        p1_view, p2_view = self.master_board.return_view_boards()
        p1_view.print_board()
        p2_view.print_board()
        print(p1_view, type(p1_view))
        self.player_1.view = p1_view
        self.player_2.view = p2_view
        

        print(self.player_1.generate_valid_moves())
        print(self.player_2.generate_valid_moves())

                

    def detect_player_stuck(self, player_to_check) -> bool:
        # detect if the given player is stuck (and update game state). If stuck, return true, false otw
        return False

    def execute_turn(self, moving_player: Player) -> Troop_Type:
        # start my seeing if the player to move has a valid move
        if self.detect_player_stuck(moving_player):
            if moving_player == self.player_1:
                self.game_state = Game_State.player_2_victory
            else:
                self.game_state = Game_State.player_1_victory
            
            return Troop_Type.unknown
        
        # if not stuck, proceed with turn
        if self.game_state != Game_State.player_1_victory and self.game_state != Game_State.player_2_victory:
            # get move from player
            (start_pos, end_pos) = moving_player.choose_move()
        
            # keep track of what to do with moving troops
            start_survives:bool = True
            end_survives:bool = True

            start_pos_troop_type: Troop_Type = self.master_board.board[start_pos[0]][start_pos[1]].troop_type
            end_pos_troop_type: Troop_Type = self.master_board.board[end_pos[0]][end_pos[1]].troop_type

            # case based on the end position
            match end_pos_troop_type:
                case Troop_Type.empty:
                    # moving troop always survives if moved into empty space, no need to update start_survives
                    pass
                case Troop_Type.flag:
                    end_survives = False  # flag "dies"
                    # game has been won, finish game
                    if moving_player == self.player_1:
                        self.game_state = Game_State.player_1_victory
                    else:
                        self.game_state = Game_State.player_2_victory
                # handle weird interactions/special cases
                case Troop_Type.marshal:
                    if start_pos_troop_type == Troop_Type.spy:
                        # if spy attacks marshal, marshal dies
                        start_survives = True
                        end_survives = False
                    else:
                        # everything else dies to marshal
                        start_survives = False
                case Troop_Type.bomb:
                    if start_pos_troop_type == Troop_Type.miner:
                        # miner can kill bomb
                        end_survives = False
                    else:
                        # everyone else dies to bomb :(
                        start_survives = False
                # attacked troop doesn't have special case
                case Troop_Type.spy | Troop_Type.scout | Troop_Type.miner | Troop_Type.sergeant | Troop_Type.lieutenant | Troop_Type.captain | Troop_Type.major | Troop_Type.colonel | Troop_Type.general:
                    print('attacking :', start_pos_troop_type.name, 'defending: ', end_pos_troop_type.name)
                    if start_pos_troop_type.value > end_pos_troop_type.value:
                        # start pos is stronger than end
                        end_survives = False
                    elif start_pos_troop_type.value == end_pos_troop_type.value:
                        # equal value means both died
                        start_survives = False
                        end_survives = False
                        print('okay its going wrong in this way')
                    else:
                        # start pos is weaker than end
                        start_survives = False

                case _:
                    print('bad troop type:', str(end_pos_troop_type.name))
                    raise Exception("impossible troop type in execute turn")
                
            # alright, now we know which pieces live and which dies
            if start_survives:
                print('start survives')
                self.master_board.move_troop(start_pos, end_pos)
            elif not start_survives and not end_survives:
                print('tie, both die')
                self.master_board.kill_troop(start_pos)
                self.master_board.kill_troop(end_pos)
            else:
                print('end kills start')
                # end killed start
                self.master_board.kill_troop(start_pos)

            return end_pos_troop_type
            
                    
                    



    def display_game_board(self):
        # this will handle displaying the board, given a variety of conditions/situations (more complicated later)
        if self.disp_board_bool:
            self.master_board.print_board()



    
