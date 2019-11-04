### Title:    Find BibTex Files Used in a LaTeX file
### Author:   Kyle M. Lang
### Created:  2019-10-31
### Modified: 2019-10-31

import sys
import re

args = sys.argv

with open(args[1], "r") as f0: tex = f0.read()
    
bibs = re.findall("\w+\\.bib", tex)

for f in set(bibs): print(f)
    
        

