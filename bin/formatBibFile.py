### Title:    Format BibTex file
### Author:   Kyle M. Lang
### Created:  2019-10-29
### Modified: 2019-11-04

### USAGE:
###   python formatBibFile.py IN_FILE OUT_FILE

### ARGS:
###   IN_FILE  = Absolute or relative path (including file name and extension)
###              to the file to be formatted
###   OUT_FILE = Absolute or relative path (including file name and extension)
###              to the file to be produced

import sys
import modBibFiles as mbf

## Extract command line arguments:
args = sys.argv

## Add annotations to BibTex file:
mbf.formatBib(iFile = args[1], oFile = args[2])

