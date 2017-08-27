# -*- coding: utf-8 -*-

from helpers import Game, GameStyle


def main():
    g = Game(GameStyle.monopolyuk, 4)

    for i in range(10):
        g.playaturn()

    g.reportStatus()

if __name__ == "__main__":
    main()
