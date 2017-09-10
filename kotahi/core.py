# -*- coding: utf-8 -*-

from money import Money
from helpers import Game, GameStyle, MONEYPERPLAYERSTART, MONEYBANKSTART


def main():
    g = Game(GameStyle.monopolyuk, 4, MONEYPERPLAYERSTART, MONEYBANKSTART )

    g.board_health_check()

    for i in range(500):
        g.play_a_turn()

    g.reportStatus()


if __name__ == "__main__":
    main()
