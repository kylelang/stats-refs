### Title:    Test Python Parsing/Modification of BibTex files
### Author:   Kyle M. Lang
### Created:  2019-10-29
### Modified: 2019-10-29

import sys
import modBibFiles as mbf

## Extract command line arguments:
args = sys.argv

## Add annotations to BibTex file:
mbf.extendBib(rawFile = args[1], extFile = args[2], outFile = args[3])

