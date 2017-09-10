# -*- coding: utf-8 -*-

from money import Money
from helpers import Game, GameStyle


def main():
    g = Game(GameStyle.monopolyuk, 4, Money(amount='5000.00', currency='UKP'), Money(amount='100000.00', currency='UKP') )

    g.board_health_check()

    for i in range(500):
        g.play_a_turn()

    g.reportStatus()


if __name__ == "__main__":
    main()
