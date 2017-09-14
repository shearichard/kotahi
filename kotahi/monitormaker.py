# -*- coding: utf-8 -*-
'''
Produces a JS file which may be used to drive a graphical respresentation of
the changing state of the  underlying game

Given a directory of files will read through each of them and by reading the 
contents generate a JS file which contains an datastructure which is the 
equivalent to the contents of the files
'''

import os
import pprint
import argparse
import glob
import jsonpickle

OUTPUTFILENAME = "gamestate.js"

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PathError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


def getargs():
    parser = argparse.ArgumentParser(description='Parse directory of board game state files and outputs a JS data structure equivalent.')
    parser.add_argument('-i','--inputdir', help='Directory containing the input files', required=True)
    parser.add_argument('-o','--outputdir', help='Directory into which the output files should be written.', required=True)
    args = vars(parser.parse_args())

    return args


def makeoutputpath(args):
    return os.path.join(args['outputdir'], OUTPUTFILENAME)


def validateargs(args):
    if os.path.isdir(args['inputdir']) == False:
        raise PathError("The inputdir path does not exist")
    if os.path.isdir(args['outputdir']) == False:
        raise PathError("The outputdir path does not exist")
    if os.path.exists(makeoutputpath(args)):
        raise PathError("The output file already exists")


def processfiles(outputpath, inputdir):

    strout = ""
    lstpath = glob.glob(os.path.join(inputdir, '*'))
    lstpath.sort()

    with open(outputpath, 'w', encoding='utf-8') as fout:
        fout.write('o={}\n')
        for p in lstpath:
            with open(p, 'r', encoding='utf-8') as fin:
                thawed = jsonpickle.decode(fin.read())
                fout.write("o[{0}]={1};\n\n".format(thawed['turnid'], pprint.pformat(thawed)))

def main():
    dargs = getargs()
    validateargs(dargs)
    pprint.pprint(dargs)
    processfiles(makeoutputpath(dargs), dargs['inputdir'])


if __name__ == "__main__":
    main()
