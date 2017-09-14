# -*- coding: utf-8 -*-

import tempfile
import os

import jsonpickle

from money import Money
from helpers import Game, GameStyle, MONEYPERPLAYERSTART, MONEYBANKSTART

def makeTempDir():
    path2dir = tempfile.mkdtemp()
    return path2dir


def getTempPath(fName, dPath=None):
    if dPath==None:
        path2dir = makeTempDir()
    else:
        path2dir = dPath
    fullpath = os.path.join(path2dir,fName)
    return fullpath


def main():
    g = Game(GameStyle.monopolyuk, 4, MONEYPERPLAYERSTART, MONEYBANKSTART )

    g.board_health_check()

    path2dir = makeTempDir()


    for i in range(50):
        g.play_a_turn()
        print(path2dir)
        pth2file = os.path.join(path2dir, "%06d" % i + ".json")
        with open(pth2file, 'w', encoding='utf-8') as f:
            frozen_game_json = jsonpickle.encode(g.make_freeze_ready_game_dic(i))
            f.write(frozen_game_json)

    g.reportStatus()
    print(path2dir)

if __name__ == "__main__":
    main()
