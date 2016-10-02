from enum import Enum


class GameStyle(Enum):
    monopoly = 1
    scrabble = 2


class MonopolyPieceStyle(Enum):
    dog = 1
    sheep = 2
    car = 3
    mobilephone = 4


class Game:
    '''Represents the game being played'''
    def __init__(self, gs, cntPlayers,):
        if gs != GameStyle.monopoly:
            raise NotImplementedError("Only Monopoloy is supported currently")
        if cntPlayers > len(MonopolyPieceStyle):
            raise NotImplementedError("Two many players for the number of available pieces")


class Board:
    '''Represents the board of the game being played'''
    def __init__(self, ):
        pass


class Player:
    '''Represents a player of the game'''
    def __init__(self):
        pass


class Players:
    '''Represents a player of the game'''
    def __init__(self, cnt):
        pass


class Place:
    '''Represents a position of the game'''
    def __init__(self):
        pass


class Square(Place):
    '''
    Represents a position for a game
    where positions are 'squares'
    (such as Monopoly)
    '''
    def __init__(self):
        pass


class Piece():
    '''
    Represents the token belonging
    to a given `Player`
    '''
    def __init__(self):
        pass
