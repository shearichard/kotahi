from enum import Enum


class GameStyle(Enum):
    monopolyuk = 1
    scrabble = 2


class MonopolyPieceStyle(Enum): 
    dog = 0 
    sheep = 1
    car = 2
    mobilephone = 3


class MonopolySquareStyle(Enum):
    go = 1
    jail = 2
    freeparking = 3
    communitychest = 4
    chance = 4
    tax = 5
    property = 6


class MonopolyPropertySquareSide(Enum):
    first = 1
    second = 2
    third = 3
    fourth= 4


class MonopolyPropertyStyle(Enum):
    brown = 1
    lightblue = 2
    pink = 3
    orange = 4
    red = 5
    yellow = 6
    green = 7
    darkblue = 8
    transport = 9
    utilities = 9

'''
dicProps = {}
dicProps['uk'] = []
dicProps['us'] = []
dicProps['uk'].append(Square('Old Kent Road', MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Mediterranean Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Whitechapel Road', MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Baltic Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('The Angel Islington', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Oriental Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Euston Road', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Vermont Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Pentonville Road', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Connecticut Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Pentonville Road', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Connecticut Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Pall Mall', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('St Charles Place', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Whitehall', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('States Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Northumberland Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Virginia Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Bow Street', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('St James Place', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Marlborough Street', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('Tennessee Place', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))
dicProps['uk'].append(Square('Vine Street', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))
dicProps['us'].append(Square('New York Avenue', MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.first))

Brown (Dark Purple)

    Old Kent Road/Mediterranean Avenue
    Whitechapel Road/Baltic Avenue 

Light Blue

    The Angel Islington/Oriental Avenue
    Euston Road/Vermont Avenue
    Pentonville Road/Connecticut Avenue 

Pink

    Pall Mall/St. Charles Place
    Whitehall/States Avenue
    Northumberland Avenue/Virginia Avenue 

Orange

    Bow Street/St. James Place
    Marlborough Street/Tennessee Avenue
    Vine Street/New York Avenue 

Red

    The Strand/Kentucky Avenue
    Fleet Street/Indiana Avenue
    Trafalgar Square/Illinois Avenue 

Yellow

    Leicester Square/Atlantic Avenue
    Coventry Street/Ventnor Avenue
    Piccadilly/Marvin Gardens 

Green

    Regent Street/Pacific Avenue
    Oxford Street/North Carolina Avenue
    Bond Street/Pennsylvania Avenue 

Dark Blue

    Park Lane/Park Place
    Mayfair/Boardwalk 

Stations

    King's Cross Station/Reading Railroad
    Marylebone Station/Pennsylvania Railroad
    Fenchurch St Station/B. & O. Railroad
    Liverpool Street Station/Short Line 

Utilities

    Electric Company
    Water Works 
'''

class Game:
    '''Represents the game being played'''
    def __init__(self, gs, cntPlayers,):


        if gs not in (GameStyle.monopolyuk, ):
            raise NotImplementedError("Only Monopoly is supported currently")
        else:
            self._gameStyle = gs
            if cntPlayers > len(MonopolyPieceStyle):
                raise NotImplementedError("Too many players for the number of available pieces")
            else:
                self._playerCount = cntPlayers
                
            self._players = []
            self.__initializeMonopolyStyleGame()

            for p in self._players:
                print(p)

    def __initializeMonopolyStyleGame(self):
        for i in range(self._playerCount):
            self._players.append(Player(MonopolyPieceStyle(i)))


class Board:
    '''Represents the board of the game being played'''
    def __init__(self, ):
        pass


class Player:
    '''Represents a player of the game'''
    def __init__(self, pieceStyle):
        self._pieceStyle = pieceStyle
    def __repr__(self):
        return self._pieceStyle.name


class Players:
    '''Represents all players of the game'''
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
    def __init__(self, name, sqstyle, propertystyle, sqside ):
        self.name = name 
        self.name = name 


class Piece():
    '''
    Represents the token belonging
    to a given `Player`
    '''
    def __init__(self):
        pass
