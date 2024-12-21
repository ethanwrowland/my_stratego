# from Board import Board
# from Board import Tile
# from Troop_Type import Troop_Type
# from Player_Owner import Player_Owner

# from Game import Game


#test_board = Board()
#print(test_board.get_adjacent_squares((0,0)))

# p1_miner = Tile(Troop_Type.miner, Player_Owner.player_1)
# p2_scout = Tile(Troop_Type.scout, Player_Owner.player_2)

# test_board.board[4][4] = p1_miner
# test_board.board[4][5] = p2_scout


# print("################ master view ###############")
# test_board.print_board()

# view_1, view_2 = test_board.return_view_boards()

# print("################ p1 view ###############")
# view_1.print_board()
# print("################ p2 view ###############")
# view_2.print_board()


# doing_game = Game('human', 'human', "True")
# doing_game.testing_functions()



from Player import Player
from Player import Computer

test_comp_player = Computer(2)
# for key, value in test_comp_player.prob_dict[(0,0)]:
#     print(key.name, value)
print()
print(test_comp_player.prob_dict[(1,1)])
print('\n')
print(test_comp_player.prob_dict[(9,9)])
print('\n')
print(test_comp_player.prob_dict[(4,9)])
