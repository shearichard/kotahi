from enum import Enum
from money import Money
from random import randint


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
    chance = 5
    tax = 6
    property = 7
    gotojail = 8


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
    utilities = 10 
    misc = 11 

class MonopolyPropertySiteAcquistionStyle(Enum): 
    random = 0 

class MonopolyPropertyDevelopmentAcquistionStyle(Enum): 
    random = 0 

class MonopolyBoardStyle(Enum): 
    uk = 0 
    us = 1 


'''
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
    def __init__(self, gs, cnt_players,):


        if gs not in (GameStyle.monopolyuk, ):
            raise NotImplementedError("Only Monopoly is supported currently")
        else:
            self._gameStyle = gs
            if cnt_players > len(MonopolyPieceStyle):
                raise NotImplementedError("Too many players for the number of available pieces")
            elif cnt_players < 2:
                raise NotImplementedError("Too few players for the game rules to make sense")
            else:
                self._player_count = cnt_players
                
            self.lst_of_players = [] 
            self.next_player_idx = None
            self.board = [] 

            self.__initialize_monopoly_style_game(cnt_players, Money(amount='10000.00', currency='NZD'), MonopolyBoardStyle.uk)


    def __initialize_monopoly_style_game(self, cnt_players, starting_funds, board_style):
        self.board = self.__build_board(board_style)

        #Create as many players as we need 
        #allocating a piece to each
        for i in range(cnt_players):
            self.lst_of_players.append(Player(MonopolyPieceStyle(i), 
                                starting_funds,
                                MonopolyPropertySiteAcquistionStyle.random,
                                MonopolyPropertyDevelopmentAcquistionStyle.random));

        self.next_player_idx = randint(0, cnt_players - 1) 

    def board_health_check(self):

        #Check Sides
        for side in MonopolyPropertySquareSide:
            cnt = 0
            for square in self.board:
                if square.square_side == side:
                    cnt += 1

            print ("Side {0} has {1} squares".format(side.name, cnt))

        print("")
        #Check Square Style
        dicstylecnt = {}
        for style in MonopolySquareStyle:
            cnt = 0
            for square in self.board:
                if square.square_style == style:
                    if style in dicstylecnt:
                        dicstylecnt[style] += 1
                    else:
                        dicstylecnt[style] = 1

        for k, v in dicstylecnt.items():
            print ("Style {0} has {1} squares".format(k.name, v))

        print("")




    def __build_board(self, board_style):

        dicProps = {}
        dicProps['uk'] = []
        dicProps['us'] = []

        #First Side ===========================================================================================================================

        dicProps['uk'].append(Square('Go', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.go, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Go', Money(amount='0.00', currency='USD'), MonopolySquareStyle.go, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Old Kent Road', Money(amount='60.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Mediterranean Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Community Chest', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Community Chest', Money(amount='0.00', currency='USD'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Whitechapel Road', Money(amount='60.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Baltic Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.brown, MonopolyPropertySquareSide.first))
        
        dicProps['uk'].append(Square('Income Tax', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.tax, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Income Tax', Money(amount='0.00', currency='USD'), MonopolySquareStyle.tax, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Kings Cross Stations', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Reading Railroad', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('The Angel Islington', Money(amount='100.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Oriental Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Chance', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Chance', Money(amount='0.00', currency='USD'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.first))
        
        dicProps['uk'].append(Square('Euston Road', Money(amount='100.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Vermont Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))

        dicProps['uk'].append(Square('Pentonville Road', Money(amount='120.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))
        dicProps['us'].append(Square('Connecticut Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.lightblue, MonopolyPropertySquareSide.first))

        #Second Side ==========================================================================================================================

        dicProps['uk'].append(Square('Jail', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.jail, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Jail', Money(amount='0.00', currency='USD'), MonopolySquareStyle.jail, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Pall Mall', Money(amount='140.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('St Charles Place', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Electricity Company', Money(amount='150.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.utilities, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Electricity Company', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.utilities, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Whitehall', Money(amount='140.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('States Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Northumberland Avenue', Money(amount='160.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Virginia Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.pink, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Marylebone Station', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Pennsylvania Railroad', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Bow Street', Money(amount='180.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('St James Place', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Community Chest', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Community Chest', Money(amount='0.00', currency='USD'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Marlborough Street', Money(amount='180.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('Tennessee Place', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))

        dicProps['uk'].append(Square('Vine Street', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))
        dicProps['us'].append(Square('New York Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.orange, MonopolyPropertySquareSide.second))

        #Third Side ===========================================================================================================================

        dicProps['uk'].append(Square('Free Parking', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.freeparking, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Free Parking', Money(amount='0.00', currency='USD'), MonopolySquareStyle.freeparking, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Strand', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Kentucky Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Chance', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Chance', Money(amount='0.00', currency='USD'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Fleet Street', Money(amount='220.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Indiana Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Trafalger Square', Money(amount='240.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Illinois Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.red, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Fenchurch St Station', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('B&O Railroad', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Leicester Square', Money(amount='260.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Atlantic Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Coventry Street', Money(amount='260.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Ventnor Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Water Works', Money(amount='150.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.utilities, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Water Works', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.utilities, MonopolyPropertySquareSide.third))

        dicProps['uk'].append(Square('Piccadilly', Money(amount='280.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))
        dicProps['us'].append(Square('Marvin Gardens', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.yellow, MonopolyPropertySquareSide.third))

        #Fourth Side ==========================================================================================================================

        dicProps['uk'].append(Square('Go To Jail', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.gotojail, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Go To Jail', Money(amount='0.00', currency='USD'), MonopolySquareStyle.gotojail, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Regent Street', Money(amount='300.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Pacific Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Oxford Street', Money(amount='300.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('North Carolina Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Community Chest', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Community Chest', Money(amount='0.00', currency='USD'), MonopolySquareStyle.communitychest, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Bond Street', Money(amount='320.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Pennsylvania Avenue', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.green, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Liverpool St Station', Money(amount='200.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Short Line', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.transport, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Chance', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Chance', Money(amount='0.00', currency='USD'), MonopolySquareStyle.chance, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Park Lane', Money(amount='350.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.darkblue, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Park Place', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.darkblue, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Super Tax', Money(amount='0.00', currency='UKP'), MonopolySquareStyle.tax, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Super Tax', Money(amount='0.00', currency='USD'), MonopolySquareStyle.tax, MonopolyPropertyStyle.misc, MonopolyPropertySquareSide.fourth))

        dicProps['uk'].append(Square('Mayfair', Money(amount='400.00', currency='UKP'), MonopolySquareStyle.property, MonopolyPropertyStyle.darkblue, MonopolyPropertySquareSide.fourth))
        dicProps['us'].append(Square('Boardwalk', Money(amount='20000.00', currency='USD'), MonopolySquareStyle.property, MonopolyPropertyStyle.darkblue, MonopolyPropertySquareSide.fourth))


        return dicProps[board_style.name]


    def throw_dice(self):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        return {'dotcnt': dice1 + dice2, 'wasdouble' : (dice1 == dice2)}

    def playaturn(self):
        while (True):
            dic_dice_throw = self.throw_dice()
            break
            
        

    def reportStatus(self):
        for p in self.lst_of_players:
            print("{0} - ({1})".format(p.piece_style.name, p.funds))



class Board:
    '''Represents the board of the game being played'''
    def __init__(self, ):
        pass


class Player:
    '''Represents a player of the game'''
    def __init__(self, pc_sty, funds, site_aq_style, prop_dev_style):
        self.piece_style = pc_sty
        self.funds = funds
        self.site_aq_style = site_aq_style
        self.prop_dev_style = prop_dev_style
            
    def __repr__(self):
        return self.piece_style.name 


class Players:
    '''Represents all players of the game'''
    def __init__(self, cnt):
        self.lst_of_players = []


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
    def __init__(self, name, price, square_style, property_style, square_side ):
        self.name = name 
        self.price = price
        self.square_style = square_style 
        self.property_style = property_style 
        self.square_side = square_side 

    def __repr__(self):
        return "{0} - Price {1} ({2} / {3})".format(self.name, self.price, self.square_style.name, self.property_style.name)

class Piece():
    '''
    Represents the token belonging
    to a given `Player`
    '''
    def __init__(self):
        pass
