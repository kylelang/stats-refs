### Title:    Format BibTex file
### Author:   Kyle M. Lang
### Created:  2019-10-29
### Modified: 2019-10-30

import sys
import modBibFiles as mbf

## Extract command line arguments:
args = sys.argv

## Add annotations to BibTex file:
mbf.formatBib(iFile = args[1], oFile = args[2])

