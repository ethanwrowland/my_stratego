import Tile
import Troop_Type

class Human: 
    def __init__(self, player_number: int) -> None:
        self.player_number = player_number
        self.view = [[]]
        return None
    
    def update_view(current_board: list[list]) -> list[list]:
        return self.view

class Computer:
    def __init__(self, player_number: int) -> None:
        self.player_number = player_number
        self.view = self.initialize_compuer_view()
    
    def initialize_compuer_view(self):
        # write later
        return [[]]
    
    def update_computer_view(self, start_loc: tuple[tuple], end_loc: tuple[tuple], start_troop_type: Troop_Type, end_troop_type: Troop_Type) -> bool:
        #write later
        return True
    