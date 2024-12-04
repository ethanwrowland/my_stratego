from enum import Enum
from Troop_Type import Troop_Type
from Player_Owner import Player_Owner

class Tile:
    def __init__(self, troop_type: Troop_Type, player_owner: Player_Owner) -> None:
        self.troop_type = troop_type
        self.player_owner = player_owner
    
