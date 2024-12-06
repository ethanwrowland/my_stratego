from Board import Board
from Board import Tile
from Troop_Type import Troop_Type
from Player_Owner import Player_Owner


test_board = Board()

p1_miner = Tile(Troop_Type.miner, Player_Owner.player_1)
p2_scout = Tile(Troop_Type.scout, Player_Owner.player_2)

test_board.board[0][0] = p1_miner
test_board.board[9][9] = p2_scout

print("################ master view ###############")
test_board.print_board()

view_1, view_2 = test_board.return_view_boards()

print("################ p1 view ###############")
view_1.print_board()
print("################ p2 view ###############")
view_2.print_board()