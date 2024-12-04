from enum import Enum

class Troop_Type(Enum):
    # normal troops
    spy = 1
    scout = 2
    miner = 3
    sergeant = 4
    lieutenant = 5
    captain = 6
    major = 7
    colonel = 8
    general = 9
    marshal = 10
    # edge cases (subject to change)
    empty = 0
    bomb = 11
    flag = -1
    water = 12
    unknown = 13