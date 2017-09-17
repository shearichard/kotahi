# -*- coding: utf-8 -*-
'''
Produces a JS file which may be used to drive a graphical respresentation of
the changing state of the  underlying game

Given a directory of files will read through each of them and by reading the 
contents generate a JS file which contains an datastructure which is the 
equivalent to the contents of the files
'''

import os
import shutil
import pprint
import argparse
import glob
import jsonpickle

from pybars import Compiler

STATIC_JS_FILENAME = "gamestate-static.js"
OUTPUT_JS_FILENAME = "gamestate.js"
OUTPUT_HTML_FILENAME = "gamestate.html"
HTML_TEMPLATE_FILENAME = "gamestate.hbr"
DYNAMIC_JS_TOP = '''
var TCG = TCG || function () { };
TCG.MDA = function () {
    foo = function () {
      //
    }
    bar = function() {
      //
    }
    return {
        //PUBLIC AREA
        buildDataStructure : function () {
'''
DYNAMIC_JS_BOTTOM = '''
            return o;
        },
    };
}();
'''

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
    parser.add_argument('-t','--template', help='Directory containing the gamestate.hbr template basis of the html output.', required=True)
    args = vars(parser.parse_args())

    return args


def make_path_to_js_static_output(args):
    return os.path.join(args['outputdir'], STATIC_JS_FILENAME)

def make_path_to_js_output(args):
    return os.path.join(args['outputdir'], OUTPUT_JS_FILENAME)

def make_path_to_html_output(args):
    return os.path.join(args['outputdir'], OUTPUT_HTML_FILENAME)

def make_path_to_html_template(args):
    return os.path.join(args['template'], HTML_TEMPLATE_FILENAME)


def validateargs(args):
    #Input dir exists ?
    if os.path.isdir(args['inputdir']) == False:
        raise PathError("The inputdir path does not exist")
    #Output dir exists ?
    if os.path.isdir(args['outputdir']) == False:
        raise PathError("The outputdir path does not exist")
    #JS output file already exists ?        
    if os.path.exists(make_path_to_js_output(args)):
        raise PathError("The js output file already exists")
    #HTML output file already exists ?        
    if os.path.exists(make_path_to_html_output(args)):
        raise PathError("The html output file already exists")
    #HTML template exists ?        
    if os.path.exists(make_path_to_html_template(args)) == False:
        raise PathError("The template file does not exist")


def processfiles(   path_to_output_js, 
                    path_to_output_html, 
                    path_to_html_template, 
                    path_to_output_static_js,
                    inputdir):

    strout = ""
    lstpath = glob.glob(os.path.join(inputdir, '*'))
    lstpath.sort()

    #Build HTML file corresponding to game squares etc
    lstout = []
    for idxrows in range(12):
        lstout.append('''<div class='row'>''')
        for idxcols in range(12):
            lstout.append('''<div class='col-md-1'><div class='demo-content'>{0}/{1}</div></div>'''.format(idxcols + 1, idxrows + 1))
        lstout.append('''</div>''')
    strout = ''.join(lstout)

    #Copy the static JS to whereever the output file is going so that
    #it can be served easily to the requesting HTML page
    shutil.copyfile(os.path.join('.', STATIC_JS_FILENAME), path_to_output_static_js) 

    #Build HTML file corresponding to game squares etc
    with open(path_to_html_template, 'r', encoding='utf-8') as ftemplate:
        template = ftemplate.read()
        with open(path_to_output_html, 'w', encoding='utf-8') as fhtmlout:
            fhtmlout.write(template.format(testrow=strout))
            #fhtmlout.write(template)
            

    #Build JS structure
    with open(path_to_output_js, 'w', encoding='utf-8') as fout:

        fout.write(DYNAMIC_JS_TOP)
        fout.write('o={}\n')
        for p in lstpath:
            with open(p, 'r', encoding='utf-8') as fin:
                thawed = jsonpickle.decode(fin.read())
                fout.write("o[{0}]={1};\n\n".format(thawed['turnid'], pprint.pformat(thawed)))
        fout.write(DYNAMIC_JS_BOTTOM)

def main():
    dargs = getargs()
    validateargs(dargs)
    pprint.pprint(dargs)
    processfiles(   make_path_to_js_output(dargs), 
                    make_path_to_html_output(dargs),
                    make_path_to_html_template(dargs),
                    make_path_to_js_static_output(dargs),
                    dargs['inputdir'])


if __name__ == "__main__":
    main()
