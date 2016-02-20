#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import re
import sys, getopt

nl = True
prevlinecode = False
output = ""

def code(s):
    global nl
    global prevlinecode
    if s.startswith(" "):
        nl = False
        if not prevlinecode:   
             s = "```\n" + s
             prevlinecode = True
    return s

def headers(s):
    # changes "^={1,3}" in "^#{1,3} "
    global nl
    global prevlinecode

    for n in range(3,0,-1):
    	if s.startswith("=" * n):
            s = re.sub("^" + "=" * n, "#" * n + " ",s)
	    if prevlinecode:
		s = "```\n" + s
	    	prevlinecode = False
            nl = False
    return s

def normal(s):
    global nl
    global prevlinecode
   
    if nl and s != "" :
        if prevlinecode:
            s = "```\n" + s
	    prevlinecode = False
        s = s + "\n"
    return s

def convert(s):
    global nl 
    global output

    nl = True

    s = headers(s)
    s = code(s)
    s = normal(s)

    output = output + s + "\n"

def main(argv):
    global inputfile 
    global outputfile
    global output

    if len(argv) != 4:
        print 'didwiki2md.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
       print 'didwiki2md.py -i <inputfile> -o <outputfile>'
       sys.exit(2)

    for opt, arg in opts:
       if opt in ("-h"):
          print 'didwiki2md.py -i <inputfile> -o <outputfile>'
          sys.exit()
       elif opt in ("-i"):
          inputfile = arg
       elif opt in ("-o"):
          outputfile = arg

    with open(inputfile,"r") as fd:
        for line in fd:
            convert(line.rstrip())
    fd.close()

    ## verify if code at end of document
    if prevlinecode:
        output = output + "```\n"

    fd = open(outputfile,"w") 
    fd.write(output)
    fd.close() 

###########################################################################

if __name__ == "__main__":
   main(sys.argv[1:])
