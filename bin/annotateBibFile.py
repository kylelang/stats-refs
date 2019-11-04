### Title:    Annotate BibTex file
### Author:   Kyle M. Lang
### Created:  2019-10-29
### Modified: 2019-11-04

### USAGE:
###   python annotateBibFile.py RAW_FILE ANN_FILE OUT_FILE

### ARGS:
###   RAW_FILE = Absolute or relative path (including file name and extension)
###              to the file containing the raw BibTex entries
###   ANN_FILE = Absolute or relative path (including file name and extension)
###              to the file containing the annotations
###   OUT_FILE = Absolute or relative path (including file name and extension)
###              to the file to be produced

import sys
import modBibFiles as mbf

## Extract command line arguments:
args = sys.argv

## Add annotations to BibTex file:
mbf.extendBib(rawFile = args[1], extFile = args[2], outFile = args[3])

